from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon

import sys
from random import choice


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(510, 238)
        self.setWindowTitle("О программе")
        # self.setWindowIcon(QIcon(filename="citrus.png", da))
        self.setFocus()


        # Устанавливаем центральный виджет Window.


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()