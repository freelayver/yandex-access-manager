from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import users
import TOKEN

Form, Window = uic.loadUiType("untitled.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()







