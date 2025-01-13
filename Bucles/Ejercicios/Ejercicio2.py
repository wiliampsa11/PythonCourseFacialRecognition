#Conjuntos
A={1,2,3,4}
B={2,3,5,6}
C={3,4,6,7}

print(A|B) # | Soma os valores
print(A|C)
print(A&B)
print(A&C) # & Compara os valores iguais
print(A-B) # - Mostra os valores que não tem no outro
print(A-C)

print(A^C) # ^ Mostra os valores que estão nos dois conjuntos, mas não nos dois
print(A^B)