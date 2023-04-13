from unittest import TestCase

import numpy
from numpy.ma.testutils import assert_array_equal


class TestSlicing(TestCase):

    def test_update_to_slice_does_propagate_to_array(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr = numpy.array(data)

        # slice entire second row
        slice_a = arr[2]
        slice_a[1] = 1

        self.assertEqual(1, arr[2, 1])

    def test_update_to_copied_slice_does_not_propagate_to_array(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr = numpy.array(data)

        # slice entire second row of copied array
        slice_a = numpy.copy(arr)[2]
        slice_a[1] = 1

        self.assertEqual(1, slice_a[1])
        self.assertEqual(8, arr[2, 1])

    def test_partial_slice(self):
        data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        arr = numpy.array(data)

        # slice from second row, the second to third columns
        slice_a = arr[1, 1:4]

        assert_array_equal([7, 8, 9], slice_a)

    def test_partial_slice_by_axis(self):
        data = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        arr = numpy.array(data)

        # slice from second to second last row, the first column
        slice_a = arr[1:-1, 1]

        assert_array_equal([4, 6, 8], slice_a)

    def test_slice_by_stride(self):
        data = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
        arr = numpy.array(data)

        # slice from first to last row, every two rows, the second column
        assert_array_equal([2, 6, 10], arr[::2, 1])

        # slice from first to last row, every three rows, the first column
        assert_array_equal([1, 7], arr[::3, 0])

        # slice from first to last row, every two rows, every two columns (for every dimension)
        assert_array_equal([[1], [5], [9]], arr[::2, ::2])
