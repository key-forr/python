import os
import time
import itertools
import hashlib
from multiprocessing import Process, Pool, Queue, Value, Lock
import multiprocessing as mp

def get_cpu_count():
    return os.cpu_count()

def generate_blake2b_hash(password):
    return hashlib.blake2b(password.encode('utf-8')).hexdigest()

def single_process_crack(charset, password_length, target_hash):
    print("Початок підбору пароля (один процес)...")
    start_time = time.time()
    
    attempts = 0
    
    for password_tuple in itertools.product(charset, repeat=password_length):
        password = ''.join(password_tuple)
        attempts += 1
        
        password_hash = generate_blake2b_hash(password)
        
        if attempts % 100000 == 0:
            print(f"Спроба #{attempts}: {password}")
        
        if password_hash == target_hash:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Пароль знайдено: {password}")
            print(f"Час виконання: {elapsed_time:.2f} секунд")
            print(f"Кількість спроб: {attempts}")
            return password, elapsed_time
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Пароль не знайдено")
    print(f"Час виконання: {elapsed_time:.2f} секунд")
    print(f"Загальна кількість спроб: {attempts}")
    return None, elapsed_time

def worker_process(process_id, charset, password_length, target_hash, start_idx, step, result_queue, found_flag):
    attempts = 0
    
    total_combinations = len(charset) ** password_length
    
    for i in range(start_idx, total_combinations, step):
        if found_flag.value == 1:
            break
            
        password = ""
        temp_i = i
        for _ in range(password_length):
            password = charset[temp_i % len(charset)] + password
            temp_i //= len(charset)
        
        attempts += 1
        
        password_hash = generate_blake2b_hash(password)
        
        if attempts % 50000 == 0:
            print(f"Процес {process_id}: спроба #{attempts}: {password}")
        
        if password_hash == target_hash:
            found_flag.value = 1
            result_queue.put((process_id, password, attempts))
            print(f"Процес {process_id} знайшов пароль: {password}")
            return
    
    result_queue.put((process_id, None, attempts))

def multiprocess_crack(charset, password_length, target_hash, num_processes):
    print(f"Початок підбору пароля ({num_processes} процесів)...")
    start_time = time.time()
    
    result_queue = Queue()
    found_flag = Value('i', 0)
    
    processes = []
    for i in range(num_processes):
        p = Process(target=worker_process, args=(i, charset, password_length, 
                                               target_hash, i, num_processes, 
                                               result_queue, found_flag))
        processes.append(p)
        p.start()
    
    found_password = None
    total_attempts = 0
    completed_processes = 0
    
    while completed_processes < num_processes:
        if not result_queue.empty():
            process_id, password, attempts = result_queue.get()
            total_attempts += attempts
            completed_processes += 1
            
            if password is not None and found_password is None:
                found_password = password
    
    for p in processes:
        p.join()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    if found_password:
        print(f"Пароль знайдено: {found_password}")
    else:
        print("Пароль не знайдено")
    
    print(f"Час виконання: {elapsed_time:.2f} секунд")
    print(f"Загальна кількість спроб: {total_attempts}")
    
    return found_password, elapsed_time

def verify_password(password, target_hash):
    password_hash = generate_blake2b_hash(password)
    return password_hash == target_hash

def main():
    uppChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowChar = "abcdefghijklmnopqrstuvwxyz"
    numChar = "0123456789"
    spcChar = "!@#$%^&*_-"
    
    charset = lowChar + numChar + spcChar
    password_length = 6
    target_hash = "6f0874bd7ba418106ac15555ea927aef34bc05c8ba92cd2e4c3065e7751ccc125fd88f19eec18f007e9f033c8dd2749edf573ac8aeec47d073f5832553fcea9c"
    
    print("=" * 60)
    print("ЛАБОРАТОРНА РОБОТА: ПІДБІР ПАРОЛЯ")
    print("=" * 60)
    
    n_cpu = get_cpu_count()
    print(f"Кількість процесорних ядер (n_cpu): {n_cpu}")
    print()
    
    print(f"Параметри пошуку:")
    print(f"Довжина пароля: {password_length} символів")
    print(f"Набір символів: {charset}")
    print(f"Кількість символів у наборі: {len(charset)}")
    print(f"Загальна кількість можливих комбінацій: {len(charset)**password_length:,}")
    print(f"Цільовий хеш: {target_hash}")
    print(f"Хеш функція: blake2b")
    print()
    
    correct_password = "*e5-qp"
    print("=" * 60)
    print("ПЕРЕВІРКА ВІДПОВІДІ")
    print("=" * 60)
    
    if verify_password(correct_password, target_hash):
        print(f"✓ ПРАВИЛЬНИЙ ПАРОЛЬ: {correct_password}")
        print(f"✓ Хеш співпадає: {generate_blake2b_hash(correct_password)}")
    else:
        print(f"✗ Пароль не співпадає")
    print()
    
    """
    print("=" * 60)
    print("2.1. ПІДБІР БЕЗ МУЛЬТИПРОЦЕСОРНОСТІ")
    print("=" * 60)
    
    single_password, single_time = single_process_crack(charset, password_length, target_hash)
    print()
    
    print("=" * 60)
    print("2.2. ПІДБІР З МУЛЬТИПРОЦЕСОРНІСТЮ")
    print("=" * 60)
    
    multi_password, multi_time = multiprocess_crack(charset, password_length, target_hash, n_cpu)
    print()
    
    print("=" * 60)
    print("ПОРІВНЯННЯ РЕЗУЛЬТАТІВ")
    print("=" * 60)
    print(f"Один процес:")
    print(f"  Знайдений пароль: {single_password}")
    print(f"  Час виконання: {single_time:.2f} секунд")
    print()
    print(f"{n_cpu} процесів:")
    print(f"  Знайдений пароль: {multi_password}")
    print(f"  Час виконання: {multi_time:.2f} секунд")
    
    if single_time > 0 and multi_time > 0:
        speedup = single_time / multi_time
        print(f"  Прискорення: {speedup:.2f}x")
    print()
    """

if __name__ == "__main__":
    main()