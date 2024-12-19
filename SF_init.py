from Systeme_flou import SystemeFlou, trimf, trapmf
import numpy as np
import matplotlib.pyplot as plt

print("Initialisation des systemes flous...")
#SF1

#Entrees
#appreciation des professeurs
x_appreciation_des_professseurs = np.arange(0, 1.25, 0.25)


appreciation_des_professseurs_TN = trimf(x_appreciation_des_professseurs, [0, 0 ,0.25])
appreciation_des_professseurs_N = trimf(x_appreciation_des_professseurs, [0, 0.25,0.5])
appreciation_des_professseurs_NTR = trimf(x_appreciation_des_professseurs, [0.25, 0.5, 0.75])
appreciation_des_professseurs_P = trimf(x_appreciation_des_professseurs, [0.5, 0.75, 1])
appreciation_des_professseurs_TP = trimf(x_appreciation_des_professseurs, [0.75, 1,1])

#afficher les fonctions d'appartenance
# fig, ax = plt.subplots()
# ax.plot(x_appreciation_des_professseurs, appreciation_des_professseurs_TN, 'b', linewidth=1.5, label='TN')
# ax.plot(x_appreciation_des_professseurs, appreciation_des_professseurs_N, 'g', linewidth=1.5, label='N')
# ax.plot(x_appreciation_des_professseurs, appreciation_des_professseurs_NTR, 'r', linewidth=1.5, label='NTR')
# ax.plot(x_appreciation_des_professseurs, appreciation_des_professseurs_P, 'y', linewidth=1.5, label='P')
# ax.plot(x_appreciation_des_professseurs, appreciation_des_professseurs_TP, 'm', linewidth=1.5, label='TP')

# ax.set_title('Appreciation des professeurs')
# ax.legend()
# plt.show()

#Potentiel Academique Perçu
x_potentiel_academique_percu = np.arange(0, 1.5, 0.5)

potentiel_academique_percu_FAIBLE = trimf(x_potentiel_academique_percu, [0, 0, 0.5])
potentiel_academique_percu_MOYEN = trimf(x_potentiel_academique_percu, [0, 0.5, 1])
potentiel_academique_percu_FORT = trimf(x_potentiel_academique_percu, [0.5, 1, 1])

#Activite Extrascolaire 

x_activites_extrascolaires = np.arange(0, 1.25, 0.25)

activites_extrascolaires_I = trimf(x_activites_extrascolaires, [0, 0 ,0.25])
activites_extrascolaires_P = trimf(x_activites_extrascolaires, [0,0.25,0.5])
activites_extrascolaires_M = trimf(x_activites_extrascolaires,  [0.25, 0.5, 0.75])
activites_extrascolaires_N = trimf(x_activites_extrascolaires, [0.5, 0.75, 1])
activites_extrascolaires_TN = trimf(x_activites_extrascolaires,  [0.75, 1,1])

#Sortie
#Engagement
x_engagement = np.arange(0, 1.25, 0.25)

engagement_TF = trimf(x_engagement, [0, 0, 0.25])
engagement_F = trimf(x_engagement, [0, 0.25, 0.5])
engagement_M = trimf(x_engagement, [0.25, 0.5, 0.75])
engagement_B = trimf(x_engagement, [0.5, 0.75, 1])
engagement_E = trimf(x_engagement, [0.75, 1, 1])

#Regles
tab_engagement = [
    #appreciation des professeurs
    # "TN"  "N"   "NTR"  "P"   "TP"
    # Potentiel académique FAIBLE
    [
        ['TF', 'F', 'F', 'M', 'M'],  # Activité extrascolaire 'I'
        ['TF', 'F', 'M', 'M', 'M'],    # Activité extrascolaire 'P'
        ['TF', 'M', 'M', 'M', 'B'],      # Activité extrascolaire 'M'
        ['TF', 'M', 'M', 'B', 'B'],      # Activité extrascolaire 'N'
        ['TF', 'M', 'M', 'B', 'B'],      # Activité extrascolaire 'TN'
    ],
    
    # Potentiel académique MOYEN
    [
        ['TF', 'F', 'F', 'M', 'M'],  # Activité extrascolaire 'I'
        ['TF', 'F', 'M', 'B', 'B'],     # Activité extrascolaire 'P'
        ['TF', 'M', 'B', 'B', 'E'],      # Activité extrascolaire 'M'
        ['TF', 'M', 'B', 'B', 'E'],      # Activité extrascolaire 'N'
        ['TF', 'M', 'B', 'B', 'E'],      # Activité extrascolaire 'TN'
    ],
    
    # Potentiel académique FORT
    [
        ['TF', 'F', 'F', 'M', 'B'],  # Activité extrascolaire 'I'
        ['TF', 'F', 'M', 'B', 'E'],     # Activité extrascolaire 'P'
        ['TF', 'M', 'B', 'E', 'E'],      # Activité extrascolaire 'M'
        ['TF', 'B', 'B', 'E', 'E'],      # Activité extrascolaire 'N'
        ['TF', 'B', 'B', 'E', 'E'],      # Activité extrascolaire 'TN'
    ],
]

