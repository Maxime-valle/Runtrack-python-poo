class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return f"Point: ({self.x}, {self.y})"

    def afficherX(self):
        return self.x

    def afficherY(self):
        return self.y

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y

point = Point(6, 3)

# Appel des méthodes
print(point.afficherLesPoints())
print("x:", point.afficherX())
print("y:", point.afficherY())

point.changerX(4)
point.changerY(7)

print("Après modification :")
print(point.afficherLesPoints())