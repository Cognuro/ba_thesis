from unittest import TestCase
from tests import test_transformation as trans
import numpy as np

places = 2


class TestImpEllipse(TestCase):
    def test_construct_by_param(self):
        from ellipse_unprojection import ImpEllipse
        e_param = ImpEllipse.construct_by_param(-1.53333, 1.1333, 3.218, 2.49266, 135)
        e_imp = ImpEllipse(1, 0.5, 1, 2.5, -1.5, -5)
        self.assertAlmostEqual(e_param.a_xx, e_imp.a_xx, places)
        self.assertAlmostEqual(e_param.h_xy, e_imp.h_xy, places)
        self.assertAlmostEqual(e_param.b_yy, e_imp.b_yy, places)
        self.assertAlmostEqual(e_param.g_x, e_imp.g_x, places)
        self.assertAlmostEqual(e_param.f_y, e_imp.f_y, places)
        self.assertAlmostEqual(e_param.d, e_imp.d, places)


class TestUnprojection(TestCase):
    from ellipse_unprojection import ImpEllipse
    from ellipse_unprojection import Double3DCircle

    # Results from Safaee-Rad p.632
    e_imp = ImpEllipse(204.024, -102.452, 225.000, -127.567, -177.45, 66.976)
    double3d_from = Double3DCircle.construct_by_ImpEllipse(e_imp, 4, focal_length=1)

    def test_construct_by_ImpEllipse(self, double3d_from = double3d_from):
        pos_true = np.array([11.830, 13.660, 27.811])
        orientation_true = np.array([-0.5, 0, -0.866025])
        decimal=2
        np.testing.assert_almost_equal(double3d_from.position, pos_true, decimal=decimal)
        np.testing.assert_almost_equal(double3d_from.pos_orientation, orientation_true, decimal=decimal)

    def test_orientation_projection(self, double3d_from = double3d_from):
        from eye_tracking import ProjectedPupil
        ProjectedPupil.construct_by_Double3DCircle(double3d_from, focal_length=1)

