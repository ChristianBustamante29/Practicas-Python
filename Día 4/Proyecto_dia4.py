from random import randint

intentos = 0
estimado = 0
numero = randint(1,100)

nombre = input("Hola, dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un numero entre 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cual es el numero?"))
    intentos += 1

    if estimado not in range(1,101):
        print("Tu numero no se encuentra en el rango que va de 1 a 100")

    if estimado < numero:
        print("Mi numero es mas alto")
    elif estimado > numero:
        print("Mi numero es mas bajo")
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break
if estimado != numero:
    print(f"Lo siento {nombre}, se han agotado los intentos. El numero secreto era {numero}")