SF1 = SystemeFlou()
SF1.ajouter_variable_entree("appreciation_des_professeurs", x_appreciation_des_professseurs, {"TN": appreciation_des_professseurs_TN, "N": appreciation_des_professseurs_N, "NTR": appreciation_des_professseurs_NTR, "P": appreciation_des_professseurs_P, "TP": appreciation_des_professseurs_TP})
SF1.ajouter_variable_entree("potentiel_academique_percu", x_potentiel_academique_percu, {"FAIBLE": potentiel_academique_percu_FAIBLE, "MOYEN": potentiel_academique_percu_MOYEN, "FORT": potentiel_academique_percu_FORT})
SF1.ajouter_variable_entree("activites_extrascolaires", x_activites_extrascolaires, {"I": activites_extrascolaires_I, "P": activites_extrascolaires_P, "M": activites_extrascolaires_M, "N": activites_extrascolaires_N, "TN": activites_extrascolaires_TN})
SF1.ajouter_variable_sortie("engagement", x_engagement, {"TF": engagement_TF, "F": engagement_F, "M": engagement_M, "B": engagement_B, "E": engagement_E})

liste_regles = []

for x, potentiel_label in enumerate(['FAIBLE', 'MOYEN', 'FORT']):
    for y, extrascolaire_label in enumerate(['I', 'P', 'M', 'N', 'TN']):
        for z, appreciation_label in enumerate(['TN', 'N', 'NTR', 'P', 'TP']):
            # Définir l'engagement cible
            engagement_target = tab_engagement[x][y][z]
            
            # Créer une règle
            rule = {
                "conditions": {
                    "appreciation_des_professeurs": appreciation_label,
                    "potentiel_academique_percu": potentiel_label,
                    "activites_extrascolaires": extrascolaire_label
                },
                "conclusion": engagement_target
            }
        
            SF1.ajouter_regle(rule)

#FIN SF1





#SF2

#Entrees
#motivation percue
x_motivation_percue = np.arange(0, 1.25, 0.25)

motivation_percue_TI= trimf(x_motivation_percue, [0, 0, 0.25])
motivation_percue_I= trimf(x_motivation_percue, [0, 0.25, 0.5])
motivation_percue_M= trimf(x_motivation_percue, [0.25, 0.5, 0.75])
motivation_percue_B= trimf(x_motivation_percue, [0.5, 0.75, 1])
motivation_percue_TB= trimf(x_motivation_percue, [0.75, 1, 1])

#qualité lettre de motivation
x_qualite_lettre_de_motivation = np.arange(0, 1.25, 0.25)

qualite_lettre_de_motivation_TI= trimf(x_qualite_lettre_de_motivation, [0, 0, 0.25])
qualite_lettre_de_motivation_I= trimf(x_qualite_lettre_de_motivation, [0, 0.25, 0.5])
qualite_lettre_de_motivation_M= trimf(x_qualite_lettre_de_motivation, [0.25, 0.5, 0.75])
qualite_lettre_de_motivation_B= trimf(x_qualite_lettre_de_motivation, [0.5, 0.75, 1])
qualite_lettre_de_motivation_TB= trimf(x_qualite_lettre_de_motivation, [0.75, 1, 1])

#Sortie
#Motivation
x_motivation = np.arange(0, 1.25, 0.25)

motivation_TF = trimf(x_motivation, [0, 0, 0.25])
motivation_F = trimf(x_motivation, [0, 0.25, 0.5])
motivation_M = trimf(x_motivation, [0.25, 0.5, 0.75])
motivation_B = trimf(x_motivation, [0.5, 0.75, 1])
motivation_TB = trimf(x_motivation, [0.75, 1, 1])


