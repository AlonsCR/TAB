from Usuarios import consultar
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)
from Registro import Ui_Form
class Ui_Login2(object):
    def setupUi2(self, Login):
        self.usuariob = QLineEdit(Login)
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(691, 501)
        self.fondo = QLabel(Login)
        self.fondo.setObjectName(u"fondo")
        self.fondo.setGeometry(QRect(0, 0, 691, 501))
        self.fondo.setPixmap(QPixmap(u"fabrizio-conti-m5fHSKYSflI-unsplash.jpg"))
        self.fondo.setScaledContents(True)

        self.resultado = QLabel(Login)
        self.resultado.setObjectName(u"resultado")
        self.resultado.setGeometry(QRect(310, 210, 200, 21))
        self.resultado.hide()

        self.UsuarioL = QLabel(Login)
        self.UsuarioL.setObjectName(u"UsuarioL")
        self.UsuarioL.setGeometry(QRect(240, 90, 58, 16))
        self.contrasenal = QLabel(Login)
        self.contrasenal.setObjectName(u"contrasenal")
        self.contrasenal.setGeometry(QRect(217, 120, 81, 20))
        self.usuariob = QLineEdit(Login)
        self.usuariob.setObjectName(u"usuariob")
        self.usuariob.setGeometry(QRect(310, 90, 113, 21))
        self.contrab = QLineEdit(Login)
        self.contrab.setObjectName(u"contrab")
        self.contrab.setGeometry(QRect(310, 120, 113, 21))
        self.contrab.setEchoMode(QLineEdit.EchoMode.Password)
        self.Registro = QPushButton(Login)
        self.Registro.setObjectName(u"Registro")
        self.Registro.setGeometry(QRect(220, 170, 100, 32))
        self.Registro.clicked.connect(self.registro)

        self.Inicio = QPushButton(Login)
        self.Inicio.setObjectName(u"Inicio")
        self.Inicio.setGeometry(QRect(360, 170, 100, 32))
        self.radioButton = QRadioButton(Login)
        self.Inicio.clicked.connect(self.inicio)

        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(430, 120, 20, 20))
        self.radioButton.toggled.connect(self.mostrar_p)

        self.retranslateUi(Login)

        self.Inicio.setDefault(True)

        QMetaObject.connectSlotsByName(Login)

    def registro(self):
        self.ventana = QWidget()
        self.nuevo = Ui_Form()
        self.nuevo.setupUi(self.ventana)
        self.ventana.show()

    def mostrar_p(self, clicked):
        if clicked:
            self.contrab.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.contrab.setEchoMode(QLineEdit.EchoMode.Password)

    def inicio(self):
        x = self.usuariob.text()
        y = self.contrab.text()
        resultado = consultar(x, y)

        if resultado is True:
            from Resultado import Datos
            c = Datos()
            c.setDato(x)
            self.resultado.hide()
            self.resultados()
        else:
            self.resultado.setText(resultado)
            self.resultado.setStyleSheet("color: red; font-weight: bold; font-size: 14px;")
            self.resultado.show()

    def resultados(self):
        from Resultado import Ui_Form as u3
        from Resultado import Datos

        self.ventana = QWidget()
        self.nuevo = u3()

        datos = Datos()
        datos.setDato(self.usuariob.text())

        self.nuevo.setupUi(self.ventana, datos)
        self.ventana.show()

    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.fondo.setText("")
        self.UsuarioL.setText(QCoreApplication.translate("Login", u"Usuario:", None))
        self.contrasenal.setText(QCoreApplication.translate("Login", u"Contrase\u00f1a:", None))
        self.Registro.setText(QCoreApplication.translate("Login", u"Registro", None))
        self.Inicio.setText(QCoreApplication.translate("Login", u"OK", None))
        self.radioButton.setText("")
    # retranslateUi

