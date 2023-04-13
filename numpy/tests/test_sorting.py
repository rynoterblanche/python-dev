from unittest import TestCase

import numpy
from numpy.ma.testutils import assert_array_equal


class TestSorting(TestCase):
    def test_in_place_sort(self):
        arr = numpy.array([5, 4, 3, 2, 1])

        # sort array in place
        arr.sort()

        assert_array_equal(arr, [1, 2, 3, 4, 5])

    def test_copy_and_sort(self):
        arr = numpy.array([5, 4, 3, 2, 1])

        # create copy and sort
        sorted_copy = numpy.sort(arr)

        assert_array_equal(arr, [5, 4, 3, 2, 1])
        assert_array_equal(sorted_copy, [1, 2, 3, 4, 5])

    def test_sort_over_rows(self):
        data = [[3, 2, 1], [4, 5, 6]]
        arr = numpy.array(data)

        arr.sort()
        assert_array_equal(arr, [[1, 2, 3],
                                 [4, 5, 6]])

    def test_sort_over_columns(self):
        data = [[3, 6, 9],
                [2, 5, 8],
                [1, 4, 7]]
        arr = numpy.array(data)

        arr.sort(axis=0)
        assert_array_equal(arr, [[1, 4, 7],
                                 [2, 5, 8],
                                 [3, 6, 9]])

    def test_argsort(self):
        arr = numpy.array([5, 4, 3, 2, 1])
        result = numpy.argsort(arr)

        assert_array_equal(result, [4, 3, 2, 1, 0])
        assert_array_equal(arr[result], [1, 2, 3, 4, 5])
