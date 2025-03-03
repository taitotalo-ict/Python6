# from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QWidget,
    QLineEdit,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.show()


        label = QLabel()
        line_edit = QLineEdit()
        # line_edit.textChanged.connect(label.setText)
        line_edit.editingFinished.connect(self.change_label)
        self.label = label
        self.line_edit = line_edit
            
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def change_label(self):
        # print(new_text)
        self.label.setText(self.line_edit.text())


app = QApplication()    # Aina pitää luoda QApplication, mutta VAIN YKSI!!!!
window = MainWindow()      # Qt toimii ns. "widgetteillä". Jos widgettillä ei ole "vanhempia", se näyttää ikkunalta
app.exec()              # `exec` aloittaa se "Event loop"