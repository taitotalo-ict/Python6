from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)
from PySide6.QtGui import QPalette, QColor


class Color(QWidget):
    def __init__(self, color):
        super().__init__()

        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(self.backgroundRole(), color)
        # palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.show()

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('green'))
        layout2.addWidget(Color('blue'))

        layout3.addWidget(Color('purple'))
        layout3.addWidget(Color('black'))
        
        layout1.addLayout(layout2)
        layout1.addWidget(Color('pink'))
        layout1.addLayout(layout3)

        container = QWidget()
        container.setLayout(layout1)
        self.setCentralWidget(container)

app = QApplication()
window = MainWindow()
app.exec()