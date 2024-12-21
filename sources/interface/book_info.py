from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools
import sources.file_extension.epub_class
from si import lang

class BookInfo:
    def __init__(self, book: sources.file_extension.epub_class.epub):
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile("./sources/interface/book_info.ui")
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, None)
        ui_file.close()

        # self.ui.textBrowser = QtWidgets.QTextBrowser()

        self.ui.setWindowTitle(book.metadata["title"])

        rec = ["# ", book.metadata["title"], "\n- **", lang.epub_metadata["path"], "**: ", book.filename]

        for i in ["language", "publisher", "rights", "ISBN", "BookId"]:
            rec += ["\n- ", "**", lang.epub_metadata[i], "**: ", book.metadata[i]]

        self.ui.textBrowser.setMarkdown("".join(rec))

        book.get_metadata()

        # self.ui.setFixedSize(530, 200)

        self.ui.show()