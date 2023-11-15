import autenticacion
import database

#Creacion de usuarios
def crear_usuario(username, password):
    password_hashed = autenticacion.hash_password(password)
    database.cursor.execute('INSERT INTO usuario (Usuario, Password) VALUES (?, ?)', (username, password_hashed))
    database.conn.commit()
   