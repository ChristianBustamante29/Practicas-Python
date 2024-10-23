from pathlib import Path, PureWindowsPath

carpeta = Path("C:/xampp/htdocs/cursos/Python/Día 6/prueba.txt")

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)