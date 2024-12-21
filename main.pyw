import sys
from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools

# from sources.interface.main_interface import MainWindow
# from sources.interface.about import AboutWindow

import si


if __name__ == '__main__':
    from sources.file_extension.epub_class import epub as EPUB
    app = QtWidgets.QApplication(sys.argv)

    import sources.interface.book_info

    a = sources.interface.book_info.BookInfo(
        EPUB("./books/010000_000060_ART-8f382c81-78f9-4575-bf21-4cfcd2439626-Преступление_и_наказание.epub")
    )

    # import file_browser


    # main_win = MainWindow()
    # main_win2 = AboutWindow()

    app.exec()
