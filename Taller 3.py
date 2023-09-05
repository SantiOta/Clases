import os
os.system('cls')

# Ejercicio 1
print("Ejercicio 1")

def funcion1():
    print("Hola mundo")

funcion1()

os.system('pause')
os.system('cls')

# Ejercicio 2
print("Ejercicio 2")

def funcion2(nombre):
    print("Hola " + nombre)
    
nombre = input("Ingrese su nombre: ")
funcion2(nombre)

os.system('pause')
os.system('cls')

# Ejercicio 3
print("Ejercicio 3")

def funcion3():
    nombre = input("Cual es su nombre: ")
    edad = input("Cual es su edad: ")
    print("Su nombre es" , nombre , "y su edad es" , edad , "años")
    
funcion3()

os.system('pause')
os.system('cls')

# Ejercicio 4
print("Ejercicio 4")

def funcion4():
    cantidad = int(input("Cuantos numeros desea ingresar: "))
    numeros = []
    for i in range(cantidad):
        numero = input("Ingrese el numero: ")
        numeros.append(numero)
        
    suma = 0
    resta = 0
    multiplicacion = 1
    division = 1

    for numero in numeros:
        suma += float(numero)
        resta -= float(numero)
        multiplicacion *= float(numero)
        if numero != 0:
            division /= float(numero)
        else:
            print("No se puede dividir por cero.")
    
    print("Suma: ", suma)
    print("Resta: ", resta)
    print("Multiplicación: ", multiplicacion)
    print("División: ", division)
    
funcion4()

os.system('pause')
os.system('cls')