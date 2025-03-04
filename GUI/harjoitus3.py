from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QWidget,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from random import choice

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.show()

        COLORS = QColor.colorNames()
        start_color = choice(COLORS)

        label = QLabel()
        self.label = label
        label.setAutoFillBackground(True)
        # Tarran fontti
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        # label.setStyleSheet('font-size: 30px')
        # Tarran alignment
        label.setAlignment(Qt.AlignCenter)
        # Tarran aloitusväri
        self.update_label(start_color)

        combobox = QComboBox()
        # combobox.addItems(['red', 'green', 'blue'])
        combobox.addItems(COLORS)
        combobox.currentTextChanged.connect(self.update_label)
        combobox.setCurrentText(start_color)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(combobox)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_label(self, color):
        self.label.setText(color)
        # palette = self.label.palette()
        # palette.setColor(self.label.backgroundRole(), color)
        # # palette.setColor(QPalette.Window, QColor(color))
        # self.label.setPalette(palette)
        self.label.setStyleSheet(f'background-color: {color}')


app = QApplication()
window = MainWindow()
app.exec()     