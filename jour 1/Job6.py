class Animal:
    def __init__(self):
        self.age = 15
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

animal = Animal()

#  l'âge de l'animal
print("Âge de l'animal :", animal.age)

#  vieillir l'animal
animal.vieillir()

#  l'âge de l'animal après avoir vieilli
print("Âge de l'animal après avoir vieilli :", animal.age)

#  l'animal
animal.nommer("Bobby")

# Affichage du nom de l'animal
print("Nom de l'animal :", animal.prenom)