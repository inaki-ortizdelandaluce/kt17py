from kt17py.kt17 import *
import unittest


class TestKt17(unittest.TestCase):

    def test_type_error_constructor(self):
        self.assertRaises(TypeError, Kt17, "Wrong", "Values")

    '''
    def test_type_error_bfield(self):
        model = Kt17(0.39, 0.50)
        xyz_msm = np.array([-2.0, 0.0, 5.0])
        self.assertRaises(TypeError, model.bfield, xyz_msm)
    '''


if __name__ == '__main__':
    unittest.main()