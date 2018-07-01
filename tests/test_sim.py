import unittest

from openburn.core.internalballistics import SimSettings, InternalBallisticsSim as sim
from openburn.core.propellant import SimplePropellant
from openburn.core.grain import CylindricalCoreGrain
from openburn.core.nozzle import ConicalNozzle
from openburn.core.motor import OpenBurnMotor

from openburn.util.units import convert_magnitude


class InternalBallisticsTest(unittest.TestCase):
    def setUp(self):
        """Set up the test data"""
        self.settings = SimSettings(twophase=0.85, timestep=0.01)
        self.propellant = SimplePropellant("68/10", 0.0341, 0.2249, 4706, 0.058, 1.226)
        # using a list comprehension to create four unique grain objects
        self.grains = [CylindricalCoreGrain(diameter=2, length=4, core_diameter=1, burning_faces=2,
                                            propellant=self.propellant)
                       for _ in range(0, 4)]
        self.nozzle = ConicalNozzle(throat=0.5, exit=2, half_angle=15, throat_len=0.25)
        self.motor = OpenBurnMotor()
        self.motor.set_grains(self.grains)
        self.motor.set_nozzle(self.nozzle)

        self.results = sim.run_sim(self.motor, self.settings)

    # def test_basic_sim(self):
    #     """Outputs basic sim info"""
    #     print("\nResults:")
    #     print("Kn Range: ", self.results.get_kn_range())
    #     print("Burn Time: (s)", self.results.get_burn_time())
    #     print("Max Pressure: (psi)", self.results.get_max_presure())
    #     print("Average Isp: (s)", self.results.get_avg_isp())
    #     print("Max Isp: (s)", self.results.get_max_isp())
    #     print("Max Mass flux: (lb/sec/in^2)", self.results.get_max_mass_flux())
    #
    #     avg_thrust_lb = self.results.get_avg_thrust()
    #     avg_thrust_n = convert_magnitude(avg_thrust_lb, 'lbf', 'newton')
    #     print("Avg Thrust: (lbs)", avg_thrust_lb)
    #     print("Avg Thrust: (newtons)", avg_thrust_n)
    #
    #     impulse_lb = self.results.get_total_impulse()
    #     impulse_n = convert_magnitude(impulse_lb, 'lbf', 'newton')
    #     print("Total Impulse (lb-sec)", impulse_lb)
    #     print("Total Impulse (newton-sec)", impulse_n)

    def test_kn(self):
        kn_low, kn_high = self.results.get_kn_range()
        self.assertAlmostEqual(kn_low, 350, places=-1)
        self.assertAlmostEqual(kn_high, 390, places=-1)
