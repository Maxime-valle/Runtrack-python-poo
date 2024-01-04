class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        adversaire.vie -= 1


class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1-3) : "))

    def lancerJeu(self):
        vie = 10 * self.niveau
        self.joueur = Personnage("Joueur", vie)
        self.ennemi = Personnage("Ennemi", vie)

    def verifierSante(self, personnage):
        return personnage.vie > 0

    def verifierGagnant(self):
        if not self.verifierSante(self.joueur):
            return "L'ennemi a gagné."
        elif not self.verifierSante(self.ennemi):
            return "Le joueur a gagné."
        else:
            return "Le jeu continue."

    def jouerTour(self):
        self.joueur.attaquer(self.ennemi)
        if self.verifierSante(self.ennemi):
            self.ennemi.attaquer(self.joueur)


# Test du code
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()

while jeu.verifierSante(jeu.joueur) and jeu.verifierSante(jeu.ennemi):
    jeu.jouerTour()

print(jeu.verifierGagnant())