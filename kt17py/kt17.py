from . import _kt17
import numpy as np


class Kt17:
    def __init__(self, rhel, idx):
        """ Initializes KT17 setting model's dynamic parameters

            :param rhel (float): heliocentric distance in astronomical units
            :param idx (float): disturbance index as defined by Anderson et al. (2013)

        """
        self.rhel = rhel
        self.idx = idx
        if type(self.rhel) not in [float]:
            raise TypeError("Heliocentric distance is not a float number")
        if type(self.idx) not in [float]:
            raise TypeError("Disturbance index is not a float number")

        _kt17.kt17_initialize(self.rhel, self.idx)

    def bfield(self, xyz_msm):
        """ Returns the magnetic field components  KT17 setting model's dynamic parameters

            :param xyz_msm: Mercury-centric Solar Magnetospheric coordinates in units of
                            the Mercury radius.
            :return the magnetic field components in Mercury-centric Solar Magnetospheric coordinates

        """
        n = np.shape(xyz_msm)[0]

        x_msm = np.reshape(xyz_msm[:, 0:1], (n,))
        y_msm = np.reshape(xyz_msm[:, 1:2], (n,))
        z_msm = np.reshape(xyz_msm[:, 2:], (n,))

        b_msm = np.reshape(_kt17.kt17_bfield(x_msm, y_msm, z_msm), (n, 3))
        return b_msm