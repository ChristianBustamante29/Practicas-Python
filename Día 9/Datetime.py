'''import datetime

mi_dia = datetime.date(2025, 10, 17)

print(mi_dia.today())'''

'''from datetime import datetime

mi_fecha = datetime(2025, 5, 15, 22 ,10, 15, 2500)

mi_fecha = mi_fecha.replace(month= 5)

print(mi_fecha)'''

'''from datetime import date

nacimiento = date(1995, 3, 5)
defuncion = date(2095, 6, 19)

vida = defuncion - nacimiento

print(vida)'''

'''from datetime import datetime

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)
vigilia = duerme - despierta
print(vigilia.seconds)'''

'''import datetime

hoy = datetime.date(2024, 2, 2)
hoy = hoy.today()

print(hoy)'''

from datetime import datetime

minutos = datetime.now().minute