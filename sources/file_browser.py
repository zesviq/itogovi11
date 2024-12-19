import si
import os
import sys


class FileBrowser:
    def __init__(self):
        si.settings.get_value("apptest")

    def scan_folder(self):
        return os.listdir("books")
        pass


a = FileBrowser().scan_folder()
print(a)

