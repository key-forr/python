import os
import time
import hashlib
from multiprocessing import Process, Queue, Value

def get_cpu_count():
    return os.cpu_count()

def check_password_hash(password, target_hash):
    return hashlib.blake2s(password.encode('utf-8')).hexdigest() == target_hash

def generate_blake2s_hash(password):
    return hashlib.blake2s(password.encode('utf-8')).hexdigest()

def generate_password(index, charset, password_length):
    password = ""
    temp_i = index
    for _ in range(password_length):
        password = charset[temp_i % len(charset)] + password
        temp_i //= len(charset)
    return password

def single_process_crack(charset, password_length, target_hash):
    start_time = time.time()
    attempts = 0
    total_combinations = len(charset) ** password_length
    
    for i in range(total_combinations):
        password = generate_password(i, charset, password_length)
        attempts += 1
        password_hash = generate_blake2s_hash(password)
        
        if password_hash == target_hash:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return {
                'found': True,
                'password': password,
                'attempts': attempts,
                'time': elapsed_time,
                'speed': attempts / elapsed_time
            }
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    return {
        'found': False,
        'password': None,
        'attempts': attempts,
        'time': elapsed_time,
        'speed': attempts / elapsed_time
    }

def worker_process(charset, password_length, target_hash, start_idx, step, result_queue, found_flag):
    attempts = 0
    total_combinations = len(charset) ** password_length
    
    for i in range(start_idx, total_combinations, step):
        if found_flag.value == 1:
            break
            
        password = generate_password(i, charset, password_length)
        attempts += 1
        password_hash = generate_blake2s_hash(password)
        
        if password_hash == target_hash:
            found_flag.value = 1
            result_queue.put((password, attempts))
            return
    
    result_queue.put((None, attempts))

def multiprocess_crack(charset, password_length, target_hash, num_processes):
    start_time = time.time()

    result_queue = Queue()
    found_flag = Value('i', 0)

    processes = []
    for i in range(num_processes):
        p = Process(target=worker_process, args=(charset, password_length,
                                                 target_hash, i, num_processes,
                                                 result_queue, found_flag))
        processes.append(p)
        p.start()

    found_password = None
    total_attempts = 0
    completed_processes = 0

    while completed_processes < num_processes:
        password, attempts = result_queue.get()  
        total_attempts += attempts
        completed_processes += 1

        if password is not None and found_password is None:
            found_password = password

    for p in processes:
        p.join()

    end_time = time.time()
    elapsed_time = end_time - start_time

    return {
        'found': found_password is not None,
        'password': found_password,
        'attempts': total_attempts,
        'time': elapsed_time,
        'speed': total_attempts / elapsed_time if elapsed_time > 0 else 0,
        'processes': num_processes
    }


def display_menu(charset, password_length):
    print("=== ПІДБІР ПАРОЛЯ ===")
    print(f"Довжина пароля: {password_length}")
    print(f"Набір символів: {charset}")
    print(f"Всього комбінацій: {len(charset) ** password_length}")
    print()
    print("Виберіть режим підбору:")
    print("1. Один процес")
    print("2. Мультипроцесорність")

def display_results(result):
    if result['found']:
        print(f"\nПароль знайдено: {result['password']}")
    else:
        print(f"\nПароль не знайдено")
    
    print(f"Час виконання: {result['time']:.2f} секунд")
    print(f"Кількість спроб: {result['attempts']}")
    print(f"Швидкість: {result['speed']:.0f} паролів/сек")
    
    if 'processes' in result:
        print(f"Використано процесів: {result['processes']}")

def main():
    lowChar = "abcdefghijklmnopqrstuvwxyz"
    spcChar = "!@#$%^&*_-"

    #^cx$%l
    
    charset = lowChar + spcChar
    password_length = 6
    target_hash = "713417394e2b74aee7fa54d09375b0c78d288a90eba27a560cfc698c5b54886c"


    if check_password_hash("^cx$%l", target_hash):
         print("Хеш відповідає паролю '^cx$%l'")
    else:
         print("Хеш не відповідає паролю '^cx$%l'")
    
    display_menu(charset, password_length)
    choice = input("\nВведіть номер (1 або 2): ").strip()
    
    print("\nПідбір пароля розпочато...")
    
    if choice == "1":
        result = single_process_crack(charset, password_length, target_hash)
    elif choice == "2":
        num_processes = get_cpu_count()
        result = multiprocess_crack(charset, password_length, target_hash, num_processes)
    else:
        print("Невірний вибір. Використовується режим з одним процесом.")
        result = single_process_crack(charset, password_length, target_hash)
    
    display_results(result)

if __name__ == "__main__":
    main()