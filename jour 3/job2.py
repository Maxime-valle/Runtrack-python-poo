class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    # Méthodes
    def afficher(self):
        print(f"Compte n°{self.__numero_compte} : {self.__nom} {self.__prenom}, Solde : {self.__solde}")

    def afficherSolde(self):
        print(f"Solde : {self.__solde}")

    def versement(self, montant):
        self.__solde += montant

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
        else:
            print("Erreur : Solde insuffisant.")

    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.05  

    def virement(self, compte, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte.versement(montant)
            print("Virement effectué avec succès.")
        else:
            print("Erreur : Solde insuffisant pour effectuer le virement.")


#  objets CompteBancaire
compte1 = CompteBancaire("123456", "stravicki", "Jean", 1000)
compte2 = CompteBancaire("789101", "logvik", "Marie", -50, True)

compte1.afficher()
compte1.afficherSolde()
compte1.versement(500)
compte1.retrait(200)
compte1.afficherSolde()

compte2.afficher()
compte2.afficherSolde()
compte2.agios()
compte2.afficherSolde()

# Virement du compte1 vers le compte2 pour remettre le compte2 à zéro
compte1.virement(compte2, 50)
compte1.afficherSolde()
compte2.afficherSolde()