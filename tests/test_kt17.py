import unittest
import sys
import numpy as np

# since kt17py contains Fortran files that need to be compiled before use
# the tests are run against the version of kt17py (if any) found on current PYTHONPATH.
# For further improvements check Testing builds section on https://numpy.org/devdocs/dev/development_environment.html
sys.path.pop(0)

from kt17py.kt17 import *


class TestKt17(unittest.TestCase):

    def test_type_error_constructor(self):
        self.assertRaises(TypeError, Kt17, "Wrong", "Values")

    def test_type_error_bfield(self):
        k = Kt17(0.39, 0.50)
        xyz_msm = np.array([-2.0, 0.0, 5.0])
        self.assertRaises(TypeError, k.bfield, xyz_msm)

    def test_bfield(self):
        k = Kt17(0.39, 50.0)
        # test a few magnetic values to discard any issue with the input, output numpy arrays
        xyz_msm = np.array([[-2.25, 0., 0.], [-2.30, -2.30, 0.], [-4.0, 0.05, 0.5]])
        b_actual = k.bfield(xyz_msm)
        b_expected = np.array([[0., 0., 8.0256237], [0., 0., 21.2404669], [28.4791596, -0.1447476, 3.3399097]])
        try:
            np.testing.assert_array_almost_equal(b_actual, b_expected)
            res = True
        except AssertionError as err:
            res = False
            print(err)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
