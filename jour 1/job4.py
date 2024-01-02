class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}"
    
personne1 = Personne("granods", "Lolo")
personne2 = Personne("irris", "Max")

print(personne1.SePresenter())
print(personne2.SePresenter())