#Regles
tab_motivation = [
    # Motivation percue
    # "TI"  "I"   "M"  "B"   "TB"
    ['TF', 'TF', 'TF', 'TF', 'F'],  # Qualité lettre de motivation 'TI'
    ['TF', 'TF', 'TF', 'F', 'M'],   # Qualité lettre de motivation 'I'
    ['TF', 'TF', 'F', 'M', 'B'],    # Qualité lettre de motivation 'M'
    ['TF', 'F', 'M', 'B', 'TB'],    # Qualité lettre de motivation 'B'
    ['F', 'M', 'B', 'TB', 'TB'],    # Qualité lettre de motivation 'TB'
]

SF2 = SystemeFlou()
SF2.ajouter_variable_entree("motivation_percue", x_motivation_percue, {"TI": motivation_percue_TI, "I": motivation_percue_I, "M": motivation_percue_M, "B": motivation_percue_B, "TB": motivation_percue_TB})
SF2.ajouter_variable_entree("qualite_lettre_de_motivation", x_qualite_lettre_de_motivation, {"TI": qualite_lettre_de_motivation_TI, "I": qualite_lettre_de_motivation_I, "M": qualite_lettre_de_motivation_M, "B": qualite_lettre_de_motivation_B, "TB": qualite_lettre_de_motivation_TB})
SF2.ajouter_variable_sortie("motivation", x_motivation, {"TF": motivation_TF, "F": motivation_F, "M": motivation_M, "B": motivation_B, "TB": motivation_TB})


for x, qualite_lettre_de_motivation_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
    for y,motivation_label  in enumerate(['TI', 'I', 'M', 'B', 'TB']):
        # Définir la motivation cible
        motivation_target = tab_motivation[x][y]
        
        # Créer une règle
        rule = {
            "conditions": {
                "motivation_percue": motivation_label,
                "qualite_lettre_de_motivation": qualite_lettre_de_motivation_label
            },
            "conclusion": motivation_target
        }
        
        SF2.ajouter_regle(rule)

#FIN SF2




#SF3
#Entrees
#Résultat scolaire
x_resultat_scolaire = np.arange(0, 21, 1)

resultat_scolaire_TI = trimf(x_resultat_scolaire, [0, 0, 5])   
resultat_scolaire_I = trimf(x_resultat_scolaire, [0, 5, 10])
resultat_scolaire_M = trimf(x_resultat_scolaire, [5, 10, 15])
resultat_scolaire_B = trimf(x_resultat_scolaire, [10, 15, 18])
resultat_scolaire_TB = trapmf(x_resultat_scolaire, [15, 18, 20, 20])
#afficher les fonctions d'appartenance
# fig, ax = plt.subplots()
# ax.plot(x_resultat_scolaire, resultat_scolaire_TI, 'b', linewidth=1.5, label='TI')
# ax.plot(x_resultat_scolaire, resultat_scolaire_I, 'g', linewidth=1.5, label='I')
# ax.plot(x_resultat_scolaire, resultat_scolaire_M, 'r', linewidth=1.5, label='M')
# ax.plot(x_resultat_scolaire, resultat_scolaire_B, 'y', linewidth=1.5, label='B')

# ax.plot(x_resultat_scolaire, resultat_scolaire_TB, 'm', linewidth=1.5, label='TB')

# ax.set_title('Resultat scolaire')
# ax.legend()
# plt.show()

#Niveau scientifique
x_niveau_scientifique = np.arange(0, 21, 1)

niveau_scientifique_TI = trimf(x_niveau_scientifique, [0, 0, 5])
niveau_scientifique_I = trimf(x_niveau_scientifique, [0, 5, 10])
niveau_scientifique_M = trimf(x_niveau_scientifique, [5, 10, 15])
niveau_scientifique_B = trimf(x_niveau_scientifique, [10, 15, 19])
niveau_scientifique_TB = trapmf(x_niveau_scientifique, [15, 19, 20, 20])

#Niveau litteraire
x_niveau_litteraire = np.arange(0, 21, 1)

