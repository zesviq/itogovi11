import json

import si
import os

import sources.file_extension.epub_class

file_extensions = ['epub']


def get_file_extension(filename):
    return filename.split(".")[-1]


class FileBrowser:
    def __init__(self):
        self.file_list = {}

        # create temp folder

        t = "temp"
        if not (os.path.exists(t) and not os.path.isfile(t)):
            os.makedirs("./temp")

        pass

    def scan_folder(self, directory: str):
        folder = os.listdir(directory)
        folder_files = []
        for file_name in folder:
            if os.path.isfile(directory + "/" + file_name) and get_file_extension(file_name) in file_extensions:
                folder_files.append(directory + "/" + file_name)
        self.file_list[directory] = folder_files

    def get_file_list(self):
        return self.file_list

    def init_file(self, filename):
        ext = get_file_extension(filename)

        try:
            if ext == "epub":
                return sources.file_extension.epub_class.epub(filename)
        except KeyError:
            raise KeyError("FileBroken")


_FileBrowser = FileBrowser()
