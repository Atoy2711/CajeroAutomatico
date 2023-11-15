import database

#Inserción de datos en la tabla Estado
database.cursor.execute('''
INSERT INTO Estado (Id, Nombre)
VALUES (1, 'Activo'),
       (2, 'Inactivo');
''')
#Inserción de datos en la tabla TipoCuenta
database.cursor.execute('''
INSERT INTO TipoCuenta (Id, Nombre)
VALUES (1, 'Cuenta de Ahorro'),
       (2, 'Cuenta Corriente');
''')
#Inserción de datos en la tabla Usuario
database.cursor.execute('''
INSERT INTO Usuario (Id, Nombre, Usuario, Password, Identificacion, TipoIdentificacion, TipoUsuario, IdCuenta, IdTarjeta)
VALUES (1, 'Administrador', 'Admin', 'admin', '123456789', 'Cédula','admin', 1, 1),
       (2, 'Usuario2', 'user2', 'password2', '987654321', 'Pasaporte','user', 2, 2);
''')
#Inserción de datos en la tabla Cuenta
database.cursor.execute('''
INSERT INTO Cuenta (Id, NumeroCuenta, saldo_ahorro, saldo_corriente)
VALUES (1, '12345', 0, 0),
       (2, '67890', 0, 0);
''')
#Inserción de datos en la tabla Tarjeta
database.cursor.execute('''
INSERT INTO Tarjeta (Id, NumeroTarjeta, Cupo, Retiro, IdEstado)
VALUES (1, '1111222233334444', 10000.00, 500.00, 1),
       (2, '5555666677778888', 20000.00, 1000.00, 1);
''')
#Inserción de datos en la tabla Dinero
database.cursor.execute('''
INSERT INTO Dinero (Id,Nombre, Denominacion,Cantidad)
VALUES
    (1,'Billete de $100,000', 100000.00,0),
    (2,'Billete de $50,000', 50000.00,0),
    (3,'Billete de $20,000', 20000.00,0),
    (4,'Billete de $10,000', 10000.00,0),
    (5,'Billete de $5,000', 5000.00,0),
    (6,'Billete de $2,000', 2000.00,0),
    (7,'Billete de $1,000', 1000.00,0),
    (8,'Moneda de $1,000', 1000.00,0),
    (9,'Moneda de $500', 500.00,0),
    (10,'Moneda de $200', 200.00,0),
    (11,'Moneda de $100', 100.00,0),
    (12,'Moneda de $50', 50.00,0)

''')
#Inserción de datos en la tabla TipoTransaccion
database.cursor.execute('''
INSERT INTO TipoTransaccion (Id, Transaccion)
VALUES (1, 'Depósito'),
       (2, 'Retiro');
''')
#Inserción de datos en la tabla Transaccion
database.cursor.execute('''
INSERT INTO Transaccion (Id, Usuario, Identificacion, FechaTransaccion, Cuenta, Valor, Tarjeta, Detalle, TipoTransaccion)
VALUES (1, 1, '123456789', '2023-10-21', 1, 500.00, 1, 'Depósito en efectivo', 1),
       (2, 2, '987654321', '2023-10-21', 2, 100.00, 2, 'Retiro en cajero', 2);
''')
#Inserción de datos en la tabla ServiciosPublicos
database.cursor.execute('''
INSERT INTO ServiciosPublicos (Id, NumeroRecibo, Nombre, Valor, TipoPago)
VALUES (1, '12345', 'Agua', 50.00, 'Pago en línea'),
       (2, '67890', 'Luz', 60.00, 'Pago en efectivo');
    
    ''')