niveau_litteraire_TI = trimf(x_niveau_litteraire, [0, 0, 5])
niveau_litteraire_I = trimf(x_niveau_litteraire, [0, 5, 10])
niveau_litteraire_M = trimf(x_niveau_litteraire, [5, 10, 15])
niveau_litteraire_B = trimf(x_niveau_litteraire, [10, 15, 18])
niveau_litteraire_TB = trapmf(x_niveau_litteraire, [15, 18, 20, 20])

#Sortie
#score academique global
x_score_academique_global = np.arange(0, 1.25, 0.25)

score_academique_global_TF = trimf(x_score_academique_global, [0, 0, 0.25])
score_academique_global_F = trimf(x_score_academique_global, [0, 0.25, 0.5])
score_academique_global_M = trimf(x_score_academique_global, [0.25, 0.5, 0.75])
score_academique_global_B = trimf(x_score_academique_global, [0.5, 0.75, 1])
score_academique_global_TB = trimf(x_score_academique_global, [0.75, 1, 1])


#Regles
tab_score_academique_global = [
    # Niveau scientifique
    # "TI"  "I"   "M"  "B"   "TB"
    
    # Résultat scolaire 'TI'
    [
    ['TF', 'TF', 'TF', 'TF', 'TF'],  # Niveau litteraire 'TI'
    ['TF', 'TF', 'TF', 'TF', 'TF'],   # Niveau litteraire 'I'
    ['TF', 'TF', 'TF', 'TF', 'F'],    # Niveau litteraire 'M'
    ['TF', 'TF', 'TF', 'F', 'F'],    # Niveau litteraire 'B'
    ['TF', 'TF', 'TF', 'F', 'M'],    # Niveau litteraire 'TB'
    ],
    
    # Résultat scolaire 'I'
    [
    ['TF', 'TF', 'TF', 'TF', 'F'],  # Niveau litteraire 'TI'
    ['TF', 'TF', 'TF', 'TF', 'F'],   # Niveau litteraire 'I'
    ['TF', 'TF', 'TF', 'TF', 'F'],    # Niveau litteraire 'M'
    ['TF', 'TF', 'TF', 'F', 'F'],    # Niveau litteraire 'B'
    ['TF', 'TF', 'TF', 'F', 'M'],    # Niveau litteraire 'TB'
    ],
    
    # Résultat scolaire 'M'
    [
    ['TF', 'TF', 'TF', 'F', 'F'],  # Niveau litteraire 'TI'
    ['TF', 'TF', 'TF', 'F', 'M'],   # Niveau litteraire 'I'
    ['TF', 'TF', 'TF', 'F', 'M'],    # Niveau litteraire 'M'
    ['TF', 'TF', 'F', 'M', 'M'],    # Niveau litteraire 'B'
    ['TF', 'TF', 'F', 'M', 'B'],    # Niveau litteraire 'TB'
    ],
    
    # Résultat scolaire 'B'
    [
    ['TF', 'TF', 'TF', 'M', 'M'],  # Niveau litteraire 'TI'
    ['TF', 'TF', 'F', 'M', 'B'],   # Niveau litteraire 'I'
    ['TF', 'TF', 'M', 'B', 'B'],    # Niveau litteraire 'M'
    ['TF', 'TF', 'M', 'B', 'TB'],    # Niveau litteraire 'B'
    ['TF', 'F', 'M', 'B', 'TB'],    # Niveau litteraire 'TB'
    ],
    
    # Résultat scolaire 'TB'
    [
    ['TF', 'TF', 'TF', 'M', 'B'],  # Niveau litteraire 'TI'
    ['TF', 'TF', 'F', 'B', 'TB'],   # Niveau litteraire 'I'
    ['TF', 'TF', 'M', 'B', 'TB'],    # Niveau litteraire 'M'
    ['TF', 'F', 'B', 'TB', 'TB'],    # Niveau litteraire 'B'
    ['TF', 'F', 'B', 'TB', 'TB'],    # Niveau litteraire 'TB'
    ],
]

