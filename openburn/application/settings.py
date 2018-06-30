from qtpy.QtCore import QObject


class OpenBurnSettings(QObject):
    def __init__(self):
        super(OpenBurnSettings, self).__init__()
        self.settings_filename: str = None

    def load_settings(self, filename: str) -> bool:
        pass

    def save_settings(self) -> bool:
        pass
