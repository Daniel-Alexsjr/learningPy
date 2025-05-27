import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt
from lorem_text import lorem

class LoremIpsumGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lorem Ipsum Generator')

        # Layout
        layout = QVBoxLayout()

        # Label
        self.label = QLabel('Enter the number of words:')
        layout.addWidget(self.label)

        # Input
        self.input = QLineEdit(self)
        layout.addWidget(self.input)

        # Button
        self.button = QPushButton('Generate', self)
        self.button.clicked.connect(self.generate_lorem)
        layout.addWidget(self.button)

        # Output
        self.output = QTextEdit(self)
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        # Set layout
        self.setLayout(layout)

    def generate_lorem(self):
        try:
            num_words = int(self.input.text())
            if num_words <= 0:
                raise ValueError("Number of words must be positive.")
            lorem_text = ''.join(lorem.words(num_words))
            self.output.setText(lorem_text)
        except ValueError:
            self.output.setText("Please enter a valid positive integer.")

def main():
    app = QApplication(sys.argv)
    ex = LoremIpsumGenerator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