SF3 = SystemeFlou()
SF3.ajouter_variable_entree("resultat_scolaire", x_resultat_scolaire, {"TI": resultat_scolaire_TI, "I": resultat_scolaire_I, "M": resultat_scolaire_M, "B": resultat_scolaire_B, "TB": resultat_scolaire_TB})
SF3.ajouter_variable_entree("niveau_scientifique", x_niveau_scientifique, {"TI": niveau_scientifique_TI, "I": niveau_scientifique_I, "M": niveau_scientifique_M, "B": niveau_scientifique_B, "TB": niveau_scientifique_TB})
SF3.ajouter_variable_entree("niveau_litteraire", x_niveau_litteraire, {"TI": niveau_litteraire_TI, "I": niveau_litteraire_I, "M": niveau_litteraire_M, "B": niveau_litteraire_B, "TB": niveau_litteraire_TB})
SF3.ajouter_variable_sortie("score_academique_global", x_score_academique_global, {"TF": score_academique_global_TF, "F": score_academique_global_F, "M": score_academique_global_M, "B": score_academique_global_B, "TB": score_academique_global_TB})


for x, resultat_scolaire_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
    for y, niveau_litteraire_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
        for z, niveau_scientifique_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
            # Définir le score académique global cible
            score_academique_global_target = tab_score_academique_global[x][y][z]
            
            # Créer une règle
            rule = {
                "conditions": {
                    "resultat_scolaire": resultat_scolaire_label,
                    "niveau_litteraire": niveau_litteraire_label,
                    "niveau_scientifique": niveau_scientifique_label
                },
                "conclusion": score_academique_global_target
            }
            
            SF3.ajouter_regle(rule)

#FIN SF3




#SF4
#Entrees
#Niveau du Lycée
x_niveau_lycee = np.arange(0, 1.25, 0.25)

niveau_lycee_TI = trimf(x_niveau_lycee, [0, 0, 0.25]) 
niveau_lycee_I = trimf(x_niveau_lycee, [0, 0.25, 0.5]) 
niveau_lycee_M = trimf(x_niveau_lycee, [0.25, 0.5, 0.75]) 
niveau_lycee_B = trimf(x_niveau_lycee, [0.5, 0.75, 1]) 
niveau_lycee_TB = trimf(x_niveau_lycee, [0.75, 1, 1]) 

#Niveau de la Classe
x_niveau_classe = np.arange(0, 1.25, 0.25)

niveau_classe_TI = trimf(x_niveau_classe, [0, 0, 0.25])
niveau_classe_I = trimf(x_niveau_classe, [0, 0.25, 0.5])
niveau_classe_M = trimf(x_niveau_classe, [0.25, 0.5, 0.75])
niveau_classe_B = trimf(x_niveau_classe, [0.5, 0.75, 1])
niveau_classe_TB = trimf(x_niveau_classe, [0.75, 1, 1])


#classement de l'eleve dans la classe
x_classement_eleve = np.arange(0, 1.5, 0.5)

classement_eleve_B = trimf(x_classement_eleve, [0, 0, 0.5])
classement_eleve_M = trimf(x_classement_eleve, [0, 0.5, 1])
classement_eleve_H = trimf(x_classement_eleve, [0.5, 1, 1])

#Sortie
#Score d'ajustement lycée-classe
x_score_ajustement_lycee_classe = np.arange(0, 1.25, 0.25)

score_ajustement_lycee_classe_TF = trimf(x_score_ajustement_lycee_classe, [0, 0, 0.25])
score_ajustement_lycee_classe_F = trimf(x_score_ajustement_lycee_classe, [0, 0.25, 0.5])
score_ajustement_lycee_classe_M = trimf(x_score_ajustement_lycee_classe, [0.25, 0.5, 0.75])
score_ajustement_lycee_classe_B = trimf(x_score_ajustement_lycee_classe, [0.5, 0.75, 1])
score_ajustement_lycee_classe_TB = trimf(x_score_ajustement_lycee_classe, [0.75, 1, 1])



#Regles

