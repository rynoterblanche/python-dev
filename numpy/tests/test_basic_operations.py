from unittest import TestCase

import numpy
from numpy import NaN
from numpy.ma.testutils import assert_array_equal


class TestOperations(TestCase):

    def test_basic_multiply_operation(self):
        arr_a = numpy.arange(12).reshape(3, 4)
        arr_b = numpy.zeros(12).reshape(3, 4) + -1

        assert_array_equal([[-0., -1., -2., -3.],
                            [-4., -5., -6., -7.],
                            [-8., -9., -10., -11.]], arr_a * arr_b)

    def test_basic_sum(self):
        arr = numpy.zeros(12).reshape(3, 4) + 2

        self.assertEqual(24, numpy.sum(arr))
        # or
        self.assertEqual(24, arr.sum())

    def test_basic_mean(self):
        arr = numpy.zeros(12).reshape(3, 4) + 3

        self.assertEqual(3, arr.mean())

    def test_basic_sum_operation_with_NaN(self):
        data = [[1, NaN, 3], [1, NaN, 3]]

        arr = numpy.array(data)
        self.assertTrue(numpy.isnan(arr.sum()))

        cleaned_arr = arr[~numpy.isnan(arr)]
        self.assertEqual(8, cleaned_arr.sum())

    def test_sum_operation_on_rows_that_contain_no_NaNs(self):
        data = [[1, NaN, 1], [2, 2, 2], [3, NaN, 3], [4, 4, 4]]
        arr = numpy.array(data)

        # all rows that are fully numerical (contains no NaNs)
        cleaned_arr = arr[~numpy.isnan(arr).any(axis=1)]

        self.assertEqual(18, cleaned_arr.sum())

    def test_sum_operation_over_rows(self):
        data = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
        arr = numpy.array(data)

        # axis = 0 means operation happens over rows
        assert_array_equal([10, 10, 10], arr.sum(axis=0))

    def test_sum_operation_over_columns(self):
        data = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
        arr = numpy.array(data)

        # axis = 1 means operation happens over columns
        assert_array_equal([3, 6, 9, 12], arr.sum(axis=1))

    def test_elementwise_multiplication(self):
        arr_a = numpy.arange(9).reshape(3, 3)
        arr_b = numpy.arange(9).reshape(3, 3)

        assert_array_equal([[0, 1, 4],
                            [9, 16, 25],
                            [36, 49, 64]], arr_a * arr_b)

    def test_matrix_multiplication(self):
        arr_a = numpy.arange(9).reshape(3, 3)
        arr_b = numpy.arange(9).reshape(3, 3)

        assert_array_equal([[15, 18, 21],
                            [42, 54, 66],
                            [69, 90, 111]], arr_a.dot(arr_b))
