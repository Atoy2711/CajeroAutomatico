import hashlib
import database
import menu
import getpass
import os

#Variable Global para conteo de rrores de inicio de sesion
#cont = 3
# Encriptar la contraseña antes de almacenarla
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#autenticacion de contraseña
def autenticar_usuario():
    cont = 3
    
    while cont > 0:
        
        username = input("Ingrese su nombre de usuario: ")
        password = getpass.getpass("Ingrese su contraseña: ")
        
        # Realiza la consulta SQL para obtener el usuario y la contraseña de la base de datos
        database.cursor.execute('SELECT Usuario, Password FROM usuario WHERE Usuario=?', (username, ))
        result = database.cursor.fetchone()
        print(result)
        if result:
            user_id, stored_password = result
            if stored_password == hash_password(password):
                return user_id
            else:
                cont -= 1
                os.system("cls")
                print(f"Contraseña Incorrecta, Intenta nuevamente. Intentos restantes: {cont}")
        else:
            os.system("cls")
            print("Usuario no encontrado.")
            cont -= 1

    print("Intentos agotados, cuenta bloqueada.")
    os.system("pause")
    os.system("cls")
    menu.menu_principal()
    return None

#def validar_tipo_úsuario():
#    database.cursor.execute(f'SELECT Usuario, TipoUsuario FROM usuario WHERE {}')