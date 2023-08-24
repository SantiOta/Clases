import os

os.system("cls")

# Ejercicio 1
#1. Escriba un programa que almacene (Input) en una Lista las materias que has cursado con sus respectivas notas Luego muestre la lista por consola mediante un ciclo se pueden poner las materias y notas que quiera el usario.

print("Ejercicio 1")
print("")

materias = []
notas = []
cantidad = int(input("Cuantas materias desea ingresar: "))
for i in range(cantidad):
    materia = input("Ingrese una materia: ")
    materias.append(materia)
    nota = input("Ingrese una nota: ")
    notas.append(nota)
    print("")  

for i in range(cantidad):
    print("Materia: ", materias[i])
    print("Nota: ", notas[i])
    print("")

print("")
os.system("pause")
os.system("cls")

# Ejercicio 2
#2. Escriba un programa que almacene personas (input), luego que le muestre por pantalla el mensaje de ‘Su nombre es ‘nombre’

print("Ejercicio 2")
print("")

personas = []
cantidad = int(input("Cuantas personas desea ingresar: "))
for i in range(cantidad):
    persona = input("Ingrese el nombre de una persona: ")
    personas.append(persona)
    print("")  

for i in range(cantidad):
    print("Su nombre es: ", personas[i])
    print("")

print("")
os.system("pause")
os.system("cls")

# Ejercicio 3
#3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y el valor en pesos a convertir. Luego muestre en consola el símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.

print("Ejercicio 3")
print("")

diccionario = {"Euro":"€", "Dollar":"$", "Yen":"¥"}
divisa = input("Ingrese una divisa: ")
pesos = float(input("Ingrese la cantidad de pesos a convertir: "))
print("")

if "€" in divisa:
    print("El valor en euros es: ", pesos * 0.00023)
elif "$" in divisa:
    print("El valor en dolares es: ", pesos * 0.00024)
elif "¥" in divisa:
    print("El valor en yenes es: ", pesos * 0.035)
else:
    print("La divisa no se encuentra en el diccionario")

print("")


os.system("pause")
os.system("cls")

# Ejercicio 4
#En una tupla coloque o ingrese (input) los siguientes valores: numeros enteros, decimales, string, colecciones luego muestre en la consola que tipo de datos o variable son los valores digitados.

print("Ejercicio 4")
print("")

tupla = ()
num = 0


num = int(input("Digite el número de datos que quiere ingresar: "))
for i in range(num):
    tupla += (input("Digite el dato: "),)

for i in range(num):
    print("El dato", tupla[i], "es de tipo:", end=" ")
    if tupla[i].isdigit():
        print("Entero")
    elif tupla[i].isalpha():
        print("String")
    else:
        print("Decimal")
    print("")
    
print("")
os.system("pause")
os.system("cls")
