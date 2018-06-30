from setuptools import setup
from openburn import __version__

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='OpenBurn',
    version=__version__,
    description='Open source solid rocket motor internal ballistics simulation',
    author='tuxxi',
    author_email='aidan@sojourner.me',
    licence='GPL3',
    long_description=long_description,
    packages=['OpenBurn'],
    package_dir={'OpenBurn': 'openburn'},
    package_data={'OpenBurn': ['res/*']},
)