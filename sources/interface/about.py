from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools


class AboutWindow:
    def __init__(self):
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile("./sources/interface/ui/about.ui")
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, None)
        ui_file.close()

        self.ui.setFixedSize(530, 200)

        self.ui.show()

    def get(self):
        return self.ui
