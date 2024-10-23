from os import system

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system('cls')

print(f"Tu nombre es {nombre} y tienes {edad} años")
'''''''


def abrir_leer(texto):
    file = open(texto, 'r')
    return file.read()


print(abrir_leer("ejemplo.txt"))
''''''''


def sobrescribir(texto):
    file = open(texto, '')
    file.write('contenido eliminado')
    file.close


sobrescribir("ejemplo.txt")