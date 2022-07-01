##### Importation de bibliothèques #####

import random # bibliothèque pour générer les voeux aléatoirement

##### Définition des variables #####

nb_salles = int(input("nombre de salles disponibles : "));
nb_cr_quot = int(input("nombre de créneaux par jour : "));
nb_etu = int(input("nombre d'étudiants : "));
nb_places = int(input("nombre de places par salle : "));
nb_creneaux = nb_salles * nb_cr_quot * 5; # nombre total de créneaux disponibles dans la semaine
remp_creneaux = []; # remplissage de chaque creneau
score_voeux = 0; # fonction à maximiser

voeux_etu = []; # stocke les voeux générés aléatoirement des étudiants

##### Génération des voeux #####

i = 0;
while (i < nb_etu): # ajoute les voeux de chaque étudiant à la liste
    j = 0;
    voeux = [];
    while (j < 5): # génère 5 voeux par étudiant parmi le nombre de créneaux disponibles
        voeux.append(random.randint(1, nb_creneaux));
        j += 1;
    voeux_etu.append(voeux);
    i += 1;

print(voeux_etu)

##### réation de la liste de résultats #####

i = 0;
while (i < nb_creneaux):
    remp_creneaux.append([0]);

print(remp_creneaux);

##### Répartition des voeux #####

i = 0;
while (i < nb_etu):
    j = 0;
    while (j < 5): # teste la disponibilité par ordre des voeux
        if(remp_creneaux[voeux_etu[i][j]] < np_places):
            remp_creneaux[voeux_etu[i][1]] += 1;
            score_voeux += 5 - j;
            j = 4;
        j += 1;
    i += 1;
           
print(remp_creneaux);
