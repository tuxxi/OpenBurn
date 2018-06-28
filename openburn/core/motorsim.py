from qtpy.QtCore import QObject, Signal, Slot

from openburn.core.motor import OpenBurnMotor


class MotorSimDataPoint:
    """A simulation data point"""
    def __init__(self):
        self.motor: OpenBurnMotor = None
        self.pressure: float = 0
        self.mass_flux: float = 0
        self.thrust: float = 0
        self.isp: float = 0
        self.kn: float = 0

        self.burn_rate: float = 0
        self.time_stamp: float = 0


class MotorSim(QObject):
    """The internal ballistics simulator"""
    SimulationStarted = Signal()
    SimulationFinished = Signal(bool)

    def __init__(self):
        super(MotorSim, self).__init__()
