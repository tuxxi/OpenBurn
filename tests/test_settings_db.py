import unittest
import jsonpickle

from openburn.application.settings import SettingsDatabase


class SettingsDatabaseTest(unittest.TestCase):
    def setUp(self):
        """Set up the test data"""
        self.db = SettingsDatabase()

    def test_default(self):
        self.db.settings.redraw_on_changes = False
        self.assertEqual(self.db.settings.redraw_on_changes, False)
        self.db.default_settings()
        self.assertEqual(self.db.settings.redraw_on_changes, True)
