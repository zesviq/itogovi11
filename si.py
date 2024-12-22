import os
from sources.interface.main_interface import MainWindow
import sources.settings

settings = sources.settings.Settings("./settings.json")
import sources.lang.ru as lang


class _Singleton:
    def __init__(self):
        pass


Singleton = _Singleton()
