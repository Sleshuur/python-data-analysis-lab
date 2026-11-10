# cython: language_level=3
"""Сумма квадратов: типизированный цикл Cython."""

def sum_squares_cython(const double[::1] values):
    cdef Py_ssize_t i
    cdef double total = 0.0
    for i in range(values.shape[0]):
        total += values[i] * values[i]
    return total
