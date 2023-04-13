from unittest import TestCase

import numpy
from numpy.ma.testutils import assert_array_equal


class TestSearch(TestCase):

    def test_search_one_dimension(self):
        data = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        arr = numpy.array(data)

        index = numpy.where(arr == 2)
        assert_array_equal(arr[index], [2, 2, 2])

    def test_search_multiple_dimensions(self):
        data = [[1, 2, 3],
                [1, 2, 3],
                [1, 2, 3]]
        arr = numpy.array(data)

        index = numpy.where(arr > 1)
        assert_array_equal(arr[index], [2, 3, 2, 3, 2, 3])

    def test_search_multiple_dimensions_and_keep_structure(self):
        data = [[1, 2, 3],
                [1, 2, 3],
                [1, 2, 3]]
        arr = numpy.array(data)

        result = numpy.where(arr > 1, arr, 0)
        assert_array_equal(result, [[0, 2, 3],
                                    [0, 2, 3],
                                    [0, 2, 3]])

    def test_get_max_without_sort(self):
        arr = numpy.array([3, 4, 5, 2, 1])
        max_index = numpy.argmax(arr)

        self.assertEqual(2, max_index)
        self.assertEqual(5, arr[max_index])
