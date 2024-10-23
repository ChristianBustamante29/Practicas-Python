def letras_unicas(word):
    mi_set = set()

    for letra in word:
        mi_set.add(letra)

    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista


palabra = ejercicio_2("Holaaaa")

print(palabra)