'''def potencia(num1, num2):
    return num1 ** num2


p = potencia(10, 2)

print(p)
'''

'''def usd_a_eur(monto):
    return monto * 0.90


dolares = usd_a_eur(10)

print(dolares)'''

def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra

palabra = invertir_palabra('Python')


print(palabra)