import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = 'C:\\xampp\\htdocs\\cursos\\Python\\Día 9\\Proyecto dia 9\\Extraccion Terminada\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
ros_encontrados = []
archivos_encontrados = []


def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        for a in archivos:
            resultado = buscar_numero(Path(carpeta, a), mi_patron)
            if resultado != '':
                ros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO.SERIE')
    print('-------\t\t\t---------')
    for a in archivos_encontrados:
        print(f'{a}\t{ros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Números encontrados: {len(ros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la busqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)



crear_listas()
mostrar_todo()
