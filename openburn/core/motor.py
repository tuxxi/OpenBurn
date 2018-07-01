from typing import List
from statistics import mean
from math import ceil

from openburn.core.grain import OpenBurnGrain
from openburn.core.nozzle import OpenBurnNozzle
from openburn.core.propellant import SimplePropellant

from openburn.object import OpenBurnObject


class OpenBurnMotor(OpenBurnObject):
    def __init__(self) -> None:
        super(OpenBurnMotor, self).__init__()
        self.grains: List[OpenBurnGrain] = []
        self.nozzle: OpenBurnNozzle = None
        self.avg_propellant = None

    def add_grain(self, grain: OpenBurnGrain) -> None:
        self.grains.append(grain)

    def set_grains(self, grains: List[OpenBurnGrain]) -> None:
        self.grains = grains
        self.avg_propellant = self.calc_avg_propellant()

    def set_nozzle(self, nozzle: OpenBurnNozzle) -> None:
        self.nozzle = nozzle

    def calc_avg_propellant(self) -> "SimplePropellant":
        """
        approximation time!! The average propellant is just the aesthetic mean of all the
        individual propellant params
        :return:
        """
        a = mean(grain.propellant.a for grain in self.grains)
        n = mean(grain.propellant.n for grain in self.grains)
        cstar = mean(grain.propellant.cstar for grain in self.grains)
        rho = mean(grain.propellant.rho for grain in self.grains)
        gamma = mean(grain.propellant.gamma for grain in self.grains)
        return SimplePropellant("AVG:" + str(self.uuid), a, n, cstar, rho, gamma)

    def get_num_grains(self) -> float:
        return len(self.grains)

    def get_length(self) -> float:
        """
        :return: propellant length, in inches
        """
        return sum(x.length for x in self.grains)

    def get_diameter(self):
        """
        :return: maximum grain diameter of the motor, in inches
        """
        return max(x.diameter for x in self.grains)

    def get_propellant_mass(self) -> float:
        """
        :return Propellant mass, in lbs
        """
        return sum(x.get_volume() * x.propellant.rho for x in self.grains)

    def get_port_throat_ratio(self) -> float:
        """
        :return: Ratio of bottom grain port area to nozzle throat area, dimensionless
        """
        return self.grains[-1].get_port_area() / self.nozzle.get_throat_area()

    def get_volume_loading(self) -> float:
        """
        :return: Ratio of propellant volume to chamber volume, dimensionless
        """
        propellant_volume = sum(x.get_volume() for x in self.grains)
        chamber_volume = (self.get_diameter() / 2) ** 2 * self.get_length()
        return propellant_volume / chamber_volume

    def get_upstream_mass_flow(self, x_val: float) -> float:
        """
        Calculate how much mass flow is occurring upstream of this given x coordinate
        :param x_val: x value of the point to find mass flux,
            where x = 0 is at the head end and x = len is the end of the propellant surface.
        :returns mass flow, in lb/sec
        """
        x = 0
        mass_flow = 0
        for grain in self.grains:
            len_ = grain.length
            if x <= x_val:
                pass
                if ceil(x) < ceil(x_val - len_):
                    burning_surface = grain.get_burning_area()
                else:
                    burning_surface = grain.get_upstream_burning_area(x + len_ - x_val)
                mass_flow += burning_surface * grain.propellant.rho * grain.burn_rate

            x += len_

        return mass_flow

    def get_mass_flow(self) -> float:
        """
        Calculate total mass flow out of the nozzle
        :return: mass flow in lb/sec
        """
        return sum(
            grain.get_burning_area() *
            grain.propellant.rho *
            grain.burn_rate
            for grain in self.grains)

    def get_grain_at_x(self, x_val: float) -> "OpenBurnGrain" or None:
        """
        Returns the grain found at the given x -val in the motor
        :param x_val: x value of the point to find mass flux,
            where x = 0 is at the head end and x = len is the end of the propellant surface.
        :return: the grain if found, otherwise None
        """
        x = 0
        for grain in self.grains:
            x += grain.length
            if x >= x_val:
                return grain

        return None

    def get_burning_area(self) -> float:
        """
        Sum of all burning surface area in the motor
        :return: burning area, in in^2
        """
        return sum(x.get_burning_area() for x in self.grains)

    def get_kn(self) -> float:
        """
        Kn (ratio of burning surface area to nozzle area)
        :return:
        """
        return self.get_burning_area() / self.nozzle.get_throat_area()
