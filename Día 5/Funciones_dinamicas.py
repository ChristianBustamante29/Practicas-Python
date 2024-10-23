'''def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras([555,99,600])

print(resultado)
'''

'''def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False
        else:
            continue
    return True

lista_numeros = [50,12,-40]

print(todos_positivos(lista_numeros))'''

'''def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n > 0 and n < 1000:
            suma += n
    return suma

lista_numeros = [55,100,999,20000]

print(suma_menores(lista_numeros))
'''

def cantidad_pares(lista_numeros):
    pares = 0
    for n in lista_numeros:
        if n % 2 == 0:
            pares += 1
    return pares

lista_numeros = [20,15,30,7]

print(cantidad_pares(lista_numeros))