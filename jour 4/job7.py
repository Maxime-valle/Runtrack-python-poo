import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = [Carte(valeur, couleur) for valeur in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] for couleur in ['Coeur', 'Carreau', 'Trefle', 'Pique']]
        random.shuffle(self.paquet)

    def valeur_carte(self, carte):
        if carte.valeur in ['J', 'Q', 'K']:
            return 10
        elif carte.valeur == 'A':
            return 11
        else:
            return int(carte.valeur)

    def ajuster_pour_as(self, main):
        total = 0
        for carte in main:
            if carte.valeur == 'A' and total + 11 > 21:
                total += 1
            else:
                total += self.valeur_carte(carte)
        return total

    def afficher_main(self, main):
        return ', '.join(f"{carte.valeur} de {carte.couleur}" for carte in main)

    def jouer(self):
        main_joueur = [self.paquet.pop(), self.paquet.pop()]
        main_croupier = [self.paquet.pop(), self.paquet.pop()]

        print(f"Votre main : {self.afficher_main(main_joueur)}")
        print(f"Main du croupier : {self.afficher_main(main_croupier)}")

        while self.ajuster_pour_as(main_joueur) < 21:
            action = input("Voulez-vous prendre une autre carte ? (O/N) ")
            if action.lower() == 'o':
                main_joueur.append(self.paquet.pop())
                print(f"Votre main : {self.afficher_main(main_joueur)}")
            else:
                break

        while self.ajuster_pour_as(main_croupier) < 17:
            main_croupier.append(self.paquet.pop())

        score_joueur = self.ajuster_pour_as(main_joueur)
        score_croupier = self.ajuster_pour_as(main_croupier)

        print(f"Votre score final : {score_joueur}")
        print(f"Score final du croupier : {score_croupier}")

        if score_joueur > 21:
            print("Vous avez dépassé 21. Vous avez perdu.")
        elif score_croupier > 21 or score_joueur > score_croupier:
            print("Vous avez gagné !")
        else:
            print("Le croupier a gagné.")

jeu = Jeu()
jeu.jouer()