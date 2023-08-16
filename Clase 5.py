import os
os.system('cls')
#1. Escriba un programa que almacene la cadena de caracteres contraseña en una variable, para luego preguntarle al usuario por la contraseña. Luego, imprima en la consola si la contraseña que el usuario ingreso coincide con la guardada en variable.

contraseña = "12345"
contraseña_usuario = input("Ingrese la contraseña: ")
if contraseña == contraseña_usuario:
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")

os.system('pause') 
os.system('cls')

#2. Realice un programa que le pida al usuario dos números por teclado y muestre por consola su división. Si el divisor es cero el programa debe mostrar un error y solicitar nuevamente el numero.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
if numero2 == 0:
    print("Error, el divisor no puede ser 0")
    numero2 = int(input("Ingrese el segundo numero: "))
else:
    print("La division es: ", numero1 / numero2)

os.system('pause') 
os.system('cls')

#3. Escriba un programa que le pida al usuario por teclado un numero entero y muestre en consola si es par o impar.

numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

os.system('pause') 
os.system('cls')

#4. Escriba que mediante un vector  de 5 item, lea cada item y evalué el ingreso a menores de edad, si la persona tiene menos de 19 años el programa le debe mostrar en pantalla que ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!

ingresos = [0, 0, 0, 0, 0]
for i in range(0, 5):
    ingresos[i] = int(input("Ingrese su edad: "))
    if ingresos[i] < 18:
        print("No puede ingresar")

    else:
        print("Bienvenido")
        
os.system('pause') 
os.system('cls')