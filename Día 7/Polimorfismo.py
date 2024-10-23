class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)


''''''''''
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

iterador = [palabra, lista, tupla]

for i in iterador:
    print(len(i))

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()
