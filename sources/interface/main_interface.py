from PySide6 import QtCore, QtWidgets, QtGui, QtUiTools


class MainWindow:
    def __init__(self):
        loader = QtUiTools.QUiLoader()
        ui_file = QtCore.QFile("./sources/interface/ui/main.ui")
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, None)
        ui_file.close()

        with open("sources/interface/styles/all_palette.qss") as st:
            self.ui.setStyleSheet(st.read())

        self.ui.show()

    def get(self):
        return self.ui
