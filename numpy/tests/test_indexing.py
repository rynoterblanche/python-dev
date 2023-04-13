from unittest import TestCase

import numpy
from numpy import NaN
from numpy.testing import assert_array_equal


class TestIndexing(TestCase):

    def test_index_with_tuple(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr = numpy.array(data)

        indexer = (1, 2)
        result = arr[indexer]

        self.assertEqual(6, result)

    def test_index_with_array(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr = numpy.array(data)

        # This indexer will trigger advanced indexing in a numpy array
        indexer = numpy.array([1, 2])

        assert_array_equal([[4, 5, 6], [7, 8, 9]], arr[indexer])

        # similarly:
        assert_array_equal(numpy.array([arr[1], arr[2]]), arr[indexer])

    def test_index_with_where_clause(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr = numpy.array(data)

        # index using the numpy where clause
        indexer = numpy.where(arr % 2 == 0)

        assert_array_equal([2, 4, 6, 8], arr[indexer])

    def test_index_with_boolean_array(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr = numpy.array(data)

        # index with a direct boolean condition
        indexer = (arr % 2 != 0) & (arr > 1)

        assert_array_equal([3, 5, 7, 9], arr[indexer])

    def test_delete_by_index(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr = numpy.array(data)

        result = numpy.delete(arr, [1, 3])

        assert_array_equal([1, 3, 5, 6, 7, 8, 9], result)

    def test_index_with_boolean_for_NaN_values(self):
        data = [[1, NaN, 3], [4, NaN, 6]]
        arr = numpy.array(data)

        indexer = numpy.isnan(arr)
        arr[indexer] = 0

        assert_array_equal([[1, 0, 3], [4, 0, 6]], arr)

    def test_index_and_slice_and_stride(self):
        arr = numpy.arange(50).reshape(5, 10)
        bool_mask = (15 < arr) & (arr < 35)

        assert_array_equal([[22, 24, 26]], arr[bool_mask[:, 5], 2:8:2])
