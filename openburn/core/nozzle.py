from math import pi, cos, radians

from openburn.object import OpenBurnObject


class OpenBurnNozzle(OpenBurnObject):
    """Base class of all nozzles"""
    def __init__(self, throat: float, exit: float):
        super(OpenBurnNozzle, self).__init__()
        self.throat_dia: float = throat
        self.exit_dia: float = exit

    def get_expansion_ratio(self) -> float:
        return self.get_exit_area() / self.get_throat_area()

    def get_throat_area(self) -> float:
        return 1/4 * pi * self.throat_dia ** 2

    def get_exit_area(self) -> float:
        return 1/4 * pi * self.exit_dia ** 2

    def get_divergence_loss(self) -> float:
        """"""
        return 1


class ConicalNozzle(OpenBurnNozzle):
    """A conical nozzle with a straight cut throat"""
    def __init__(self, throat: float, exit: float, half_angle: float, throat_len: float):
        super(ConicalNozzle, self).__init__(throat, exit)
        self.half_angle = half_angle
        self.throat_len = throat_len

    def get_divergence_loss(self) -> float:
        """
        //http://rasaero.com/dloads/Departures%20from%20Ideal%20Performance.pdf
        :return:
        """
        return (1 + cos(radians(self.half_angle))) / 2
