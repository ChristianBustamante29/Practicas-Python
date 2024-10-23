'''def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 10


print(mi_funcion())
print(mi_generador())

g = mi_generador()

print(next(g))
print(next(g))'''


'''def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x
'''

'''g = mi_generador()

print(next(g))
print(next(g))

print("hola mundo")

print(next(g))

'''''''


def mi_generador():
    x = 0
    while True:
        x += 1
        yield x


generador = mi_generador()'''

''''''''


def mi_generador():
    x = 4
    while x > 2:
        x -= 1
        yield f"Te quedan {x} vidas"

    yield "Te queda 1 vida"
    yield "Game Over"


g = mi_generador()

print(next(g))
print(next(g))
print(next(g))
print(next(g))