tab_score_ajustement_lycee_classe = [
    # Niveau du Lycée
    # "TI"  "I"   "M"  "B"   "TB"
    
    # classement de l'eleve dans la classe 'B'
    [
        ['TF', 'TF', 'TF', 'F', 'M'],  # Niveau de la Classe 'TI'
        ['TF', 'TF', 'TF', 'F', 'M'],   # Niveau de la Classe 'I'
        ['TF', 'TF', 'F', 'M', 'B'],    # Niveau de la Classe 'M'
        ['TF', 'TF', 'F', 'B', 'TB'],    # Niveau de la Classe 'B'
        ['TF', 'F', 'M', 'B', 'TB'],    # Niveau de la Classe 'TB'
    ],
    
    # classement de l'eleve dans la classe 'M'
    [
        ['TF', 'TF', 'F', 'F', 'M'],  # Niveau de la Classe 'TI'
        ['TF', 'TF', 'F', 'M', 'B'],   # Niveau de la Classe 'I'
        ['TF', 'TF', 'F', 'B', 'TB'],    # Niveau de la Classe 'M'
        ['TF', 'F', 'M', 'TB', 'TB'],    # Niveau de la Classe 'B'
        ['TF', 'F', 'B', 'TB', 'TB'],    # Niveau de la Classe 'TB'
    ],
    
    # classement de l'eleve dans la classe 'H'
    [
        ['F', 'F', 'B', 'TB', 'TB'],  # Niveau de la Classe 'TI'
        ['F', 'M', 'B', 'TB', 'TB'],   # Niveau de la Classe 'I'
        ['F', 'B', 'B', 'TB', 'TB'],    # Niveau de la Classe 'M'
        ['M', 'B', 'B', 'TB', 'TB'],    # Niveau de la Classe 'B'
        ['M', 'B', 'TB', 'TB', 'TB'],    # Niveau de la Classe 'TB'
    ],
]

SF4 = SystemeFlou()
SF4.ajouter_variable_entree("niveau_lycee", x_niveau_lycee, {"TI": niveau_lycee_TI, "I": niveau_lycee_I, "M": niveau_lycee_M, "B": niveau_lycee_B, "TB": niveau_lycee_TB})
SF4.ajouter_variable_entree("niveau_classe", x_niveau_classe, {"TI": niveau_classe_TI, "I": niveau_classe_I, "M": niveau_classe_M, "B": niveau_classe_B, "TB": niveau_classe_TB})
SF4.ajouter_variable_entree("classement_eleve", x_classement_eleve, {"B": classement_eleve_B, "M": classement_eleve_M, "H": classement_eleve_H})
SF4.ajouter_variable_sortie("score_ajustement_lycee_classe", x_score_ajustement_lycee_classe, {"TF": score_ajustement_lycee_classe_TF, "F": score_ajustement_lycee_classe_F, "M": score_ajustement_lycee_classe_M, "B": score_ajustement_lycee_classe_B, "TB": score_ajustement_lycee_classe_TB})



for x, classement_eleve_label in enumerate(['B', 'M', 'H']):
    for y, niveau_classe_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
        for z, niveau_lycee_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
            # Définir le score d'ajustement lycée-classe cible
            score_ajustement_lycee_classe_target = tab_score_ajustement_lycee_classe[x][y][z]
            
            # Créer une règle
            rule = {
                "conditions": {
                    "niveau_lycee": niveau_lycee_label,
                    "niveau_classe": niveau_classe_label,
                    "classement_eleve": classement_eleve_label
                },
                "conclusion": score_ajustement_lycee_classe_target
            }
            
            SF4.ajouter_regle(rule)

#FIN SF4




#SF5
#Entrees
#Score académique global



#score d'ajustement lycée-classe

#Sortie
#Niveau scolaire ajusté
x_niveau_scolaire_ajuste = np.arange(0, 1.25, 0.25)

niveau_scolaire_ajuste_TF = trimf(x_niveau_scolaire_ajuste, [0, 0, 0.25])
niveau_scolaire_ajuste_F = trimf(x_niveau_scolaire_ajuste, [0 ,0.25, 0.5])
niveau_scolaire_ajuste_M = trimf(x_niveau_scolaire_ajuste, [0.25, 0.5, 0.75])
niveau_scolaire_ajuste_B = trimf(x_niveau_scolaire_ajuste, [0.5, 0.75, 1])
niveau_scolaire_ajuste_TB = trimf(x_niveau_scolaire_ajuste, [0.75, 1, 1])



#Regles

tab_niveau_scolaire_ajuste = [
    # Score académique global
    #"TF"  "F"   "M"   "B"   "TB"
    ['TF', 'TF', 'TF', 'F', 'M'],  # Score d'ajustement lycée-classe 'TF'
    ['TF', 'TF', 'F', 'M', 'B'],  # Score d'ajustement lycée-classe 'F'
    ['TF', 'F', 'M', 'M', 'B'],  # Score d'ajustement lycée-classe 'M'
    ['F', 'M', 'B', 'B', 'TB'],  # Score d'ajustement lycée-classe 'B'
    ['M', 'B', 'TB', 'TB', 'TB'],  # Score d'ajustement lycée-classe 'TB'
]

