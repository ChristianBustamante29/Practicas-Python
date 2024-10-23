nombre = input("¿Cuál es tu nombre?")

ventas = input("¿Cuanto vendiste?")

ventasfinales = float(ventas)

comision = (ventasfinales/100) * 13

comision_final = round(comision,2)

print(f"Ok {nombre}, este mes ganaste {comision_final}")

#profesor

nombre = input("Por favor dime tu nombre: ")
ventas = int(input("Diga sus ventas totales del mes: "))

comision = round(ventas * 13 / 100,2)


print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")