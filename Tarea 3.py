import os
os.system('cls')

#1. Escriba una función que muestre por consola un saludo personalizado. Por ejemplo ‘¡Hola mundo!’

def saludo():
    print("Hola mundo")
    return
saludo()



#2. Escriba una función que reciba un nombre por parámetro y que luego muestre en pantalla ¡Hola <nombre>!

def saludo2(nombre):
    print("Hola " + nombre )
    
nombre = input("Ingrese su nombre: ")  
saludo2(nombre)

os.system('pause')
os.system('cls')

#3. Cree una función que le pida al usuario su nombre y su edad, luego muestre en pantalla los resultados


def datos():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    print("Su nombre es " + nombre + " y su edad es " + edad + " años")

datos()

os.system('pause')
os.system('cls')

#4. Definir una función que reciba n cantidad de números por parámetros y que luego los sume, reste, mutiplique y divida.
def calculadora():

    entrada = input("Ingrese los numeros separados por comas: ")
    numeros = [float(numero) for numero in entrada.split(',')]
    
    suma = numeros[0]
    resta = numeros[0]
    multiplicacion = numeros[0]
    division = numeros[0]

    for numero in numeros[1:]:
        suma += numero
        resta -= numero
        multiplicacion *= numero
        if numero != 0:
            division /= numero
        else:
            print("No se puede dividir por cero.")

    print("Suma: ", suma)
    print("Resta: ", resta)
    print("Multiplicación: ", multiplicacion)
    print("División: ", division)
    
calculadora()

