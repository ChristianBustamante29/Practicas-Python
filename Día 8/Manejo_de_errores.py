'''def suma():
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar" + n1)



try:
    suma()
except TypeError:
    print("Estas intenando concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")'''

def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break

    print("Gracias")

pedir_numero()


''''
def cociente(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")

'''


def abrir_archivo(nombre_archivo):
    try:
        open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")