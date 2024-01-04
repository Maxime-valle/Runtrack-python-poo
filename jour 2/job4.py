class Student:
    def __init__(self, nom, prenom, numero_etudiant, credits=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = self.__studentEval()

    # Assesseurs
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def get_credits(self):
        return self.__credits

    # Mutateur
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()  
            print("Erreur : Le nombre de crédits doit être un nombre positif.")

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom : {self.__nom}, Prénom : {self.__prenom}, Identifiant : {self.__numero_etudiant}, Niveau : {self.__level}")

john = Student("John", "Doe", 145)


john.add_credits(30)
john.add_credits(40)
john.add_credits(20)


print(f"Total de crédits : {john.get_credits()}")


john.studentInfo()