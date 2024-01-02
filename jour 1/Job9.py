class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 125)

    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}, Prix TTC: {self.CalculerPrixTTC()}"

    def modifierNom(self, nom):
        self.nom = nom

    def modifierPrix(self, prixHT):
        self.prixHT = prixHT

    def retournerNom(self):
        return self.nom

    def retournerPrixHT(self):
        return self.prixHT

    def retournerTVA(self):
        return self.TVA

# Création produits
produit1 = Produit("Produit 1", 100, 20)
produit2 = Produit("Produit 2", 200, 40)

#  informations pour chaque produit
print(produit1.afficher())
print(produit2.afficher())

# nom et du prix de chaque produit
produit1.modifierNom("Produit 1 modifié")
produit1.modifierPrix(120)
produit2.modifierNom("Produit 2 modifié")
produit2.modifierPrix(220)

# nouveau prix des produits
print("Nouveau prix TTC de Produit 1 :", produit1.CalculerPrixTTC())
print("Nouveau prix TTC de Produit 2 :", produit2.CalculerPrixTTC())