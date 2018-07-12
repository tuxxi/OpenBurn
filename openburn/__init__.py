from os import path, pardir

# Create path references for resource files and such
ROOT_PATH = path.dirname(path.realpath(path.join(__file__, pardir)))
RESOURCE_PATH = path.join(ROOT_PATH, 'res/')

__version__ = '0.2.0'
__author__ = 'tuxxi'
__author_email__ = 'aidan@sojourner.me'

__special_thanks__ = ['John Wickman',
                      'Peter Hackett']
