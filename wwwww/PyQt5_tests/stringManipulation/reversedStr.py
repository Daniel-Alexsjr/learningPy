import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel

def reverse_string(textStr):
    return textStr[::-1]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("string severser")

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # String receiver
        self.strReceiver = QLineEdit()
        self.strReceiver.setPlaceholderText("Write here")
        layout.addWidget(self.strReceiver)

        # Button to reverse string
        reverse_button = QPushButton("Reverse String")
        reverse_button.clicked.connect(self.reverse_and_display)
        layout.addWidget(reverse_button)

        # Label to display reversed string
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        # Set fixed size
        self.setFixedSize(QSize(400, 200))

    def reverse_and_display(self):
        input_text = self.strReceiver.text()
        reversed_text = reverse_string(input_text)
        self.result_label.setText(reversed_text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
