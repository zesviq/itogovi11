import json
import os


class Settings:
    def __init__(self, settings_file: str):
        self.settings_file = settings_file
        if not os.path.isfile(self.settings_file):
            from sources.settings_preset import _preset as settings
            self.settings = settings
            self.save()
        else:
            with open(self.settings_file, "r", encoding="UTF-8") as f:
                self.settings = json.loads(f.read())
        pass

    def save(self):
        with open(self.settings_file, "w+", encoding="UTF-8") as f:
            f.write(json.dumps(self.settings, indent=5))

    def set_value(self, key: str, value):
        self.settings[key] = value

    def get_value(self, key: str):
        return self.settings[key]
