from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools


class SettingsWindow:
    def __init__(self):
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile("./sources/interface/ui/settings.ui")
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, None)
        ui_file.close()
        QtGui.QShortcut('Esc', self.ui).activated.connect(self.ui.close)

    def open(self):
        self.ui.show()