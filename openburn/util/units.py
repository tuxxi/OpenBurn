from pint import UnitRegistry

ureg = UnitRegistry()

# define slugs
ureg.define('slug = lbf * s**2 / foot = slug')

# define density units
ureg.define('lb_per_cubic_inch = pounds / (inch**3) = lb_per_in3')
ureg.define('slug_per_cubic_inch = slug / (inch**3) = slug_per_in3')
ureg.define('kg_per_cubic_meter = kilogram / (meter**3) = kg_per_m3')


def convert_magnitude(val: float, from_: str, to_: str) -> float:
    """
    Convert a magnitude to a new unit
    :param val: the magnitude to convert
    :param from_: the unit to convert from, a str defined in the pint unit registry @ureg
    :param to_:the unit to convert to, a str defined in the pint unit registry @ureg
    :return: the new magnitude, in terms of unit @to_
    """
    old = ureg.Quantity(val, from_)
    new = old.to(to_)
    return new.magnitude
