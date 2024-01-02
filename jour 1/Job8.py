import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon = rayon

    def afficherInfos(self):
        return f"Rayon: {self.rayon}, Circonférence: {self.circonference()}, Diamètre: {self.diametre()}, Aire: {self.aire()}"

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon

# Création de deux cercles
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations pour chaque cercle
print("Cercle 1 :", cercle1.afficherInfos())
print("Cercle 2 :", cercle2.afficherInfos())