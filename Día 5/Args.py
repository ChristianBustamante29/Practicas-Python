'''def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total


print(suma(5,6,1))'''


def numeros_persona(name, *args):
    suma_numeros = 0

    for arg in args:
        suma_numeros += arg

    return f"{name}, la suma de tus números es {suma_numeros}"

resultado = numeros_persona('juaco', 5,5,5)

print(resultado)