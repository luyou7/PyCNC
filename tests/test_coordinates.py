import unittest

from cnc.coordinates import *


class TestCoordinates(unittest.TestCase):
    def setUp(self):
        self.default = Coordinates(96, 102, 150)

    def tearDown(self):
        pass

    def test_constructor(self):
        # constructor rounds values to 10 digits after the point
        self.assertRaises(TypeError, Coordinates)
        c = Coordinates(1.00000000005, 2.00000000004, -3.5000000009)
        self.assertEquals(c.x, 1.0000000001)
        self.assertEquals(c.y, 2.0)
        self.assertEquals(c.z, -3.5000000009)

    def test_zero(self):
        c = Coordinates(0, 0, 0)
        self.assertTrue(c.is_zero())

    def test_aabb(self):
        # aabb - Axis Aligned Bounded Box.
        # original method checks if point belongs aabb.
        p1 = Coordinates(0, 0, 0)
        p2 = Coordinates(2, 2, 2)
        c = Coordinates(1, 1, 1)
        self.assertTrue(c.is_in_aabb(p1, p2))
        self.assertTrue(c.is_in_aabb(p2, p1))
        c = Coordinates(0, 0, 0)
        self.assertTrue(c.is_in_aabb(p1, p2))
        c = Coordinates(2, 2, 2)
        self.assertTrue(c.is_in_aabb(p1, p2))
        c = Coordinates(2, 3, 2)
        self.assertFalse(c.is_in_aabb(p1, p2))
        c = Coordinates(-1, 1, 1)
        self.assertFalse(c.is_in_aabb(p1, p2))
        c = Coordinates(1, 1, 3)
        self.assertFalse(c.is_in_aabb(p1, p2))

    def test_length(self):
        c = Coordinates(-1, 0, 0)
        self.assertEquals(c.length(), 1)
        c = Coordinates(0, 3, -4)
        self.assertEquals(c.length(), 5)
        c = Coordinates(3, 4, 12)
        self.assertEquals(c.length(), 13)

    def test_round(self):
        # round works in another way then Python's round.
        # This round() rounds digits with specified step.
        c = Coordinates(1.5, -1.4, 3.05)
        r = c.round(1)
        self.assertEquals(r.x, 2.0)
        self.assertEquals(r.y, -1.0)
        self.assertEquals(r.z, 3.0)
        r = c.round(0.25)
        self.assertEquals(r.x, 1.5)
        self.assertEquals(r.y, -1.5)
        self.assertEquals(r.z, 3.0)

    def test_max(self):
        self.assertEquals(self.default.find_max(), max(self.default.x,
                                                       self.default.y,
                                                       self.default.z))

    # build-in function overriding tests
    def test_add(self):
        r = self.default + Coordinates(1, 2, 3)
        self.assertEquals(r.x, self.default.x + 1)
        self.assertEquals(r.y, self.default.y + 2)
        self.assertEquals(r.z, self.default.z + 3)

    def test_sub(self):
        r = self.default - Coordinates(1, 2, 3)
        self.assertEquals(r.x, self.default.x - 1)
        self.assertEquals(r.y, self.default.y - 2)
        self.assertEquals(r.z, self.default.z - 3)

    def test_mul(self):
        r = self.default * 2
        self.assertEquals(r.x, self.default.x * 2)
        self.assertEquals(r.y, self.default.y * 2)
        self.assertEquals(r.z, self.default.z * 2)

    def test_div(self):
        r = self.default / 2
        self.assertEquals(r.x, self.default.x / 2)
        self.assertEquals(r.y, self.default.y / 2)
        self.assertEquals(r.z, self.default.z / 2)

    def test_truediv(self):
        r = self.default / 3.0
        self.assertEquals(r.x, self.default.x / 3.0)
        self.assertEquals(r.y, self.default.y / 3.0)
        self.assertEquals(r.z, self.default.z / 3.0)

    def test_eq(self):
        a = Coordinates(self.default.x, self.default.y, self.default.z)
        self.assertTrue(a == self.default)
        a = Coordinates(-self.default.x, self.default.y, self.default.z)
        self.assertFalse(a == self.default)
        a = Coordinates(self.default.x, -self.default.y, self.default.z)
        self.assertFalse(a == self.default)
        a = Coordinates(self.default.x, self.default.y, -self.default.z)
        self.assertFalse(a == self.default)

    def test_str(self):
        self.assertTrue(isinstance(str(self.default), str))

    def test_abs(self):
        c = Coordinates(-1, -2.5, -99)
        r = abs(c)
        self.assertEquals(r.x, 1.0)
        self.assertEquals(r.y, 2.5)
        self.assertEquals(r.z, 99.0)


if __name__ == '__main__':
    unittest.main()