import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


str = "hello world"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("my app")
        button = QPushButton(str)
        self.setFixedSize(QSize(400,300))

        self.setCentralWidget(button)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()