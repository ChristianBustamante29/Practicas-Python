'''from collections import defaultdict

mi_dic = defaultdict(lambda: 'nada')

mi_dic['uno'] = 'verde'

print(mi_dic['dos'])
print(mi_dic['tres'])

print(mi_dic)'''

'''from collections import defaultdict

mi_diccionario = defaultdict(lambda: 'Valor no hallado')

mi_diccionario['edad'] = 44

print(mi_diccionario['tres'])'''

from collections import deque

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

lista_ciudades.appendleft('Durango')

print(lista_ciudades)