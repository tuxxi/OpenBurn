from abc import abstractmethod
from math import pi

from openburn.core.propellant import OpenBurnPropellant
from openburn.object import OpenBurnObject


class OpenBurnGrain(OpenBurnObject):
    """Base class of all propellant segments.
    The segment is cylindrical with a 2D port shape extruded through the entire length.
    """
    def __init__(self, diameter: float, length: float, burning_faces: float,
                 propellant: OpenBurnPropellant = None):

        super(OpenBurnGrain, self).__init__()
        # all lengths in inches
        self.diameter: float = diameter
        self.length: float = length
        self.burning_faces: float = burning_faces
        self.propellant: OpenBurnPropellant = propellant

        self.burn_rate = 0  # state variable. ew.

    def get_volume(self) -> float:
        """
        Calculates the volume of the grain
        :return: volume of the grain in in^3
        """
        grain_volume = (self.diameter / 2) ** 2 * pi * self.length
        port_volume = self.get_port_area() * self.length
        return grain_volume - port_volume

    @abstractmethod
    def get_burning_area(self):
        """
        get the uninhibited burning area
        :return: burning surface area in in^2
        """

    @abstractmethod
    def burn(self, burnrate: float, time_step: float) -> bool:
        """Regress the grain by the given amount
        :param burnrate: the burn rate in inches / second
        :param time_step: how much time will pass
        :returns True if burn was successful and False if grain is burned out.
        """

    @abstractmethod
    def get_port_area(self) -> float:
        """
        returns the area of the grain port
        :returns port area in in^2
        """

    @abstractmethod
    def is_burned_out(self) -> bool:
        """
        Is the grain burned out?
        :return: true if it is burned out, false if not
        """


class CylindricalCoreGrain(OpenBurnGrain):
    """A cylindrical core BATES grain"""
    def __init__(self, diameter: float, length: float, burning_faces: float,
                 core_diameter: float, propellant: OpenBurnPropellant = None):
        """
        :param diameter: the grain's diameter, in inches
        :param length: the grain's length, in inches
        :param burning_faces: # of faces burning. two is typical, if both are inhibited, this number is 0
        :param core_diameter: diameter of the grain's cylindrical core, in inches
        :param propellant: an OpenBurnPropellant object
        """
        super(CylindricalCoreGrain, self).__init__(diameter, length, burning_faces, propellant)
        self.core_diameter: float = core_diameter

    def burn(self, burnrate: float, time_step: float) -> bool:
        if self.is_burned_out():
            return False
        self.burn_rate = burnrate

        burn_dist = burnrate * time_step
        self.core_diameter += 2 * burn_dist
        self.length -= self.burning_faces * burn_dist
        return True

    def get_port_area(self) -> float:
        return (self.core_diameter / 2) ** 2 * pi

    def get_burning_area(self):
        core_area = pi * self.core_diameter * self.length
        face_area = 1/4*pi * (self.diameter**2 - self.core_diameter**2)
        return core_area + self.burning_faces * face_area

    def is_burned_out(self):
        return self.core_diameter >= self.diameter
