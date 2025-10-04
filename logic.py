import numpy as np

def solve_slae():
    A = np.array([[2, 3, 7],
                  [11, 4, 9],
                  [17, 1, -3]])
    b = np.array([-2, 13, 6])
    x = np.linalg.solve(A, b)
    return x

def create_matrix():
    return np.array([[15, 14, 13, 12],
                     [11, 10, 9, 8],
                     [7, 6, 5, 4],
                     [3, 2, 1, 0]], dtype=np.uint64)

def every_third_row(matrix):
    return matrix[::3]

def elements_less_than_2_in_even_rows(matrix):
    return matrix[::2][matrix[::2] < 2]

def every_second_element(matrix):
    return matrix.flatten()[::2]

def has_zero_rows(matrix):
    return np.any(matrix.sum(axis=1) == 0)

def replace_max_with_min(matrix):
    m_copy = matrix.copy()
    m_copy[m_copy == m_copy.max()] = m_copy.min()
    return m_copy

def even_elements(matrix):
    evens = matrix[matrix % 2 == 0]
    return evens, len(evens)

def min_per_column(matrix):
    return matrix.min(axis=0)

def mean_per_row(matrix):
    return matrix.mean(axis=1)
