import getpass
import autenticacion
import Usuario
import IngresarDinero
import os
opcion = ""
def menu_principal():
    print("Bienvenido al Cajero Automático Multifuncional")

    while True:
        opcion = input("""
Cajero Automático

1. Iniciar sesión
2. Crear usuario
3. Salir
Seleccione una opción: """)

        if opcion == "1":
            user = autenticacion.autenticar_usuario()
            if user == 'camilo':   
                while True:
                    os.system("cls")
                    print(f"!!!Bienvenido {user}, Que deseas realizar hoy!!")
                        
                    opcion = input("""
Cajero Automático

1. Ingresar Dinero al Cajero
2. Imprimir Informe Diario
3. Salir

Seleccione una opción: """)
                    match opcion:
                        case '1':
                            IngresarDinero.ingresar_cantidad_billetes()
                            os.system('pause')
                        case '2':
                            pass #funcion de imprimir informe diario
                        case '3':
                            os.system("cls")
                            print("Gracias por utilizar el Cajero Automático Multifuncional. ¡Hasta luego!")
                            break
                        case _:
                            os.system("cls")
                            print("Opcion fallida. Intente nuevamente.")
                            continue
            else:    
                os.system("cls")
                print(f"!!!Bienvenido {user}, Que deseas realizar hoy!!")
                
                while True:
                    opcion = input("""
Cajero Automático

1. Retirar Dinero
2. Consignar Dinero
3. Giros Nacionales o Internacionales
4. Pagar Recibo
5. Ver Saldo
6. Salir

Seleccione una opción: """)
                    match opcion:
                        case '1':
                            while True:
                                subopcion = input("""
Realizar Retiro de Cuenta

1. Ahorros
2. Corriente
3. Cancelar Operación

Seleccione una opción: """)
                                match subopcion:
                                    case '1':
                                        pass #Retiro de cuenta Ahorros
                                    case '2':
                                        pass #Retiro de cuenta Corriente
                                    case '3':
                                        print("operacion Cancelada. ¡Hasta luego!")
                                        break
                                    case _:
                                        os.system("cls")
                                        print("Opcion Incorrecta. Intente nuevamente.")
                                        
                                    
                        case '2':
                            pass #funcion de imprimir informe diario
                        case '3':
                            pass
                        case '4':
                            pass #funcion de imprimir informe diario
                        case '5':
                            pass #funcion de imprimir informe diario
                        case '6':
                            print("Gracias por utilizar el Cajero Automático Multifuncional. ¡Hasta luego!")
                            break
                        case _:
                            print("Autenticación fallida. Intente nuevamente.")
                        
            
        elif opcion == "2":
            os.system("cls")
            username = input("Ingrese un nombre de usuario: ")
            password = getpass.getpass("Ingrese su contraseña: ")
            Usuario.crear_usuario(username, password)
            print("Usuario creado exitosamente.")
            print("Crear cuenta.")
            #cuenta = int(input("Ingrese el numero de cuenta: "))
            #tipocuenta = input("Ingrese el tipo de cuenta ahorro/corriente: ")
            #create_user.crear_cuenta(cuenta,tipocuenta)
            

        elif opcion == "3":
            os.system("cls")
            print("Gracias por utilizar el Cajero Automático Multifuncional. ¡Hasta luego!")
            break


if __name__ == "__main__":
    menu_principal()