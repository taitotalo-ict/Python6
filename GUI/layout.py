# from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.show()


        label = QLabel('Push the button to do something')
        button = QPushButton('Click me')

        layout = QVBoxLayout()

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        layout.addWidget(label)
        layout.addWidget(button)

app = QApplication()    # Aina pitää luoda QApplication, mutta VAIN YKSI!!!!
window = MainWindow()      # Qt toimii ns. "widgetteillä". Jos widgettillä ei ole "vanhempia", se näyttää ikkunalta
app.exec()              # `exec` aloittaa se "Event loop"