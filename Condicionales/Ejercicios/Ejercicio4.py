#Ejercicio 4

saldo = float(2000)

opcion = int(input(" 1. Depositar dinero \n 2. Retirar dinero \n 3. Consultar saldo \n 4. Salir \n Elija una opción: "))

if opcion == 1:
    deposito = float(input("Ingrese el monto a depositar: "))
    saldo += deposito
    print(f"Se ha depositado ${deposito}, su nuevo saldo es ${saldo}")
elif opcion == 2:
    retiro = float(input("Ingrese el monto a retirar: "))
    if retiro > saldo:
        print("No hay suficiente saldo.")
    else:
        saldo -= retiro
        print(f"Se ha retirado ${retiro}, su nuevo saldo es ${saldo}")
elif opcion == 3:
    print(f"Su saldo es ${saldo}")
elif opcion == 4:
    print("Gracias por usar nuestra app. Adiós.")
else:
    print("Opción no válida.")