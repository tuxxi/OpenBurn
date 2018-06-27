from openburn.core.object import OpenBurnObject


class OpenBurnPropellant(OpenBurnObject):
    """Base class of all propellants"""
    def __init__(self, name: str) -> None:
        super(OpenBurnPropellant, self).__init__()
        self.name = name


class SimplePropellant(OpenBurnPropellant):
    """Simple propellant using Saint Robert's law"""
    def __init__(self, name: str, a: float, n: float, cstar: float, rho: float, gamma: float = 1.25) -> None:
        super(SimplePropellant, self).__init__(name)
        self.a : float= a
        self.n: float = n
        self.cstar: float = cstar
        self.rho: float = rho
        self.gamma: float= gamma


class AdvancedPropellant(SimplePropellant):
    NotImplemented
