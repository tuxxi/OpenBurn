from openburn.core.propellant import OpenBurnPropellant
from openburn.core.object import OpenBurnObject


class OpenBurnGrain(OpenBurnObject):
    """Base class of all propellant segments"""
    def __init__(self, diameter: float, length: float, burning_faces: float,
                 propellant: OpenBurnPropellant = None):

        super(OpenBurnGrain, self).__init__()
        self.diameter: float = diameter
        self.length: float = length
        self.burning_faces: float = burning_faces
        self.propellant: OpenBurnPropellant = propellant


class CylindricalCoreGrain(OpenBurnGrain):
    """A cylindrical core BATES grain"""
    def __init__(self, diameter: float, length: float, burning_faces: float,
                 core_diameter: float, propellant: OpenBurnPropellant = None):

        super(CylindricalCoreGrain, self).__init__(diameter, length, burning_faces, propellant)
        self.core_diameter: float = core_diameter
