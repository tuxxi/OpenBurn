import unittest

from openburn.core.internalballistics import SimSettings, InternalBallisticsSim as sim
from openburn.core.propellant import SimplePropellant
from openburn.core.grain import CylindricalCoreGrain
from openburn.core.nozzle import ConicalNozzle
from openburn.core.motor import OpenBurnMotor


class InternalBallisticsTest(unittest.TestCase):
    def setUp(self):
        """Set up the test data"""
        self.settings = SimSettings(timestep=0.01)
        self.propellant = SimplePropellant("Test Propellant", 0.01, 0.4, 5000, 0.06)
        # using a list comprehension to create four unique grain objects
        self.grains = [CylindricalCoreGrain(diameter=2, length=4, core_diameter=1, burning_faces=2,
                                            propellant=self.propellant)
                       for _ in range(0, 4)]
        self.nozzle = ConicalNozzle(throat=0.5, exit=2, half_angle=15, throat_len=0.25)
        self.motor = OpenBurnMotor()
        self.motor.set_grains(self.grains)
        self.motor.set_nozzle(self.nozzle)

    def test_basic_sim(self):
        results = sim.run_sim(self.motor, self.settings)
        print("\nResults:")
        print("Kn Range: ", results.get_kn_range())
        print("Burn Time: (s)", results.get_burn_time())
        print("Max Thrust: (lbs)", results.get_max_thrust())
        print("Max Pressure: (psi)", results.get_max_presure())
        print("Avg Thrust: (lbs)", results.get_avg_thrust())
        print("Average Isp: (s)", results.get_avg_isp())
        print("Total Impulse (lb-sec)", results.get_total_impulse())
