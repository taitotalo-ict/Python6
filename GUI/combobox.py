# Basic PySide6 app
from PySide6.QtWidgets import QApplication, QComboBox

app = QApplication()

window = QComboBox()
window.addItems(['Option 1', 'Option 2', 'Option 3'])

window.show()

app.exec()