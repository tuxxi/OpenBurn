import unittest

from openburn.core.propellant import SimplePropellant
from openburn.application.propellant_db import PropellantDatabase


class PropellantDatabaseTest(unittest.TestCase):
    def setUp(self):
        self.db = PropellantDatabase()
        self.db.add_propellant(SimplePropellant("72/10", 0.03, 0.3, 4800, 0.06, 1.25))
        self.db.add_propellant(SimplePropellant("68/10", 0.03, 0.31, 4900, 0.061, 1.244))

    def test_remove(self):
        self.db.remove_propellant("72/10")
        self.assertNotIn("72/10", self.db.propellants)

    def test_add(self):
        to_add = SimplePropellant("68/10", 0.0341, 0.2249, 4706, 0.058, 1.226)
        self.db.add_propellant(to_add)
        self.assertIn(to_add, self.db.propellants.values())

    def test_edit(self):
        to_edit = SimplePropellant("70/10", 0.0341, 0.2249, 4706, 0.058, 1.226)
        self.db.update_propellant("68/10", to_edit)
        self.assertIn(to_edit, self.db.propellants.values())
