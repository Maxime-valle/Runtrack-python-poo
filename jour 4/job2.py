class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print('bonjour')

    def modifierAge(self, newAge):
        self.age = newAge


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self._matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


eleve = Eleve()
professeur = Professeur("Mathématiques", 40)

eleve.bonjour()
eleve.allerEnCours()

eleve.modifierAge(15)

professeur.bonjour()
professeur.enseigner()