import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel


def decimalToBinary(decNUm):
    return int(bin(decNUm)[2:])

def decimalToHex(decNUm):
    return hex(decNUm)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Decimal to binary")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.decimalReceiver = QLineEdit()
        self.decimalReceiver.setPlaceholderText("decimal number Interger")
        layout.addWidget(self.decimalReceiver)

        convert_button = QPushButton("convert to binarie")
        convert_button.clicked.connect(self.convert_and_display_binario)
        layout.addWidget(convert_button)
        convert_button = QPushButton("convert to hexadecimal")
        convert_button.clicked.connect(self.convert_and_display_hexadecimal)
        layout.addWidget(convert_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setFixedSize(QSize(400, 200))

    def convert_and_display_binario(self):
        input_decimal = self.decimalReceiver.text()
        decimal = int(input_decimal)
        binaryNumber = decimalToBinary(decimal)
        self.result_label.setText(f"{binaryNumber}")

    def convert_and_display_hexadecimal(self):
        input_decimal = self.decimalReceiver.text()
        decimal = int(input_decimal)
        hexadecimalNumber = decimalToHex(decimal)
        self.result_label.setText(f"{hexadecimalNumber}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()