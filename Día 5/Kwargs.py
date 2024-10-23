'''def prueba(num1, num2, *args, **kwargs):

    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


prueba(15,50,200,100,300,400,x='uno',y='dos',z='tres')'''


'''def cantidad_atributos(**kwargs):
    cantidad = 0

    for clave, valor in kwargs.items():
        cantidad += 1

    return cantidad

resumen = cantidad_atributos(x='uno',y='dos',z='tres')

print(resumen)'''

'''
def lista_atributos(**kwargs):
    lista = []
    for key, value in kwargs.items():
        lista.append(value)

    return lista'''


def describir_persona(name, **kwargs):
    print(f"Características de {name}:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

describir_persona('María', color_ojos="azules", color_pelo="rubio")
