import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('cajero.db')
cursor = conn.cursor()

# Crear tablas usuarios
cursor.execute('''
    
CREATE TABLE IF NOT EXISTS Usuario (
    Id INT PRIMARY KEY,
    Nombre VARCHAR(255),
    Usuario VARCHAR(50),
    Password VARCHAR(50),
    Identificacion VARCHAR(20),
    TipoIdentificacion VARCHAR(20),
    TipoUsuario VARCHAR(50),
    IdCuenta INT,
    IdTarjeta INT,
    FOREIGN KEY (IdCuenta) REFERENCES Cuenta(Id),
    FOREIGN KEY (IdTarjeta) REFERENCES Tarjeta(Id)
)
''')
#Creación de la tabla Cuenta
cursor.execute('''
CREATE TABLE IF NOT EXISTS Cuenta (
    Id INT PRIMARY KEY,
    NumeroCuenta VARCHAR(20),
    saldo_ahorro DECIMAL(10, 2), 
    saldo_corriente DECIMAL(10, 2)
)
''')
#Creación de la tabla Tarjeta
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tarjeta (
    Id INT PRIMARY KEY,
    NumeroTarjeta VARCHAR(16),
    Cupo DECIMAL(10, 2),
    Retiro DECIMAL(10, 2),
    IdEstado INT,
    FOREIGN KEY (IdEstado) REFERENCES Estado(Id)
)
''')

#Creación de la tabla Estado
cursor.execute('''
CREATE TABLE IF NOT EXISTS Estado (
    Id INT PRIMARY KEY,
    Nombre VARCHAR(50)
)
''')

#Creación de la tabla Dinero
cursor.execute('''
CREATE TABLE IF NOT EXISTS Dinero (
    Id INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Denominacion DECIMAL(10, 2),
    Cantidad INT
)
''')

#Creación de la tabla Transaccion
cursor.execute('''
CREATE TABLE IF NOT EXISTS Transaccion (
    Id INT PRIMARY KEY,
    Usuario INT,
    Identificacion VARCHAR(20),
    FechaTransaccion DATE,
    Cuenta INT,
    Valor DECIMAL(10, 2),
    Tarjeta INT,
    Detalle VARCHAR(255),
    TipoTransaccion INT,
    FOREIGN KEY (Usuario) REFERENCES Usuario(Id),
    FOREIGN KEY (Cuenta) REFERENCES Cuenta(Id),
    FOREIGN KEY (Tarjeta) REFERENCES Tarjeta(Id),
    FOREIGN KEY (TipoTransaccion) REFERENCES TipoTransaccion(Id)
)
''')
#Creación de la tabla TipoTransaccion
cursor.execute('''
CREATE TABLE IF NOT EXISTS TipoTransaccion (
    Id INT PRIMARY KEY,
    Transaccion VARCHAR(50)
)
''')
#Creación de la tabla ServiciosPublicos
cursor.execute('''
CREATE TABLE IF NOT EXISTS ServiciosPublicos (
    Id INT PRIMARY KEY,
    NumeroRecibo VARCHAR(20),
    Nombre VARCHAR(50),
    Valor DECIMAL(10, 2),
    TipoPago VARCHAR(50)
)
''')
#Creación de la tabla TipoCuenta
cursor.execute('''
CREATE TABLE IF NOT EXISTS TipoCuenta (
    Id INT PRIMARY KEY,
    Nombre VARCHAR(50)
)

''')

conn.commit()