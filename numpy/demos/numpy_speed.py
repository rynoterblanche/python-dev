import random
from timeit import timeit

import numpy


def multiply(list_arr, scalar):
    new = []
    for val in list_arr:
        new.append(scalar * val)


def demo_list_vs_np_array():
    test_range = 1000

    list_arr = [random.random() for _ in range(test_range)]
    numpy_arr = numpy.random.rand(test_range)

    list_result = timeit(lambda: multiply(list_arr, 2))
    print(f"List Result: {list_result}")

    np_arr_result = timeit(lambda: numpy_arr * 2)
    print(f"Numpy Array Result: {np_arr_result}")


if __name__ == '__main__':
    demo_list_vs_np_array()