SF5 = SystemeFlou()
SF5.ajouter_variable_entree("score_academique_global", x_score_academique_global, {"TF": score_academique_global_TF, "F": score_academique_global_F, "M": score_academique_global_M, "B": score_academique_global_B, "TB": score_academique_global_TB})
SF5.ajouter_variable_entree("score_ajustement_lycee_classe", x_score_ajustement_lycee_classe, {"TF": score_ajustement_lycee_classe_TF, "F": score_ajustement_lycee_classe_F, "M": score_ajustement_lycee_classe_M, "B": score_ajustement_lycee_classe_B, "TB": score_ajustement_lycee_classe_TB})
SF5.ajouter_variable_sortie("niveau_scolaire_ajuste", x_niveau_scolaire_ajuste, {"TF": niveau_scolaire_ajuste_TF, "F": niveau_scolaire_ajuste_F, "M": niveau_scolaire_ajuste_M, "B": niveau_scolaire_ajuste_B, "TB": niveau_scolaire_ajuste_TB})


for x, score_ajustement_lycee_classe_label  in enumerate(['TF', 'F', 'M', 'B', 'TB']):
    for y, score_academique_global_label  in enumerate(['TF', 'F', 'M', 'B', 'TB']):
        # Définir le niveau scolaire ajusté cible
        niveau_scolaire_ajuste_target = tab_niveau_scolaire_ajuste[x][y]
        
        # Créer une règle
        rule = {
            "conditions": {
                "score_academique_global": score_academique_global_label,
                "score_ajustement_lycee_classe": score_ajustement_lycee_classe_label
            },
            "conclusion": niveau_scolaire_ajuste_target
        }
        
        SF5.ajouter_regle(rule)
        

#FIN SF5




#SF6
#Entrees
#engagement

#Motivation

#sortie
#predisposition academique
x_predisposition_academique = np.arange(0, 1.25, 0.25)

predisposition_academique_TF = trimf(x_predisposition_academique, [0, 0, 0.25])
predisposition_academique_F = trimf(x_predisposition_academique, [0, 0.25, 0.5])
predisposition_academique_M = trimf(x_predisposition_academique, [0.25, 0.5, 0.75])
predisposition_academique_B = trimf(x_predisposition_academique, [0.5, 0.75, 1])
predisposition_academique_TB = trimf(x_predisposition_academique, [0.75, 1, 1])



#Regles

tab_predisposition_academique = [
    # Engagement
    #"TF"  "F"   "M"   "B"   "E"
    ['TF', 'TF', 'TF', 'F', 'M'],  # Motivation 'TF'
    ['TF', 'TF', 'F', 'M', 'M'],  # Motivation 'F'
    ['TF', 'F', 'M', 'M', 'B'],  # Motivation 'M'
    ['F', 'M', 'M', 'B', 'TB'],  # Motivation 'B'
    ['M', 'M', 'B', 'TB', 'TB'],  # Motivation 'TB'
]


SF6 = SystemeFlou()
SF6.ajouter_variable_entree("engagement", x_engagement, {"TF": engagement_TF, "F": engagement_F, "M": engagement_M, "B": engagement_B, "E": engagement_E})
SF6.ajouter_variable_entree("motivation", x_motivation, {"TF": motivation_TF, "F": motivation_F, "M": motivation_M, "B": motivation_B, "TB": motivation_TB})
SF6.ajouter_variable_sortie("predisposition_academique", x_predisposition_academique, {"TF": predisposition_academique_TF, "F": predisposition_academique_F, "M": predisposition_academique_M, "B": predisposition_academique_B, "TB": predisposition_academique_TB})



for x, motivation_label in enumerate(['TF', 'F', 'M', 'B', 'TB']):
    for y, engagement_label in enumerate(['TF', 'F', 'M', 'B', 'E']):
        # Définir la predisposition academique cible
        predisposition_academique_target = tab_predisposition_academique[x][y]
        
        # Créer une règle
        rule = {
            "conditions": {
                "motivation": motivation_label,
                "engagement": engagement_label
            },
            "conclusion": predisposition_academique_target
        }
        
        SF6.ajouter_regle(rule)
        
#FIN SF6




#SF7
#Entrees
#predisposition academique


#niveau scolaire ajusté


#sortie
#Score de l'élève
x_score_eleve = np.arange(0, 1.25, 0.25)

