import unittest

from openburn.core.propellant import SimplePropellant
from openburn.core.grain import CylindricalCoreGrain
from openburn.core.nozzle import ConicalNozzle
from openburn.core.motor import OpenBurnMotor


class InternalBallisticsTest(unittest.TestCase):
    def setUp(self):
        """Set up the test data"""
        self.propellant = SimplePropellant("68/10", 0.0341, 0.2249, 4706, 0.058, 1.226)
        # using a list comprehension to create four unique grain objects
        self.grains = [CylindricalCoreGrain(diameter=2, length=4, core_diameter=1, burning_faces=2,
                                            propellant=self.propellant)
                       for _ in range(0, 4)]
        self.nozzle = ConicalNozzle(throat=0.5, exit=2, half_angle=15, throat_len=0.25)
        self.motor = OpenBurnMotor()
        self.motor.set_grains(self.grains)
        self.motor.set_nozzle(self.nozzle)

    def test_json_in(self):
        out = self.motor.to_json()
        uuid_out = self.motor.uuid

        in_ = self.motor.from_json(out)
        uuid_in = in_.uuid
        self.assertIsInstance(in_, OpenBurnMotor)
        self.assertNotEqual(uuid_out, uuid_in)
