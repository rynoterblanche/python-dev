from unittest import TestCase

import numpy
from numpy.testing import assert_array_equal


class TestBroadcasting(TestCase):
    """
    Broadcasting rules:
        1. One dimension is one
        2. Both Dimensions are equal
    """

    def test_broadcasting_with_scalar(self):
        arr = numpy.arange(6)

        result = arr * 2

        assert_array_equal(result, [0., 2., 4., 6., 8., 10.])

    def test_broadcasting_with_one_array_having_one_dimension(self):
        arr_a = numpy.arange(7).reshape(1, 7)
        arr_b = numpy.arange(49).reshape(7, 7)

        self.assertEqual((7, 7), (arr_a * arr_b).shape)

    def test_broadcasting_with_both_arrays_having_same_dimensions(self):
        arr_a = numpy.arange(49).reshape(7, 7)
        arr_b = numpy.zeros(49).reshape(7, 7) + 2

        self.assertEqual((7, 7), (arr_a * arr_b).shape)

    def test_broadcasting_caveats(self):
        arr_a = numpy.array([1, 2, 3, 4])
        arr_b = numpy.arange(20).reshape(4, 5)

        # This fails because arr_a is one dimensional, while arr_b is not:
        with self.assertRaises(Exception) as ex:
            arr_a + arr_b
            self.assertIsInstance(ex, ValueError)

        # Reshape arr_a to allow broadcasting:
        result = arr_a.reshape(4, 1) + arr_b
        self.assertEqual((4, 5), result.shape)