score_eleve_TF = trimf(x_score_eleve, [0, 0, 0.25])
score_eleve_F = trimf(x_score_eleve, [0, 0.25, 0.5])
score_eleve_M = trimf(x_score_eleve, [0.25, 0.5, 0.75])
score_eleve_B = trimf(x_score_eleve, [0.5, 0.75, 1])
score_eleve_TB = trimf(x_score_eleve, [0.75, 1, 1])


#Regles

tab_score_eleve = [
    # predisposition academique
    #"TF"  "F"   "M"   "B"   "TB"
    ['TF', 'TF', 'TF', 'F', 'M'],  # Niveau scolaire ajusté 'TF'
    ['TF', 'TF', 'F', 'M', 'B'],  # Niveau scolaire ajusté 'F'
    ['TF', 'F', 'M', 'B', 'B'],  # Niveau scolaire ajusté 'M'
    ['F', 'M', 'B', 'B', 'TB'],  # Niveau scolaire ajusté 'B'
    ['M', 'B', 'B', 'TB', 'TB'],  # Niveau scolaire ajusté 'TB'
]

SF7 = SystemeFlou()
SF7.ajouter_variable_entree("predisposition_academique", x_predisposition_academique, {"TF": predisposition_academique_TF, "F": predisposition_academique_F, "M": predisposition_academique_M, "B": predisposition_academique_B, "TB": predisposition_academique_TB})
SF7.ajouter_variable_entree("niveau_scolaire_ajuste", x_niveau_scolaire_ajuste, {"TF": niveau_scolaire_ajuste_TF, "F": niveau_scolaire_ajuste_F, "M": niveau_scolaire_ajuste_M, "B": niveau_scolaire_ajuste_B, "TB": niveau_scolaire_ajuste_TB})
SF7.ajouter_variable_sortie("score_eleve", x_score_eleve, {"TF": score_eleve_TF, "F": score_eleve_F, "M": score_eleve_M, "B": score_eleve_B, "TB": score_eleve_TB})


for x, niveau_scolaire_ajuste_label in enumerate(['TF', 'F', 'M', 'B', 'TB']):
    for y,predisposition_academique_label  in enumerate(['TF', 'F', 'M', 'B', 'TB']):
        # Définir le score de l'élève cible
        score_eleve_target = tab_score_eleve[x][y]
        
        # Créer une règle
        rule = {
            "conditions": {
                "niveau_scolaire_ajuste": niveau_scolaire_ajuste_label,
                "predisposition_academique": predisposition_academique_label
            },
            "conclusion": score_eleve_target
        }
        
        SF7.ajouter_regle(rule)

#FIN SF7


systemes_flous_dico = {
    'engagement': [SF1, x_engagement, [engagement_TF, engagement_F, engagement_M, engagement_B, engagement_E]],
    'motivation': [SF2, x_motivation, [motivation_TF, motivation_F, motivation_M, motivation_B, motivation_TB]], 
    'score_academique_global': [SF3, x_score_academique_global, [score_academique_global_TF, score_academique_global_F, score_academique_global_M, score_academique_global_B, score_academique_global_TB]],
    'score_ajustement_lycee_classe': [SF4, x_score_ajustement_lycee_classe, [score_ajustement_lycee_classe_TF, score_ajustement_lycee_classe_F, score_ajustement_lycee_classe_M, score_ajustement_lycee_classe_B, score_ajustement_lycee_classe_TB]],
    'niveau_scolaire_ajuste': [SF5, x_niveau_scolaire_ajuste, [niveau_scolaire_ajuste_TF, niveau_scolaire_ajuste_F, niveau_scolaire_ajuste_M, niveau_scolaire_ajuste_B, niveau_scolaire_ajuste_TB]],
    'predisposition_academique': [SF6, x_predisposition_academique, [predisposition_academique_TF, predisposition_academique_F, predisposition_academique_M, predisposition_academique_B, predisposition_academique_TB]],
    'score_eleve': [SF7, x_score_eleve, [score_eleve_TF, score_eleve_F, score_eleve_M, score_eleve_B, score_eleve_TB]]
}

import pickle

with open('systemes_flous.pkl', 'wb') as f:
    pickle.dump(systemes_flous_dico, f)
    
print("Systèmes flous sauvegardés dans 'systemes_flous.pkl'")