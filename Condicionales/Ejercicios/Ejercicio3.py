#Ejercicio 3

nombre1 = str(input("Dame un nombre:"))
nombre2 = str(input("Confirma el nombre:"))

if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print(f"Los nombres {nombre1} y {nombre2} son iguales")
else:
    print(f"Los nombres {nombre1} y {nombre2} no son iguales")