#16/08/2023
#listas y sus elelmentos
import os
"""
os.system('cls')

lista =["hector", True, 23, 1.75]

lista.append("hola")
lista.insert(2, "hola")
q = 0


while q < len(lista):
    print(lista[q])
    q += 1

os.system('pause')
os.system('cls')
"""
#listas en listas

lista = [[1,2,3], [4,5,6], [7,8,9],]
print(lista[0][0])

for i in range(len(lista)):
    for j in range(len(lista[i])):
        print(lista[i][j], end=" ")
        
for z in lista:
    for x in z:
        print(x)
    print()

#tuplas
#presentacion tarea proxima clase