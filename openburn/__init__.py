from os import path, walk, pardir

# Create path references for resource files and such
ROOT_PATH = path.dirname(path.realpath(path.join(__file__, pardir)))
RESOURCE_PATH = path.join(ROOT_PATH, 'res/')

__version__ = "0.2.0"

