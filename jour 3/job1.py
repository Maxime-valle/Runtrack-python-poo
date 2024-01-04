class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    # Assesseurs (getters)
    def get_nom(self):
        return self.__nom

    def get_habitants(self):
        return self.__habitants

    # Mutateur (setter)
    def ajouter_habitant(self):
        self.__habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville.ajouter_habitant()

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

#  nombre d'habitants de chaque ville
print(f"Paris : {paris.get_habitants()} habitants")
print(f"Marseille : {marseille.get_habitants()} habitants")

maxime = Personne("maxime", 45, paris)
mytlourd = Personne("Mytlourd", 4, paris)
chloe = Personne("Chloé", 18, marseille)

#  nombre d'habitants de chaque ville après l'arrivée des nouvelles personnes
print(f"Paris : {paris.get_habitants()} habitants")
print(f"Marseille : {marseille.get_habitants()} habitants")