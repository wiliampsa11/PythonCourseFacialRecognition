#Ejercicio 1 Condicional

n1 = int(input("Dame el primer número:"))
n2 = int(input("Dame el segundo número:"))

if n1%2 == 0 and n2%2 == 0:
    print("Ambos números son pares")
elif n1%2 == 0 and n2%2 != 0:
    print("El primer número es par")    
elif n1%2 != 0 and n2%2 == 0:
    print("El segundo número es par") 
else:
    print("Ambos números son impares")
