'''from random import *


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    return (dado1, dado2)


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados < 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


dado1,dado2 = lanzar_dados()
message = evaluar_jugada(dado1,dado2)

print(message)
'''
'''
lista_numeros = [1, 2, 15, 7, 2]


def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista

def promedio(lista):
    valor_medio = sum(lista)/len(lista)
    return valor_medio

reducir = reducir_lista(lista_numeros)

print(reducir)
promedioo = promedio(reducir)

print(promedioo)'''

from random import *

lista_numeros = [1, 4, 1, 4, 65, 23]


def lanzar_moneda():
    monedas = ['Cara', 'Cruz']
    eleccion = choice(monedas)
    return eleccion


def probar_suerte(moneda, lista):
    if moneda == 'Cara':
        print("La lista se autodestruira")
        return []
    else:
        print("La lista fue salvada")
        return lista

dado_lanzado = lanzar_moneda()

resultado = probar_suerte(dado_lanzado,lista_numeros)

print(resultado)