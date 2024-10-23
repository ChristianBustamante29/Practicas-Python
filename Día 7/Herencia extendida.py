'''class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
       super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro vuelva {metros} metros")

piolin = Pajaro(3, 'amarrillo', 60)

mi_animal = Animal(5, 'negro')

piolin.volar(100)'''

class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("Que tal")

class Hijo(Madre, Padre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.reir()
mi_nieto.hablar()

print(Nieto.__mro__)

'''''''''''
class Padre:

    def hablar(self):
        print("Hola que hace?")

    def hobby(self):
        return('Doctor')


class Hijo(Padre):
    def hobby(self):
        return('Juego videojuegos en mi tiempo libre')

hijo1 = Hijo()

print(hijo1.hobby())