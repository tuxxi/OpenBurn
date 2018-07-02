import jsonpickle

from qtpy.QtCore import QObject, Signal


class OpenBurnSettings:
    DEFAULT_UNITS = {
            'length_units': 'inch',
            'mass_units': 'lbs',
            'temperature_units' : 'degF',
            'pressure_units': 'psi',
            'force_units': 'newton',    # why are amateur rocketry units in the USA so inconsistent..?
            'velocity_units': 'feet_per_second',
            'density_units': 'lb_per_cubic_inch',
            'burn_rate_units': 'inch_per_second',
            'mass_flux_units': 'lb_per_sec_per_sq_in'
        }

    def __init__(self):
        # base settings:
        self.redraw_on_changes = True
        self.unit_settings = self.DEFAULT_UNITS


class SettingsDatabase(QObject):
    settings_changed = Signal()

    def __init__(self, filename: str):
        super(SettingsDatabase, self).__init__()
        self.settings = OpenBurnSettings()  # default settings
        self.settings_filename = None
        self.load_settings(filename)

    def load_settings(self, filename: str):
        with open(filename, 'r') as f:
            data = f.read()
            if len(data) > 0:
                self.settings = jsonpickle.decode(data)
        self.settings_filename = filename
        self.emit(self.settings_changed)

    def save_settings(self):
        with open(self.settings_filename, 'w') as f:
            jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
            f.write(jsonpickle.encode(self.settings))

    def default_settings(self):
        self.settings = OpenBurnSettings()
        self.emit(self.settings_changed)
