class Rectangle:
    def __init__(self, longueur=1, largeur=1):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    # Assesseurs
    @property
    def longueur(self):
        return self.__longueur

    @property
    def largeur(self):
        return self.__largeur

    # Mutateurs
    @longueur.setter
    def longueur(self, longueur):
        self.__longueur = longueur

    @largeur.setter
    def largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

rectangle = Rectangle(5, 4)
parallelepipede=Parallelepipede(5,4,8)
print(f"Périmètre du rectangle : {rectangle.perimetre()}")
print(f"Surface du rectangle : {rectangle.surface()}")
print(f"volume du rectangle: {parallelepipede.volume()} ")
