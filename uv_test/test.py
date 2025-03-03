# Basic PySide6 app
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.click_counter = 0
        self.show()
        self.setWindowTitle('Minun sovellus')

        button = QPushButton('Click me!')
        button.setCheckable(True)
        button.clicked.connect(self.print_click)
        button.clicked.connect(self.count_clicks)
        self.setCentralWidget(button)

    def print_click(self, is_checked):
        print(f'Button is clicked! {is_checked=}')
    
    def count_clicks(self):
        self.click_counter += 1
        print(self.click_counter)

app = QApplication()    # Aina pitää luoda QApplication, mutta VAIN YKSI!!!!

window = MainWindow()      # Qt toimii ns. "widgetteillä". Jos widgettillä ei ole "vanhempia", se näyttää ikkunalta
# window.show()           # Ikkunat ovat piilotettu oletuksena. Pitää näyttää niitä aktiivisesti

app.exec()              # `exec` aloittaa se "Event loop"