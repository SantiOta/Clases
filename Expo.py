import os
os.system('cls')

tupla = (1, 2, 3, 4, 5)

print(tupla[2:])

os.system('pause') 
os.system('cls')


tupla = (1, 2, 3, 4, 5)
print(4 in tupla)

os.system('pause') 
os.system('cls')

# Empaquetado de tuplas
coordenadas = (10, 20)

# Desempaquetado de tuplas
x, y = coordenadas

# Imprimir los valores desempaquetados
print("Valor de x:", x)
print("Valor de y:", y)

print(type(coordenadas))
os.system('pause') 
os.system('cls')

# Función que devuelve una tupla
def obtener_coordenadas():
    return 30, 40

# Desempaquetado de los valores devueltos por la función
x2, y2 = obtener_coordenadas()


# Imprimir los valores desempaquetados
print("Valor de x2:", x2)
print("Valor de y2:", y2)

print(type(obtener_coordenadas()))

os.system('pause') 
os.system('cls')