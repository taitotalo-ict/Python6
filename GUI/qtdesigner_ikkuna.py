from PySide6.QtWidgets import QApplication, QMainWindow
from ui_window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_2.clicked.connect(lambda: print('clicked!'))


app = QApplication()
window = MainWindow()
app.exec()