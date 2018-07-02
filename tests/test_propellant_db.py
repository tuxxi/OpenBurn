import unittest
import jsonpickle

from openburn.core.propellant import SimplePropellant
from openburn.application.propellant_db import PropellantDatabase


class PropellantDatabaseTest(unittest.TestCase):
    def setUp(self):
        self.db = PropellantDatabase()
        self.db.add_propellant(SimplePropellant("72/10", 0.03, 0.3, 4800, 0.06, 1.25))
        self.db.add_propellant(SimplePropellant("72/10", 0.03, 0.31, 4900, 0.061, 1.244))

    def test_remove(self):
        to_remove = self.db.propellants[-1]
        self.db.remove_propellant(to_remove)
        self.assertNotIn(to_remove, self.db.propellants)

    def test_add(self):
        to_add = SimplePropellant("68/10", 0.0341, 0.2249, 4706, 0.058, 1.226)
        self.db.add_propellant(to_add)
        self.assertIn(to_add, self.db.propellants)

    def test_edit(self):
        old = self.db.propellants[-1]
        to_edit = SimplePropellant("68/10", 0.0341, 0.2249, 4706, 0.058, 1.226)
        self.db.update_propellant(old, to_edit)
        self.assertIn(to_edit, self.db.propellants)
        self.assertNotIn(old, self.db.propellants)
