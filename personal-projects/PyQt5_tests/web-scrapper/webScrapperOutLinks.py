import sys
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse, urljoin
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QInputDialog

def extract_all_links(site):
    html = requests.get(site).text
    soup = bs(html, 'html.parser').find_all('a')
    links = [link.get('href') for link in soup]

    external_links = []
    for link in links:
        absolute_link = urljoin(site, link)
        parsed_url = urlparse(absolute_link)
        if parsed_url.netloc and parsed_url.netloc != urlparse(site).netloc:
            external_links.append(absolute_link)

    return external_links

class LinkExtractorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('External Link Extractor') #widget title

        self.layout = QVBoxLayout() #creates a window vertical layout

        self.url_input = QLineEdit(self) #creates a input dialog to the user write
        self.url_input.setPlaceholderText('Digite a URL aqui') #sets palceholder text
        self.layout.addWidget(self.url_input) #adiciona a caixa de texto ao layouts

        self.paste_button = QPushButton('Colar do Clipboard', self) #creates a button with 'colar do clipboard message'
        self.paste_button.clicked.connect(self.paste_from_clipboard) #conects the button with the function paste_from_clipboard
        self.layout.addWidget(self.paste_button) #add button to layout

        self.extract_button = QPushButton('Extrair Links', self) #creates a button with 'extrair links' str
        self.extract_button.clicked.connect(self.extract_links) #conects button click with the function 'extract_links"
        self.layout.addWidget(self.extract_button) #add button to layour

        self.setLayout(self.layout) #sets vertical layout to main window

    def paste_from_clipboard(self):
        clipboard = QApplication.clipboard() #gets the clipboard content
        self.url_input.setText(clipboard.text()) #defines the input box text to the clipboard

    def extract_links(self):
        site_link = self.url_input.text() #receives the text that the user input
        if site_link:
            for i, item in enumerate(extract_all_links(site_link), start=1):
                print(f"{i}. {item}") #displays the content enumarated and in order

def main():
    app = QApplication(sys.argv) #essential for pyqt5 aplication
    ex = LinkExtractorApp() #creates an instance LinkExtractorApp
    ex.show() #shows the instance
    sys.exit(app.exec_()) #start app event loop and ant stop it when closed

if __name__ == "__main__":
    main()
