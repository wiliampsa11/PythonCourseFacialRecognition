#While
import math #serve tbm para ter raizes quadradas
numero= int(input("Escriba un numero: "))

while numero<0:
    print("Porfavor ingrese un numero positivo")
    numero= int(input("Escriba un numero positivo: "))
print(f"El resultado de la raiz cuadrada es {math.sqrt(numero):.2f}")