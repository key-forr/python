import numpy as np

A = np.array([[2, 3, 7],
              [11, 4, 9],
              [17, 1, -3]])
b = np.array([-2, 13, 6])
x = np.linalg.solve(A, b)
print("Розв'язок СЛАР:", x)

matrix = np.array([[15, 14, 13, 12],
                   [11, 10, 9, 8],
                   [7, 6, 5, 4],
                   [3, 2, 1, 0]], dtype=np.uint64)
print("\nМатриця:\n", matrix)

print("\nКожен третій рядок:\n", matrix[::3])

print("\nЕлементи < 2 у парних рядках:", matrix[::2][matrix[::2] < 2])

print("\nЕлементи через один:", matrix.flatten()[::2])

print("\nНульові рядки:", np.any(matrix.sum(axis=1) == 0))

m_copy = matrix.copy()
m_copy[m_copy == m_copy.max()] = m_copy.min()
print("\nМатриця після заміни max на min:\n", m_copy)

evens = matrix[matrix % 2 == 0]
print("\nКількість парних:", len(evens))
print("Парні елементи:", evens)

print("\nМінімальні по стовпцях:", matrix.min(axis=0))

print("\nСередні по рядках:", matrix.mean(axis=1))
