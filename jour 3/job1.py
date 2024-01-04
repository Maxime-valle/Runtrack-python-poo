class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    # Assesseurs
    def get_numero_commande(self):
        return self.__numero_commande

    def get_plats_commandes(self):
        return self.__plats_commandes

    def get_statut_commande(self):
        return self.__statut_commande

    # Mutateurs 
    def ajouter_plat(self, nom_plat, prix):
        self.__plats_commandes[nom_plat] = prix

    def annuler_commande(self):
        self.__statut_commande = "annulée"

    def __calculer_total(self):
        return sum(self.__plats_commandes.values())

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande} : {self.__plats_commandes}")
        print(f"Total à payer : {self.__calculer_total()}")

    def calculer_TVA(self, taux_TVA):
        return self.__calculer_total() * taux_TVA / 100