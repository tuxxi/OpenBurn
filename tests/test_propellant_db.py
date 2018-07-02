import unittest

from openburn.core.propellant import SimplePropellant
from openburn.application.propellant_db import PropellantDatabase


class InternalBallisticsTest(unittest.TestCase):
    def setUp(self):
        """Set up the test data"""
        self.propellants = [SimplePropellant("68/10", 0.0341, 0.2249, 4706, 0.058, 1.226),
                            SimplePropellant("Orange Sunset", 0.015, 0.2, 4800, 0.6),
                            SimplePropellant("TEST", 1, 2, 3, 4, 5)
                            ]
        self.filename = 'tests/data/propellants.json'
        self.db = PropellantDatabase(self.filename)
        for prop in self.propellants:
            self.db.add_propellant(prop)

    def test_save(self):
        self.db.save_database()

    def test_load(self):
        self.db.clear_database()
        self.db.load_database(self.filename)
        self.assertEqual(len(self.db.propellants), len(self.propellants))

    def test_remove(self):
        to_remove = self.propellants[-1]
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
