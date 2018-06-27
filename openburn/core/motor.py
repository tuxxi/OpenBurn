
from openburn.core.grain import OpenBurnGrain
from openburn.core.object import OpenBurnObject
from openburn.core.nozzle import OpenBurnNozzle

from typing import List


class OpenBurnMotor(OpenBurnObject):
    def __init__(self):
        super(OpenBurnMotor, self).__init__()
        self.grains: List[OpenBurnGrain] = []
        self.nozzle: OpenBurnNozzle = None

    def add_grain(self, grain: OpenBurnGrain):
        self.grains.append(grain)