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
        self.setWindowTitle('Link Extractor')

        self.layout = QVBoxLayout()

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText('Digite a URL aqui')
        self.layout.addWidget(self.url_input)

        self.paste_button = QPushButton('Colar do Clipboard', self)
        self.paste_button.clicked.connect(self.paste_from_clipboard)
        self.layout.addWidget(self.paste_button)

        self.extract_button = QPushButton('Extrair Links', self)
        self.extract_button.clicked.connect(self.extract_links)
        self.layout.addWidget(self.extract_button)

        self.setLayout(self.layout)

    def paste_from_clipboard(self):
        clipboard = QApplication.clipboard()
        self.url_input.setText(clipboard.text())

    def extract_links(self):
        site_link = self.url_input.text()
        if site_link:
            for i, item in enumerate(extract_all_links(site_link), start=1):
                print(f"{i}. {item}")

def main():
    app = QApplication(sys.argv)
    ex = LinkExtractorApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
