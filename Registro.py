from PySide6.QtCore import (QCoreApplication, QDate, Qt, QMetaObject, QPropertyAnimation, QEasingCurve)
from PySide6.QtGui import QFont, QPixmap, QColor
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QLabel,
                               QLineEdit, QPushButton, QWidget, QGraphicsOpacityEffect)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(600, 500)

        font_label = QFont("Arial", 16, QFont.Weight.Bold)
        font_input = QFont("Arial", 14)

        # Fondo con animación de aparición
        self.fondo = QLabel(Form)
        self.fondo.setObjectName("fondo")
        self.fondo.setGeometry(0, 0, 600, 500)
        self.fondo.setPixmap(QPixmap(u"2.jpg"))
        self.fondo.setScaledContents(True)

        self.fondo_effect = QGraphicsOpacityEffect(self.fondo)
        self.fondo.setGraphicsEffect(self.fondo_effect)

        self.fondo_animation = QPropertyAnimation(self.fondo_effect, b"opacity")
        self.fondo_animation.setDuration(1000)
        self.fondo_animation.setStartValue(0)
        self.fondo_animation.setEndValue(1)
        self.fondo_animation.setEasingCurve(QEasingCurve.OutCubic)
        self.fondo_animation.start()

        label_x = 80
        input_x = 200
        row_height = 50

        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setGeometry(label_x, 50, 150, 30)
        self.label.setFont(font_label)
        self.Nombref = QLineEdit(Form)
        self.Nombref.setObjectName("Nombref")
        self.Nombref.setGeometry(input_x, 50, 250, 30)
        self.Nombref.setFont(font_input)
        self.Nombref.setStyleSheet("border-radius: 10px; padding: 5px;")

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(label_x, 50 + row_height, 150, 30)
        self.label_2.setFont(font_label)
        self.Nombref_2 = QLineEdit(Form)
        self.Nombref_2.setObjectName("Nombref_2")
        self.Nombref_2.setGeometry(input_x, 50 + row_height, 250, 30)
        self.Nombref_2.setFont(font_input)
        self.Nombref_2.setStyleSheet("border-radius: 10px; padding: 5px;")

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(label_x, 50 + 2 * row_height, 150, 30)
        self.label_3.setFont(font_label)
        self.nacimiento = QDateEdit(Form)
        self.nacimiento.setObjectName("nacimiento")
        self.nacimiento.setGeometry(input_x, 50 + 2 * row_height, 250, 30)
        self.nacimiento.setFont(font_input)
        self.nacimiento.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nacimiento.setCalendarPopup(True)
        self.nacimiento.setStyleSheet("border-radius: 10px; padding: 5px;")

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(label_x, 50 + 3 * row_height, 150, 30)
        self.label_4.setFont(font_label)
        self.Nombref_4 = QLineEdit(Form)
        self.Nombref_4.setObjectName("Nombref_4")
        self.Nombref_4.setGeometry(input_x, 50 + 3 * row_height, 250, 30)
        self.Nombref_4.setFont(font_input)
        self.Nombref_4.setStyleSheet("border-radius: 10px; padding: 5px;")

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(label_x, 50 + 4 * row_height, 150, 30)
        self.label_6.setFont(font_label)
        self.password = QLineEdit(Form)
        self.password.setObjectName("password")
        self.password.setGeometry(input_x, 50 + 4 * row_height, 250, 30)
        self.password.setFont(font_input)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("border-radius: 10px; padding: 5px;")

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(label_x, 50 + 5 * row_height, 150, 30)
        self.label_5.setFont(font_label)
        self.Adminbox = QCheckBox(Form)
        self.Adminbox.setObjectName("Adminbox")
        self.Adminbox.setGeometry(input_x, 50 + 5 * row_height, 30, 30)

        self.finalizar = QPushButton("Finalizar", Form)
        self.finalizar.setObjectName("finalizar")
        self.finalizar.setGeometry(200, 50 + 6 * row_height, 200, 40)
        self.finalizar.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.finalizar.setStyleSheet("background-color: black; color: white; border-radius: 10px;")
       # self.finalizar.clicked.connect(self.finalizar)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Registro", None))
        self.label.setText(QCoreApplication.translate("Form", "Nombre:"))
        self.label_2.setText(QCoreApplication.translate("Form", "Apellido:"))
        self.label_3.setText(QCoreApplication.translate("Form", "Nacimiento:"))
        self.label_4.setText(QCoreApplication.translate("Form", "Correo:"))
        self.label_5.setText(QCoreApplication.translate("Form", "Administrador:"))
        self.label_6.setText(QCoreApplication.translate("Form", "Contraseña:"))
        self.nacimiento.setDisplayFormat(QCoreApplication.translate("Form", "dd MMMM yyyy"))
