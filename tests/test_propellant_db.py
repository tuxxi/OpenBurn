import unittest
import jsonpickle

from openburn.core.propellant import SimplePropellant
from openburn.application.propellant_db import PropellantDatabase


class PropellantDatabaseTest(unittest.TestCase):
    def setUp(self):
        """Set up the test data"""
        self.filename = 'tests/data/propellants.json'
        self.db = PropellantDatabase(self.filename)
        with open(self.filename) as f:
            self.propellants = jsonpickle.decode(f.read())

    def test_load(self):
        self.db.clear_database()
        self.db.load_database(self.filename)
        self.assertEqual(len(self.db.propellants), len(self.propellants))

    def test_remove(self):
        to_remove = self.db.propellants[-1]
        self.db.remove_propellant(to_remove)
        self.assertNotIn(to_remove, self.db.propellants)

    def test_add(self):
        to_add = SimplePropellant("72/10", 0.03, 0.3, 4800, 0.06, 1.25)
        self.db.add_propellant(to_add)
        self.assertIn(to_add, self.db.propellants)

    def test_edit(self):
        old = self.db.propellants[-1]
        to_edit = SimplePropellant("72/10", 0.03, 0.31, 4900, 0.061, 1.244)
        self.db.update_propellant(old, to_edit)
        self.assertIn(to_edit, self.db.propellants)
        self.assertNotIn(old, self.propellants)
