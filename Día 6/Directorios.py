from pathlib import Path

carpeta = Path("C:/Users/chris/Downloads/Alternativo")
archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())