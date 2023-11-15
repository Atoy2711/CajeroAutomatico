import database

def realizar_retiro(usuario_id, tipo_cuenta, monto):
    # 1. Verificar que el monto sea un múltiplo de 10,000
    if monto % 10000 != 0:
        print("El cajero solo entrega múltiplos de 10,000.")
        return None

    # 2. Obtener el saldo actual de la cuenta
    if tipo_cuenta == "ahorro":
        database.cursor.execute('SELECT saldo_ahorro FROM usuarios WHERE id=?', (usuario_id,))
    else:
        database.cursor.execute('SELECT saldo_corriente FROM usuarios WHERE id=?', (usuario_id,))
    saldo = database.cursor.fetchone()[0]

    # 3. Verificar que haya suficiente saldo en la cuenta
    if saldo < monto:
        print("Saldo insuficiente.")
        return None

    # 4. Realizar el retiro y actualizar el saldo
    nuevo_saldo = saldo - monto
    if tipo_cuenta == "ahorro":
        database.cursor.execute('UPDATE usuarios SET saldo_ahorro=? WHERE id=?', (nuevo_saldo, usuario_id))
    else:
        database.cursor.execute('UPDATE usuarios SET saldo_corriente=? WHERE id=?', (nuevo_saldo, usuario_id))
    
    # Registrar la transacción en la base de datos
    database.cursor.execute('INSERT INTO transacciones (usuario_id, tipo_transaccion, monto) VALUES (?, ?, ?)', (usuario_id, "retiro", monto))
    database.conn.commit()
    
    return monto

# Ejemplo de uso
#usuario_id = 1  # Reemplaza con el ID del usuario autenticado
#tipo_cuenta = "ahorro"  # Reemplaza con el tipo de cuenta del usuario (ahorro o corriente)
#monto_a_retirar = 20000  # Reemplaza con el monto a retirar
#retiro_exitoso = realizar_retiro(usuario_id, tipo_cuenta, monto_a_retirar)
#if retiro_exitoso is not None:
#    print(f"Retiro exitoso: ${retiro_exitoso:.2f}")