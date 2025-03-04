# from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
    QDialog,
    QDialogButtonBox,
)

### Button types:
# QDialogButtonBox.Ok
# QDialogButtonBox.Open
# QDialogButtonBox.Save
# QDialogButtonBox.Cancel
# QDialogButtonBox.Close
# QDialogButtonBox.Discard
# QDialogButtonBox.Apply
# QDialogButtonBox.Reset
# QDialogButtonBox.RestoreDefaults
# QDialogButtonBox.Help
# QDialogButtonBox.SaveAll
# QDialogButtonBox.Yes
# QDialogButtonBox.YesToAll
# QDialogButtonBox.No
# QDialogButtonBox.NoToAll
# QDialogButtonBox.Abort
# QDialogButtonBox.Retry
# QDialogButtonBox.Ignore
# QDialogButtonBox.NoButton

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Are you sure?')

        buttons = QDialogButtonBox.Yes | QDialogButtonBox.No
        buttonbox = QDialogButtonBox(buttons)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(buttonbox)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.show()

        label = QLabel('Push the button to do something')
        button = QPushButton('Open dialog')
        button.clicked.connect(self.open_dialog)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_dialog(self):
        dlg = CustomDialog()
        result = dlg.exec()
        print(result)

app = QApplication()    # Aina pitää luoda QApplication, mutta VAIN YKSI!!!!
window = MainWindow()      # Qt toimii ns. "widgetteillä". Jos widgettillä ei ole "vanhempia", se näyttää ikkunalta
app.exec()              # `exec` aloittaa se "Event loop"