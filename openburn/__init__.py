from os import path, walk, pardir

# Create path references for resource files and such
ROOT = path.dirname(path.realpath(path.join(__file__, pardir)))
RES = path.join(ROOT, 'res/')

__version__ = "0.2.0"

