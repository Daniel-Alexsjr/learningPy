import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel

def imcCalculator(weight, height):
    return weight / height**2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("imc calculator")

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # String receiver
        self.weightReceiver = QLineEdit()
        self.weightReceiver.setPlaceholderText("weight (kg)")
        layout.addWidget(self.weightReceiver)

        self.heightReceiver = QLineEdit()
        self.heightReceiver.setPlaceholderText("height (m)")
        layout.addWidget(self.heightReceiver)

        # Button to call the function calculate_and_display
        calculate_button = QPushButton("calculate IMC")
        calculate_button.clicked.connect(self.calculate_and_display)
        layout.addWidget(calculate_button)

        # Label to display
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        # Set fixed size
        self.setFixedSize(QSize(400, 200))

    def calculate_and_display(self):
        input_weight = self.weightReceiver.text()
        input_height = self.heightReceiver.text()

        try:
            weight = float(input_weight)
            height = float(input_height)
            imc = imcCalculator(weight, height)
            self.result_label.setText(f"IMC: {imc:.2f}") # .2f ## 2 for decimals qnd f for float
        
        except ValueError:
            self.result_label.setText("Please enter valid numbers for weight and height.")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
 