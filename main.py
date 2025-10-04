from logic import *

def print_task(num, desc, matrix=None, result=None):
    print("=" * 70)
    print(f"ЗАВДАННЯ {num}: {desc}")
    print("=" * 70)
    if matrix is not None:
        print(f"Матриця:\n{matrix}")
    if result is not None:
        print(f"Результат:\n{result}")
    print()

def main():
    matrix = create_matrix()

    # 1
    print_task(1, "Тип: uint64, матриця 4x4", matrix=matrix)

    # 2
    print_task(2, "Кожен третій рядок", matrix=matrix, result=every_third_row(matrix))

    # 3
    print_task(3, "Елементи < 2 у парних рядках", matrix=matrix,
               result=elements_less_than_2_in_even_rows(matrix))

    # 4
    print_task(4, "Елементи через один починаючи з першого", matrix=matrix,
               result=every_second_element(matrix))

    # 5
    print_task(5, "Чи є в матриці нульові рядки", matrix=matrix,
               result=has_zero_rows(matrix))

    # 6
    print_task(6, "Замінити максимальний елемент мінімальним", matrix=matrix,
               result=replace_max_with_min(matrix))

    # 7
    evens, count = even_elements(matrix)
    print_task(7, "Підрахувати кількість парних елементів", matrix=matrix,
               result=f"Кількість: {count}, Елементи: {evens}")

    # 8
    print_task(8, "Мінімальні значення по стовпцях", matrix=matrix,
               result=min_per_column(matrix))

    # 9
    print_task(9, "Середні значення по рядках", matrix=matrix,
               result=mean_per_row(matrix))

    # 10
    x = solve_slae()
    print_task(10, "Розв’язати систему лінійних рівнянь", result=x)

if __name__ == "__main__":
    main()
