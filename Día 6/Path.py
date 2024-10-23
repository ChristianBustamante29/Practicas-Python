from pathlib import Path

base = Path.home()
guia = Path(base,"Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))

print(guia.parent)
''''''''

from pathlib import Path

ruta_base = Path().home()

print(ruta_base)

''''''''
from pathlib import Path as p

ruta = p("Curso Python","Día 6","practicas_path.py")
print(ruta)
''''''''''''

from pathlib import Path

ruta = Path(Path.home(), "Curso Python","Día 6","practicas_path.py")