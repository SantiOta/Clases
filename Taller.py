import os
os.system('cls')

print("Bienvenido a la calculadora")
print("Ingrese los numeros que desea operar")
print("Ingrese 0 para terminar de ingresar numeros")
numeros = []
while True:
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        break
    else:
        numeros.append(numero)
print("Los numeros ingresados son: ", numeros)
print("Ingrese la operacion que desea realizar")
print("+ para sumar")
print("- para restar")
print("* para multiplicar")
print("/ para dividir")
operacion = input("Ingrese la operacion: ")
if operacion == "+":
    resultado = 0
    for numero in numeros:
        resultado += numero
    print("El resultado de la suma es: ", resultado)
elif operacion == "-":
    resultado = 0
    for numero in numeros:
        resultado -= numero
    print("El resultado de la resta es: ", resultado)
elif operacion == "*":
    resultado = 1
    for numero in numeros:
        resultado *= numero
    print("El resultado de la multiplicacion es: ", resultado)
elif operacion == "/":
    resultado = 1
    for numero in numeros:
        resultado /= numero
    print("El resultado de la division es: ", resultado)
else:
    print("Operacion no valida")
    

os.system('pause') 
os.system('cls')