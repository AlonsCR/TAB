import sys
from PySide6.QtWidgets import *
from ventana1 import Ui_Login

class Ventana(QWidget, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Ventana()
    sys.exit(app.exec())




