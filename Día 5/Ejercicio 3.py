def ceros_vecinos(*args):

    contador = 0

    for num in args:

        if contador + 1 == len(args):
            return False

        if args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

print(ceros_vecinos(0,4,0,2,3,2,1,1,1,4,0,))