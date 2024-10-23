nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','Mexico']

combinados = list(zip(nombres, edades, ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

    # capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
    # paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

    # combinados = list(zip(capitales,paises))

    # for capital,pais in combinados:
    #   print(f"La capital de {pais} es {capital}")

    espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
    portugues = ["um", "dois", "três", "quatro", "cinco"]
    ingles = ["one", "two", "three", "four", "five"]

    numeros = list(zip(espaniol, portugues, ingles))

    print(numeros)