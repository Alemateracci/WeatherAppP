import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainAppWindow()
    main_window.show()
    sys.exit(app.exec_())