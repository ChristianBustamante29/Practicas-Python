import os
import shutil
import send2trash

ruta = 'C:\\Users\\chris\\Downloads\\Carpeta_superior'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')