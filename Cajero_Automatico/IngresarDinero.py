import database


def ingresar_cantidad_billetes():
    try:
        # Conecta a la base de datos (reemplaza con tu configuración)
        #conn = database.connect('cajero.db')
        #cursor = conn.cursor()

        cantidad_billetes = {}

        # Solicita al usuario la cantidad de cada denominación de billetes
        for denominacion in ['Billete de $100,000',
                            'Billete de $50,000',
                            'Billete de $20,000',
                            'Billete de $10,000',
                            'Billete de $5,000',
                            'Billete de $2,000',
                            'Billete de $1,000',
                            'Moneda de $1,000',
                            'Moneda de $500',
                            'Moneda de $200',
                            'Moneda de $100', 
                            'Moneda de $50']:
            cantidad_actual = database.cursor.execute('SELECT Cantidad FROM Dinero WHERE Nombre = ?', (denominacion,)).fetchone()[0]
            cantidad = int(input(f"Ingrese la cantidad de billetes de {denominacion}: "))
            
            # Suma la cantidad ingresada a la cantidad actual
            nueva_cantidad = cantidad_actual + cantidad

            # Verifica que la cantidad total no supere 200
            if nueva_cantidad > 200:
                print(f"La cantidad total de billetes de {denominacion} no puede superar 200.")
                continue

            cantidad_billetes[denominacion] = nueva_cantidad

            # Actualiza la base de datos con la nueva cantidad de billetes
            database.cursor.execute('UPDATE Dinero SET Cantidad = ? WHERE Nombre = ?', (nueva_cantidad, denominacion))
        # Guarda los cambios en la base de datos
        database.conn.commit()
        database.conn.close()

        print("Cantidad de billetes ingresada con exito.")

    except database.Error as e:
        print(f"Error al actualizar la cantidad de billetes en la base de datos: {str(e)}")




