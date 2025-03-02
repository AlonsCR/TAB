
usuarios= {"diego":{"nombre":"diego","apellido":"Cervantes",
                   "nacimiento":"05/07/2003",
                   "correo":"cortes.alonso16@outlook.com","contraseña":"1","admin":"no"}}

def registrar(diccionario):
    usuarios.update(diccionario)

def consultar(usuario, contra):

    if usuario in usuarios:
        if usuarios[usuario]["contraseña"] == contra:
            return True
        else:
            return "Contraseña incorrecta"

    else:
        return "Usuario no existe"