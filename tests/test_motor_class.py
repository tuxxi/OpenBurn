import unittest

from openburn.util.motorclass import get_motor_class


class MotorClassTest(unittest.TestCase):
    def test_class(self):
        des, _ = get_motor_class(2500)
        self.assertEqual(des, 'K')

        des, _ = get_motor_class(1281)
        self.assertEqual(des, 'K')

        des, _ = get_motor_class(1279)
        self.assertEqual(des, 'J')

        des, _ = get_motor_class(350)
        self.assertEqual(des, 'I')

    def test_percent(self):
        _, percent = get_motor_class(2500)
        self.assertAlmostEqual(percent, 95.3125)

        _, percent = get_motor_class(1281)
        self.assertAlmostEqual(percent, 0.078125)

        _, percent = get_motor_class(1279)
        self.assertAlmostEqual(percent, 99.84375)

        _, percent = get_motor_class(350)
        self.assertAlmostEqual(percent, 9.375)

    def test_special(self):
        des, percent = get_motor_class(2)
        self.assertEqual(des, 'A')
        self.assertAlmostEqual(percent, 80)

        des, percent = get_motor_class(9.23)
        self.assertEqual(des, 'C')
        self.assertAlmostEqual(percent, 92.3)

        des, percent = get_motor_class(3.55)
        self.assertEqual(des, 'B')
        self.assertAlmostEqual(percent, 71)

