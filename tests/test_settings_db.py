import unittest
import jsonpickle

from openburn.application.settings import OpenBurnSettings, SettingsDatabase


class SettingsDatabaseTest(unittest.TestCase):
    def setUp(self):
        """Set up the test data"""
        self.filename = 'tests/data/settings.json'
        self.db = SettingsDatabase(self.filename)

    def test_load(self):
        self.db.default_settings()
        self.db.load_settings(self.filename)
        # the settings data file should have redraw_on_changes as false
        self.assertEquals(self.db.settings.redraw_on_changes, False)

    def test_save(self):
        self.db.settings.redraw_on_changes = True
        self.db.save_settings()
        self.db.load_settings(self.filename)
        self.assertEquals(self.db.settings.redraw_on_changes, True)

        # clean up
        self.db.settings.redraw_on_changes = False
        self.db.save_settings()
