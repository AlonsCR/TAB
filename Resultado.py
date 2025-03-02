from PySide6.QtCore import QMetaObject, QRect, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from Usuarios import usuarios

class Datos:
    def __init__(self):
        self.nombre_usuario = ""
        self.apellido_usuario = ""
        self.nacimiento_usuario = ""
        self.correo_usuario = ""
        self.contrasena_usuario = ""
        self.admin_usuario = ""

    def setDato(self, usuario):
        self.nombre_usuario = usuarios[usuario]["nombre"]
        self.apellido_usuario = usuarios[usuario]["apellido"]
        self.nacimiento_usuario = usuarios[usuario]["nacimiento"]
        self.correo_usuario = usuarios[usuario]["correo"]
        self.contrasena_usuario = usuarios[usuario]["contraseña"]
        self.admin_usuario = usuarios[usuario]["admin"]

class Ui_Form(object):

    def setupUi(self, Form, datos=None):
        Form.setObjectName("Form")
        Form.resize(600, 500)
        Form.setStyleSheet("background-color: black;")

        font_label = QFont()
        font_label.setFamilies(["Arial"])
        font_label.setPointSize(20)
        font_label.setBold(True)

        self.fondo = QLabel(Form)
        self.fondo.setGeometry(QRect(0, 0, 600, 500))
        self.fondo.setPixmap(QPixmap("3.jpg"))
        self.fondo.setScaledContents(True)
        self.fondo.lower()

        self.boton_ok = QPushButton(Form)
        self.boton_ok.setText("OK")
        self.boton_ok.setGeometry(QRect(250, 420, 100, 40))
        self.boton_ok.setFont(font_label)
        self.boton_ok.setStyleSheet("""
            background-color: #B0B0B0;  /* Gris claro */
            color: black;  /* Texto negro */
            border: none;
            border-radius: 20px;
            padding: 10px;
            font-size: 14px;
        """)
        self.boton_ok.clicked.connect(Form.close)

        font_value = QFont()
        font_value.setFamilies(["Arial"])
        font_value.setPointSize(20)

        labels = ["Nombre:", "Apellido:", "Nacimiento:", "Correo:", "Contraseña:", "Administrador:"]
        self.fields = []

        y_offset = 50
        for i, text in enumerate(labels):
            label = QLabel(Form)
            label.setText(text)
            label.setFont(font_label)
            label.setStyleSheet("color: black  ; background-color: transparent;")
            label.setGeometry(QRect(50, y_offset, 150, 30))

            field = QLabel(Form)
            field.setGeometry(QRect(200, y_offset, 320, 30))
            field.setFont(font_value)
            field.setStyleSheet("""
                background-color: rgba(255, 255, 255, 0.0); 
                border-radius: 15px;
                padding: 5px;
                color: black;
            """)
            self.fields.append(field)
            y_offset += 60

        self.datos = Datos()
        self.datos = datos

        self.nombre, self.apellido, self.nacim, self.correo, self.contra, self.admin = self.fields

        self.nombre.setText(self.datos.nombre_usuario)
        self.apellido.setText(self.datos.apellido_usuario)
        self.nacim.setText(self.datos.nacimiento_usuario)
        self.correo.setText(self.datos.correo_usuario)
        self.contra.setText(self.datos.contrasena_usuario)
        self.admin.setText(self.datos.admin_usuario)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle("Perfil de Usuario")