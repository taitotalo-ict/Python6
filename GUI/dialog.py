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
    QMessageBox,
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

        # Basic Message Dialog
        button2 = QPushButton('Show message')
        button2.clicked.connect(self.show_message)
        layout.addWidget(button2)

        # Question Message Dialog
        button3 = QPushButton('Show a Question message')
        button3.clicked.connect(self.question_message)
        layout.addWidget(button3)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_dialog(self):
        dlg = CustomDialog()
        result = dlg.exec()
        print(result)
    
    def show_message(self):
        dlg = QMessageBox(text='Action has been canceled!')
        # dlg.setText('Action has been canceled!')
        dlg.setText("The document has been modified.")
        dlg.setInformativeText("Do you want to save your changes?")
        dlg.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        dlg.setDefaultButton(QMessageBox.Save)
        result = dlg.exec()
        match result:
            case QMessageBox.Save: print('Save')
            case QMessageBox.Discard: print('Discard')
            case QMessageBox.Cancel: print('Cancel')

    def question_message(self):
        result = QMessageBox.question(
            self, 
            'My question',
            'Is Python the best programming language?'
            )
        print(result)

app = QApplication()    # Aina pitää luoda QApplication, mutta VAIN YKSI!!!!
window = MainWindow()      # Qt toimii ns. "widgetteillä". Jos widgettillä ei ole "vanhempia", se näyttää ikkunalta
app.exec()              # `exec` aloittaa se "Event loop"


# QMessageBox.Question:    The message is asking a question.
# QMessageBox.Information: The message is informational only.
# QMessageBox.Warning:     The message is warning.
# QMessageBox.Critical:    The message indicates a critical problem.