import os
from sources.interface.main_interface import MainWindow
import sources.settings

settings = sources.settings.Settings("./settings.json")
import sources.lang.ru as lang


class _Singleton:
    def __init__(self):
        self.opened = []
        pass

    def open(self, window):
        return self.opened.append(window)


Singleton = _Singleton()
