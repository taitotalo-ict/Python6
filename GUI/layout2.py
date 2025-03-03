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
        widget = Color('green')
        self.setCentralWidget(widget)

app = QApplication()
window = MainWindow()
app.exec()