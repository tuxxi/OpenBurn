from pint import UnitRegistry, set_application_registry

ureg = UnitRegistry()
set_application_registry(ureg)
Q_ = ureg.Quantity

# define slugs
ureg.define('slug = lbf * s**2 / foot = slug')

# define density units
ureg.define('lb_per_cubic_inch = pounds / (inch**3) = lb/in3')
ureg.define('slug_per_cubic_inch = slug / (inch**3) = slug/in3')
ureg.define('kg_per_cubic_meter = kilogram / (meter**3) = kg/m3')