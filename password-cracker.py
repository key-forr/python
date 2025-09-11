import os
import time
import hashlib
import argparse
from multiprocessing import Process, Event, Queue, cpu_count

LENGTH = 6
lowChar = "abcdefghijklmnopqrstuvwxyz"
numChar = "0123456789"
spcChar = "!@#$%^&*_-"
CHARSET = lowChar + numChar + spcChar 
HASH_ALGORITHM = "blake2b"  
TARGET_HASH_HEX = (
    "6f0874bd7ba418106ac15555ea927aef34bc05c8ba92cd2e4c3065e7751ccc125fd88f19eec18f007e9f033c8dd2749edf573ac8aeec47d073f5832553fcea9c"
)

def n_cpu():
    """Return number of CPU cores available."""
    c = os.cpu_count()
    return c or cpu_count()


def blake2b_hex(s: str) -> str:
    return hashlib.blake2b(s.encode("utf-8")).hexdigest()


def idx_to_candidate(idx: int, length: int, charset: str) -> str:
    """Convert an integer index to a candidate string in base len(charset).

    Index 0 -> charset[0]*length (i.e. first lexicographic string), etc.
    The ordering is lexicographic where the leftmost character changes slowest.
    """
    base = len(charset)
    chars = []
    for _ in range(length):
        chars.append(charset[idx % base])
        idx //= base
    return ''.join(reversed(chars))


def sequential_search(length: int, charset: str, target_hash_hex: str, max_checks: int = None):
    """Sequential brute-force search. If max_checks is None, tries the whole space.

    Returns: (found_password_or_None, checks_done, elapsed_seconds)
    """
    total = len(charset) ** length
    if max_checks is None:
        max_checks = total
    checks = 0
    start = time.perf_counter()

    for idx in range(total):
        candidate = idx_to_candidate(idx, length, charset)
        checks += 1
        if blake2b_hex(candidate) == target_hash_hex:
            elapsed = time.perf_counter() - start
            return candidate, checks, elapsed
        if checks >= max_checks:
            break
    elapsed = time.perf_counter() - start
    return None, checks, elapsed


def worker_process(proc_id: int, start_idx: int, step: int, length: int, charset: str,
                   target_hash_hex: str, stop_event: Event, out_q: Queue, progress_interval: int = 1_000_000):
    total = len(charset) ** length
    checks = 0
    idx = start_idx
    while idx < total and not stop_event.is_set():
        candidate = idx_to_candidate(idx, length, charset)
        if blake2b_hex(candidate) == target_hash_hex:
            out_q.put((candidate, proc_id, checks))
            stop_event.set()
            return
        checks += 1
        if checks % progress_interval == 0:
            out_q.put((None, proc_id, checks))
        idx += step
    return


def multiprocessing_search(length: int, charset: str, target_hash_hex: str, nprocs: int):
    total = len(charset) ** length
    stop_event = Event()
    out_q = Queue()
    procs = []
    start_time = time.perf_counter()

    # start processes
    for i in range(nprocs):
        p = Process(target=worker_process, args=(i, i, nprocs, length, charset, target_hash_hex, stop_event, out_q))
        p.start()
        procs.append(p)

    found = None
    checks_total = 0

    try:
        while True:
            try:
                item = out_q.get(timeout=0.5)
            except Exception:
                item = None

            if item is not None:
                candidate, proc_id, checks = item
                if candidate is None:
                    checks_total += checks
                else:
                    found = candidate
                    checks_total += checks
                    break

            alive = any(p.is_alive() for p in procs)
            if not alive:
                break
    finally:
        stop_event.set()
        for p in procs:
            p.join(timeout=1)
            if p.is_alive():
                p.terminate()
                p.join()

    elapsed = time.perf_counter() - start_time
    return found, checks_total, elapsed


def human_time(sec: float) -> str:
    if sec == float('inf'):
        return 'infinite/unknown'
    sec = int(sec)
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    parts = []
    if d:
        parts.append(f"{d}d")
    if h:
        parts.append(f"{h}h")
    if m:
        parts.append(f"{m}m")
    parts.append(f"{s}s")
    return ' '.join(parts)


def main():
    parser = argparse.ArgumentParser(description='Brute-force blake2b password (sequential and multiprocessing)')
    parser.add_argument('--length', type=int, default=LENGTH, help='Password length')
    parser.add_argument('--charset', type=str, default=CHARSET, help='Characters to use')
    parser.add_argument('--hash', type=str, default=TARGET_HASH_HEX, help='Target hash (hex)')
    parser.add_argument('--max-checks', type=int, default=0, help='Limit checks in sequential mode (0 = no limit)')
    parser.add_argument('--no-mp', action='store_true', help='Skip multiprocessing mode')
    args = parser.parse_args()

    length = args.length
    charset = args.charset
    target_hash_hex = args.hash

    cores = n_cpu()
    total_space = len(charset) ** length

    print(f"Detected CPU cores: {cores}")
    print(f"Charset size: {len(charset)}; password length: {length}; total search space = {total_space:,} combinations")
    print(f"Target hash (hex): {target_hash_hex}")
    print()

    max_checks = None if args.max_checks <= 0 else args.max_checks
    print("Starting sequential search...")
    found_seq, checks_seq, elapsed_seq = sequential_search(length, charset, target_hash_hex, max_checks=max_checks)
    if found_seq:
        print(f"Sequential: FOUND password = '{found_seq}' after {checks_seq:,} checks in {elapsed_seq:.3f} s")
    else:
        print(f"Sequential: not found within checked candidates ({checks_seq:,}). Time: {elapsed_seq:.3f} s")
    if elapsed_seq > 0:
        print(f"  Speed (checks/s): {checks_seq/elapsed_seq:.0f}")
    print()

    if args.no_mp:
        print("Skipping multiprocessing mode (flag --no-mp used).")
        return

    print(f"Starting multiprocessing search with {cores} processes...")
    found_mp, checks_mp, elapsed_mp = multiprocessing_search(length, charset, target_hash_hex, cores)
    if found_mp:
        print(f"Multiprocessing: FOUND password = '{found_mp}' (approx checks reported: {checks_mp:,}) in {elapsed_mp:.3f} s")
    else:
        print(f"Multiprocessing: password not found. (approx checks reported: {checks_mp:,}). Time: {elapsed_mp:.3f} s")
    if elapsed_mp > 0:
        print(f"  Approx speed (checks/s): {checks_mp/elapsed_mp:.0f}")


if __name__ == '__main__':
    main()
