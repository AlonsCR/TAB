from Registro import Ui_Form

usuarios= {"diego":{"apellido":"Cervantes",
                   "nacimiento":"05/07/2003",
                   "correo":"cortes.alonso16@outlook.com","contrasena":1,"admin":"no"}}
x = Ui_Form()

def registrar(diccionario, clave, nombre, apellido,nacimiento, correo, contrasena, admin):
    diccionario[clave] = {"nombre": nombre, "apellido":apellido, "nacimiento":nacimiento,
                          "correo": correo, "contrasena":contrasena, "admin":admin}
    usuarios.update(x.finalizar())

def consultar():
    from ventana2 import Ui_Login2
    c = Ui_Login2()
    d= c.datos()
    usuario, contra = d

    if usuario in usuarios:
        if usuarios[usuario]["contrasena"] == contra:
            return True, usuario
        else:
            return "Contraseña incorrecta"

    else:
        return "Usuario no existe"