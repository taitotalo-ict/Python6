# Basic PySide6 app
from random import choice
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        self.counter = 0

        self.setWindowTitle('A')
        button = QPushButton('Click me!')
        button.clicked.connect(self.change_title)
        button.clicked.connect(self.print_click)

        self.setCentralWidget(button)
        self.button = button
        self.windowTitleChanged.connect(self.print_window_title)

    def change_title(self):
        titles = ['A', 'B', 'C', 'D']
        old_title = self.windowTitle()
        while old_title == self.windowTitle():
            self.setWindowTitle(choice(titles))
    
    def print_click(self):
        print('Button has been clicked')
        self.counter += 1
        if self.counter == 10:
            self.button.setDisabled(True)
            # self.button.setEnabled(False)

    def print_window_title(self, new_title):
        print(f'New window title is: {new_title}')

app = QApplication()    # Aina pitää luoda QApplication, mutta VAIN YKSI!!!!

window = MainWindow()      # Qt toimii ns. "widgetteillä". Jos widgettillä ei ole "vanhempia", se näyttää ikkunalta

app.exec()              # `exec` aloittaa se "Event loop"