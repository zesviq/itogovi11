from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools

import si
from sources.interface.styles._theme_list import _theme_list
from si import lang, settings, Singleton


class SettingsWindow:
    def __init__(self):
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile("./sources/interface/ui/settings.ui")
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, None)
        ui_file.close()
        QtGui.QShortcut('Esc', self.ui).activated.connect(self.ui.close)
        self.ui.theme.addItems([lang.theme_list[key] for key, value in _theme_list.items()])

        self.ui.ok.clicked.connect(self.save)
        self.ui.theme.activated.connect(self.theme_update)
        self.thitmememe = settings.get_value("app.read.theme")

    @QtCore.Slot()
    def soi(self):
        pass

    def open(self):
        fnt = QtGui.QFont()
        fnt.setFamily(settings.get_value("reader.font"))
        self.ui.font_family.setCurrentFont(fnt)

        self.ui.font_size.setValue(settings.get_value("reader.font.size.points"))

        self.ui.setWindowTitle("Настройки")
        self.ui.show()

    def theme_update(self):
        self.thitmememe = _theme_list[list(filter(lambda x: lang.theme_list[x] == self.ui.theme.currentText(), lang.theme_list))[0]]

    def save(self):
        # self.ui.font_family = QtWidgets.QFontComboBox()
        settings.set_value("reader.font", self.ui.font_family.currentFont().family())

        settings.set_value("app.read.theme", self.thitmememe)

        # self.ui.theme = QtWidgets.QComboBox()
        settings.save()
        self.ui.close()


        for i in Singleton.opened:
            i.update_theme()

        print(Singleton.opened)