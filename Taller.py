import os
os.system('cls')

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
    
if edad > 0 and edad < 15:
    print("Usted es un niño")
elif edad >= 15 and edad < 18:
    print("Usted es adolescente")
elif edad >= 18 and edad < 60:
    print("Usted es adulto")
else:    
    print("Usted es un adulto mayor")
    

os.system('pause') 
os.system('cls')