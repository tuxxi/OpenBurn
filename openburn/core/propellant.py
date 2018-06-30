from openburn.object import OpenBurnObject


class OpenBurnPropellant(OpenBurnObject):
    """Base class of all propellants"""
    def __init__(self, name: str) -> None:
        super(OpenBurnPropellant, self).__init__()
        self.name = name


class SimplePropellant(OpenBurnPropellant):
    """Simple propellant using Saint Robert's law (r = aP^n)"""
    def __init__(self, name: str, a: float, n: float, cstar: float, rho: float, gamma: float = 1.25) -> None:
        """
        :param name: The propellant's name
        :param a: ballistic burn rate coefficient 'a' in r=aP^n, measured in inches / second
        :param n: ballistic burn rate exponent 'n' in r=aP^n, dimensionless
        :param cstar: characteristic velocity, (C*), measured in feet/second
        :param rho: density of propellant, measured in lbs/in^3
        :param gamma: Ratio of specific heats Cp/Cv, dimensionless
        """
        super(SimplePropellant, self).__init__(name)
        self.a: float = a
        self.n: float = n
        self.cstar: float = cstar
        self.rho: float = rho
        self.gamma: float = gamma


class AdvancedPropellant(SimplePropellant):
    NotImplemented
