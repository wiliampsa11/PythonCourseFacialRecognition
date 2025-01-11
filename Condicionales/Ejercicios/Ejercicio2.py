#Ejercicio 2
n1 = int(input("Dame el primer número: "))
n2 = int(input("Dame el segundo número: "))
n3 = int(input("Dame el tercer número: "))

if n1 >= n2 and n1 >= n3:
    print(f"El primer número es el mayor {n1}")
elif n2 >= n1 and n2 >= n3:
    print(f"El segundo número es el mayor {n2}")
elif n3 >= n1 and n3 >= n2:
    print(f"El tercer número es el mayor {n3}")
