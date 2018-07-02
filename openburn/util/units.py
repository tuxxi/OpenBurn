from pint import UnitRegistry

# Pint's unit registry has many units, but we need to define a few ourselves.
ureg = UnitRegistry()

# for some reason slugs are not a default unit (probably because slugs are ridicules and awful )
ureg.define('slug = lbf * s**2 / foot = slug')

# density units
ureg.define('lb_per_cubic_inch = pounds / (inch**3) = lb_per_in3')
ureg.define('slug_per_cubic_inch = slug / (inch**3) = slug_per_in3')
ureg.define('kg_per_cubic_meter = kilogram / (meter**3) = kg_per_m3')

# velocity units
ureg.define('feet_per_second = feet / second = fps')
ureg.define('meters_per_second = meters / second = mps')

# burn rate units
ureg.define('inch_per_second = inch / second = ips')
ureg.define('mm_per_second = mm / second = mmps')

# mass flux units
ureg.define('lb_per_sec_per_sq_in = lb / second / inch**2')
ureg.define('kg_per_sec_per_sq_m = kg / second / meter**2')


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
