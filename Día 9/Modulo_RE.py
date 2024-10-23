import re


'''texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas llama al servicio de ayuda online"

patron = 'ayuda'

#busqueda = re.search(patron, texto)
#busqueda = re.findall(patron, texto)

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
'''

#texto = "llama al 564-525-6548 ya mismo"

#patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

'''resultado = re.search(patron, texto)

print(resultado.group(1))'''

'''
clave = input("Clave: ")

patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)

print(chequear)'''

'''texto = "No atendemos los jueves por la tarde"

#buscar = re.search(r'lunes|martes', texto)

#buscar = re.search(r'...demos...', texto)

buscar = re.search(r'', texto)
print(buscar)'''

import re

import re


def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


import re


def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron, frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")


import re


def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")