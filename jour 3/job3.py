class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.statut = "terminée"

    def afficherListe(self):
        for tache in self.taches:
            print(f"{tache.titre} : {tache.statut}")

    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]
    
liste = ListeDeTaches()

tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Rendre le rapport", "Rapport de projet à rendre pour vendredi")
tache3 = Tache("Réviser le cours", "Réviser le cours de mathématiques pour l'examen")


liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

#toutes les taches 
liste.afficherListe()

# tâche  terminée
liste.marquerCommeFinie(tache1)

# tâches à faire
print("Tâches à faire :")
for tache in liste.filterListe("à faire"):
    print(tache.titre)