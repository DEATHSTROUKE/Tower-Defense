from random import choice, shuffle, random
from copy import deepcopy
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtWidgets import QLineEdit, QMainWindow, QCheckBox, QPlainTextEdit
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import QFormLayout, QListWidget, QListWidgetItem, QDialog
from PyQt5 import uic
from PyQt5.QtGui import QPalette, QImage, QBrush, QPixmap, QIcon


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui', self)
        self.setWindowIcon(QIcon('data/Pictures/171.png'))
        self.setWindowTitle('Tower Defence')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    n = Menu()
    n.show()
    sys.exit(app.exec_())
