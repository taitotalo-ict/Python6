import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Simple Example")

        button = QPushButton("Click Me")
        button.clicked.connect(self.show_message)
        self.setCentralWidget(button)

    def show_message(self):
        msg_box = QMessageBox()
        msg_box.setText("Button Clicked!")
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())