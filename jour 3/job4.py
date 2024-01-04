class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            print(f"{joueur.nom} : Buts - {joueur.buts}, Passes - {joueur.passes}, Cartons jaunes - {joueur.cartons_jaunes}, Cartons rouges - {joueur.cartons_rouges}")

#  joueurs
joueur1 = Joueur("tiakola", 7, "Attaquant")
joueur2 = Joueur("cisoco", 6, "Milieu")
joueur3 = Joueur("maitreO", 4, "Défenseur")
joueur4 = Joueur("zozo", 3, "Attaquant")
joueur5 = Joueur("soco", 6, "Milieu")
joueur6 = Joueur("maitrez", 4, "Défenseur")
joueur7 = Joueur("lolo", 8, "Attaquant")
joueur8 = Joueur("mortadans",2, "Milieu")
joueur9 = Joueur("firbal",5, "Défenseur")
joueur10 = Joueur("lozo", 6, "Milieu")
joueur11 = Joueur("ratoune", 4, "Défenseur")

# équipe
equipe = Equipe("France")

# Ajout des joueurs à l'équipe
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe.ajouterJoueur(joueur3)

# statistiques des joueurs
equipe.afficherStatistiquesJoueurs()

# Simulation  match
joueur1.buts += 2
joueur1.passes += 4
joueur2.cartons_jaunes += 1
joueur3.cartons_rouges += 1
joueur8.buts += 4
joueur5.passes += 5
joueur10.cartons_jaunes += 0
joueur11.cartons_rouges += 1

equipe.afficherStatistiquesJoueurs()



























