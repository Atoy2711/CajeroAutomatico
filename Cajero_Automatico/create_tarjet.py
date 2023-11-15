import database

#Crear Tarjeta 
def crear_tarjeta(usuario_id, numero_tarjeta):
    database.cursor.execute('INSERT INTO tarjetas (usuario_id, numero_tarjeta, saldo) VALUES (?, ?, 0)', (usuario_id, numero_tarjeta))
    database.conn.commit()
    