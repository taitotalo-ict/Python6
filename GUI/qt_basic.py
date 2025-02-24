# Basic PySide6 app
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication()    # Aina pitää luoda QApplication, mutta VAIN YKSI!!!!

window = QWidget()      # Qt toimii ns. "widgetteillä". Jos widgettillä ei ole "vanhempia", se näyttää ikkunalta
window.show()           # Ikkunat ovat piilotettu oletuksena. Pitää näyttää niitä aktiivisesti

app.exec()              # `exec` aloittaa se "Event loop"