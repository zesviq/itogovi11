from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools

import si
from sources.file_extension.epub_class import epub
from sources.interface.book_info import BookInfo


class ReaderWindow:
    def __init__(self, book: epub):
        self.book = book
        self.book_info = None
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile("./sources/interface/ui/reader.ui")
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()

        self.ui.setWindowTitle(book.metadata["title"])
        self.generate_toc()
        self.ui.dockWidget.hide()
        # Buttons
        self.ui.toc_toggle.clicked.connect(self.toggle_tos)

        self.ui.book_info.clicked.connect(self.open_book_info)
        self.ui.open_settings.clicked.connect(self.open_settings)

        self.ui.toggle_fullscreen.clicked.connect(self.toggle_fullscreen)
        self.ui.toggle_max_r.clicked.connect(self.toggle_max_r)

        self.update_theme()

        self.init_hotkeys()
        # self.ui.horizontalSpacer.hide()
        # self.ui.horizontalSpacer_2.hide()
        self.ui.show()

    def generate_toc(self):
        a = self.book.table_of_context()
        items = []
        for i in a:
            q = QtWidgets.QTreeWidgetItem(self.ui.table_of_contents, [str(i.label)])
            q.info = i
            items.append(q)

        self.ui.table_of_contents.insertTopLevelItems(0, items)
        # self.ui.table_of_contents = QtWidgets.QTreeWidget()
        self.ui.table_of_contents.itemClicked.connect(self.onItemClicked)

        QtGui.QShortcut('F1', self.ui.table_of_contents).activated.connect(self.onItemClicked)

    @QtCore.Slot(QtWidgets.QTreeWidgetItem, int)
    def onItemClicked(self, it, col):
        self.generate_page(it.info.path)

    @QtCore.Slot()
    def toggle_tos(self):
        if self.ui.dockWidget.isHidden():
            self.ui.dockWidget.show()
        else:
            self.ui.dockWidget.hide()

    @QtCore.Slot()
    def generate_page(self, path):
        page = self.book.load_chapter(path)

        with open("sources/interface/html/reader.html") as f:
            self.ui.content.setHtml(page.replace("</head>", f.read()+"</head>").replace("<p", "<p align='justify' "))
        pass

    @QtCore.Slot()
    def open_book_info(self):
        if self.book_info is None:
            from sources.interface.book_info import BookInfo
            self.book_info = BookInfo(self.book)
            self.book_info.ui.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
            self.book_info.ui.show()
        else:
            self.book_info.ui.show()

    @QtCore.Slot()
    def open_settings(self):
        si.Singleton.SettingsWindow.open()
        si.Singleton.SettingsWindow.ui.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

    @QtCore.Slot()
    def toggle_max_r(self):
        self.ui.content.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed))

        # if self.ui.isFullScreen():
        #     self.ui.content = QtWidgets.QTextBrowser()
        #     self.ui.toggle_max_r.setIcon(QtGui.QIcon("sources/interface/icons/max.png"))
        # else:
        #     self.ui.showFullScreen()
        #     self.ui.toggle_max_r.setIcon(QtGui.QIcon("sources/interface/icons/min.png"))
        # pass

    @QtCore.Slot()
    def toggle_fullscreen(self):
        if self.ui.isFullScreen():
            self.ui.showNormal()
            self.ui.toggle_fullscreen.setIcon(QtGui.QIcon("sources/interface/icons/max.png"))

        else:
            self.ui.showFullScreen()
            self.ui.toggle_fullscreen.setIcon(QtGui.QIcon("sources/interface/icons/min.png"))

    def update_theme(self):
        with open(si.settings.get_value("app.read.theme")) as st:
            self.ui.setStyleSheet(st.read())

            # self.ui.content = QtWidgets.QTextBrowser()

            fnt = QtGui.QFont()
            fnt.setPointSize(40)
            fnt.setFamily(si.settings.get_value("reader.font"))
            self.ui.content.setFont(fnt)


    def init_hotkeys(self):
        QtGui.QShortcut('F11', self.ui).activated.connect(self.toggle_fullscreen)
        QtGui.QShortcut('F12', self.ui).activated.connect(self.toggle_tos)
        QtGui.QShortcut('F2', self.ui).activated.connect(self.open_book_info)