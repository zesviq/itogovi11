import sys
from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools
from sources.interface.main_interface import MainWindow
# from sources.interface.book_info import BookInfo
# from sources.interface.about import AboutWindow
from sources.interface.reader import ReaderWindow
from sources.interface.settings import SettingsWindow

import si

if __name__ == '__main__':
    from sources.file_extension.epub_class import epub as EPUB

    app = QtWidgets.QApplication(sys.argv)

    b = ReaderWindow(
        # EPUB("./books/010000_000060_ART-8f382c81-78f9-4575-bf21-4cfcd2439626-Преступление_и_наказание.epub")
        EPUB("C:/Users/asata/Downloads/010000_000060_ART-33bfc45a-3b08-4ee0-94b8-1902bcfc6828-Вишневый_сад.epub")
    )

    # si.Singleton.MainWindow = MainWindow()
    si.Singleton.SettingsWindow = SettingsWindow()

    app.exec()
