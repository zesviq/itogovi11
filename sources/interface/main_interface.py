from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools


class MainWindow:
    def __init__(self):
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile("./sources/interface/settings.ui")
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, None)
        ui_file.close()


        self.ui.show()

    def get(self):
        return self.ui
