import numpy as np

print("=" * 80)
print("ЗАВДАННЯ 1: Створення матриці 4х4 з типом uint64 та виведення інформації")
print("=" * 80)

# Створення матриці 4х4 з типом uint64
matrix = np.array([
    [15, 14, 13, 12],
    [11, 10, 9, 8],
    [7, 6, 5, 4],
    [3, 2, 1, 0]
], dtype=np.uint64)

print("\nМатриця:")
print(matrix)
print(f"\nРозмірність: {matrix.shape}")
print(f"Тип елементів: {matrix.dtype}")
print(f"Розмір елементу в байтах: {matrix.itemsize}")
print(f"Розмір масиву в байтах: {matrix.nbytes}")

print("\n" + "=" * 80)
print("ЗАВДАННЯ 2: Кожен третій рядок")
print("=" * 80)
every_third_row = matrix[::3]
print("\nКожен третій рядок (індекси 0, 3, ...):")
print(every_third_row)

print("\n" + "=" * 80)
print("ЗАВДАННЯ 3: Елементи в парних рядках менші 2")
print("=" * 80)
# Парні рядки мають індекси 0, 2, 4... (рахуємо з 0)
even_rows = matrix[::2]
print("\nПарні рядки (індекси 0, 2):")
print(even_rows)
elements_less_than_2 = even_rows[even_rows < 2]
print(f"\nЕлементи в парних рядках менші 2:")
print(elements_less_than_2)

print("\n" + "=" * 80)
print("ЗАВДАННЯ 4: Всі елементи через один починаючи з першого")
print("=" * 80)
# Перетворюємо матрицю в одновимірний масив і беремо кожен другий елемент
flat_matrix = matrix.flatten()
every_other_element = flat_matrix[::2]
print("\nВсі елементи через один починаючи з першого:")
print(every_other_element)

print("\n" + "=" * 80)
print("ЗАВДАННЯ 5: Чи є в матриці нульові рядки")
print("=" * 80)
# Рядок є нульовим, якщо всі його елементи дорівнюють 0
zero_rows = np.all(matrix == 0, axis=1)
print("\nПеревірка кожного рядка на нульовість:")
for i, is_zero in enumerate(zero_rows):
    print(f"Рядок {i}: {'нульовий' if is_zero else 'не нульовий'}")
has_zero_rows = np.any(zero_rows)
print(f"\nЧи є в матриці нульові рядки: {'Так' if has_zero_rows else 'Ні'}")

print("\n" + "=" * 80)
print("ЗАВДАННЯ 6: Замінити максимальний елемент мінімальним")
print("=" * 80)
matrix_copy = matrix.copy()
max_value = matrix_copy.max()
min_value = matrix_copy.min()
print(f"\nМаксимальний елемент: {max_value}")
print(f"Мінімальний елемент: {min_value}")
print("\nМатриця до заміни:")
print(matrix_copy)
# Замінюємо всі максимальні елементи на мінімальне значення
matrix_copy[matrix_copy == max_value] = min_value
print("\nМатриця після заміни:")
print(matrix_copy)

print("\n" + "=" * 80)
print("ЗАВДАННЯ 7: Підрахувати кількість парних елементів у матриці")
print("=" * 80)
even_elements = matrix[matrix % 2 == 0]
count_even = len(even_elements)
print(f"\nПарні елементи: {even_elements}")
print(f"Кількість парних елементів: {count_even}")

print("\n" + "=" * 80)
print("ЗАВДАННЯ 8: Мінімальні значення по стовбцях")
print("=" * 80)
min_by_columns = matrix.min(axis=0)
print("\nМінімальні значення по стовбцях:")
for i, min_val in enumerate(min_by_columns):
    print(f"Стовбець {i}: {min_val}")
print(f"\nМасив мінімальних значень: {min_by_columns}")

print("\n" + "=" * 80)
print("ЗАВДАННЯ 9: Середні значення по рядках")
print("=" * 80)
mean_by_rows = matrix.mean(axis=1)
print("\nСередні значення по рядках:")
for i, mean_val in enumerate(mean_by_rows):
    print(f"Рядок {i}: {mean_val:.2f}")
print(f"\nМасив середніх значень: {mean_by_rows}")

print("\n" + "=" * 80)
print("ЗАВЕРШЕННЯ РОБОТИ ПРОГРАМИ")
print("=" * 80)