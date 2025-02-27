
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)
from ventana2 import Ui_Login2

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(691, 502)
        self.Boton1 = QPushButton(Login)
        self.Boton1.setObjectName(u"Boton1")
        self.Boton1.setGeometry(QRect(160, 180, 311, 111))
        self.Boton1.clicked.connect(self.iniciar)

        font = QFont()
        font.setFamilies([u"Baskerville"])
        font.setPointSize(51)

        self.Boton1.setFont(font)
        self.fondo = QLabel(Login)
        self.fondo.setObjectName(u"fondo")
        self.fondo.setGeometry(QRect(0, 0, 791, 511))
        self.fondo.setPixmap(QPixmap(u"fabrizio-conti-m5fHSKYSflI-unsplash.jpg"))
        self.fondo.setScaledContents(True)
        self.fondo.raise_()
        self.Boton1.raise_()

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)

    def iniciar(self):
        self.ventana =  QWidget()
        self.nuevo = Ui_Login2()
        self.nuevo.setupUi2(self.ventana)
        self.ventana.show()
        self.close()

    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Inicio", None))
        self.Boton1.setText(QCoreApplication.translate("Login", u"Iniciar sesion", None))
        self.fondo.setText("")
    # retranslateUi

