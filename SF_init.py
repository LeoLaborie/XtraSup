import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

print("Initialisation des systemes flous...")
#SF2

#Entrees
#appreciation des professeurs
x_appreciation_des_professseurs = np.arange(0, 1.25, 0.25)


appreciation_des_professseurs_TN = fuzz.trimf(x_appreciation_des_professseurs, [0, 0 ,0.25])
appreciation_des_professseurs_N = fuzz.trimf(x_appreciation_des_professseurs, [0, 0.25,0.5])
appreciation_des_professseurs_NTR = fuzz.trimf(x_appreciation_des_professseurs, [0.25, 0.5, 0.75])
appreciation_des_professseurs_P = fuzz.trimf(x_appreciation_des_professseurs, [0.5, 0.75, 1])
appreciation_des_professseurs_TP = fuzz.trimf(x_appreciation_des_professseurs, [0.75, 1,1])
#afficher les fonctions d'appartenance
fig, ax = plt.subplots()
ax.plot(x_appreciation_des_professseurs, appreciation_des_professseurs_TN, 'b', linewidth=1.5, label='TN')
ax.plot(x_appreciation_des_professseurs, appreciation_des_professseurs_N, 'g', linewidth=1.5, label='N')
ax.plot(x_appreciation_des_professseurs, appreciation_des_professseurs_NTR, 'r', linewidth=1.5, label='NTR')
ax.plot(x_appreciation_des_professseurs, appreciation_des_professseurs_P, 'y', linewidth=1.5, label='P')
ax.plot(x_appreciation_des_professseurs, appreciation_des_professseurs_TP, 'm', linewidth=1.5, label='TP')

ax.set_title('Appreciation des professeurs')
ax.legend()
plt.show()
#Potentiel Academique Perçu
x_potentiel_academique_perçu = np.arange(0, 1.5, 0.5)

potentiel_academique_perçu_FAIBLE = fuzz.trimf(x_potentiel_academique_perçu, [0, 0, 0.5])
potentiel_academique_perçu_MOYEN = fuzz.trimf(x_potentiel_academique_perçu, [0, 0.5, 1])
potentiel_academique_perçu_FORT = fuzz.trimf(x_potentiel_academique_perçu, [0.5, 1, 1])

#Activite Extrascolaire

x_activite_extrascolaire = np.arange(0, 1.25, 0.25)

activite_extrascolaire_I = fuzz.trimf(x_activite_extrascolaire, [0, 0 ,0.25])
activite_extrascolaire_P = fuzz.trimf(x_activite_extrascolaire, [0,0.25,0.5])
activite_extrascolaire_M = fuzz.trimf(x_activite_extrascolaire,  [0.25, 0.5, 0.75])
activite_extrascolaire_N = fuzz.trimf(x_activite_extrascolaire, [0.5, 0.75, 1])
activite_extrascolaire_TN = fuzz.trimf(x_activite_extrascolaire,  [0.75, 1,1])

#Sortie
#Engagement
x_engagement = np.arange(0, 1.25, 0.25)

engagement_TF = fuzz.trimf(x_engagement, [0, 0, 0.25])
engagement_F = fuzz.trimf(x_engagement, [0, 0.25, 0.5])
engagement_M = fuzz.trimf(x_engagement, [0.25, 0.5, 0.75])
engagement_B = fuzz.trimf(x_engagement, [0.5, 0.75, 1])
engagement_E = fuzz.trimf(x_engagement, [0.75, 1, 1])

#Regles
tab_engagement = [
    #appreciation des professeurs
    # "TN"  "N"   "NTR"  "P"   "TP"
    # Potentiel académique FAIBLE
    [
        ['TF', 'F', 'F', 'M', 'M'],  # Activité extrascolaire 'I'
        ['TF', 'F', 'M', 'M', 'B'],    # Activité extrascolaire 'P'
        ['TF', 'M', 'M', 'B', 'B'],      # Activité extrascolaire 'M'
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


appreciation = ctrl.Antecedent(x_appreciation_des_professseurs, 'appreciation_des_professeurs')
potentiel = ctrl.Antecedent(x_potentiel_academique_perçu, 'potentiel_academique_percu')
extrascolaire = ctrl.Antecedent(x_activite_extrascolaire, 'activites_extrascolaires')
engagement = ctrl.Consequent(x_engagement, 'engagement')

appreciation['TN'] = appreciation_des_professseurs_TN
appreciation['N'] = appreciation_des_professseurs_N
appreciation['NTR'] = appreciation_des_professseurs_NTR
appreciation['P'] = appreciation_des_professseurs_P
appreciation['TP'] = appreciation_des_professseurs_TP

potentiel['FAIBLE'] = potentiel_academique_perçu_FAIBLE
potentiel['MOYEN'] = potentiel_academique_perçu_MOYEN
potentiel['FORT'] = potentiel_academique_perçu_FORT

extrascolaire['I'] = activite_extrascolaire_I
extrascolaire['P'] = activite_extrascolaire_P
extrascolaire['M'] = activite_extrascolaire_M
extrascolaire['N'] = activite_extrascolaire_N
extrascolaire['TN'] = activite_extrascolaire_TN

engagement['TF'] = engagement_TF
engagement['F'] = engagement_F
engagement['M'] = engagement_M
engagement['B'] = engagement_B
engagement['E'] = engagement_E



liste_regles = []

for x, potentiel_label in enumerate(['FAIBLE', 'MOYEN', 'FORT']):
    for y, extrascolaire_label in enumerate(['I', 'P', 'M', 'N', 'TN']):
        for z, appreciation_label in enumerate(['TN', 'N', 'NTR', 'P', 'TP']):
            # Définir l'engagement cible
            engagement_target = tab_engagement[x][y][z]
            
            # Créer une règle
            rule = ctrl.Rule(
                potentiel[potentiel_label] & 
                extrascolaire[extrascolaire_label] & 
                appreciation[appreciation_label], 
                engagement[engagement_target]
            )
            
            liste_regles.append(rule)

# Créer le système de contrôle
engagement_ctrl = ctrl.ControlSystem(liste_regles)

# Créer la simulation
engagement_sim = ctrl.ControlSystemSimulation(engagement_ctrl)


#FIN SF2






#SF3

#Entrees
#motivation percue
x_motivation_percue = np.arange(0, 1.25, 0.25)

motivation_percue_TI= fuzz.trimf(x_motivation_percue, [0, 0, 0.25])
motivation_percue_I= fuzz.trimf(x_motivation_percue, [0, 0.25, 0.5])
motivation_percue_M= fuzz.trimf(x_motivation_percue, [0.25, 0.5, 0.75])
motivation_percue_B= fuzz.trimf(x_motivation_percue, [0.5, 0.75, 1])
motivation_percue_TB= fuzz.trimf(x_motivation_percue, [0.75, 1, 1])

#qualité lettre de motivation
x_qualite_lettre_de_motivation = np.arange(0, 1.25, 0.25)

qualite_lettre_de_motivation_TI= fuzz.trimf(x_qualite_lettre_de_motivation, [0, 0, 0.25])
qualite_lettre_de_motivation_I= fuzz.trimf(x_qualite_lettre_de_motivation, [0, 0.25, 0.5])
qualite_lettre_de_motivation_M= fuzz.trimf(x_qualite_lettre_de_motivation, [0.25, 0.5, 0.75])
qualite_lettre_de_motivation_B= fuzz.trimf(x_qualite_lettre_de_motivation, [0.5, 0.75, 1])
qualite_lettre_de_motivation_TB= fuzz.trimf(x_qualite_lettre_de_motivation, [0.75, 1, 1])

#Sortie
#Motivation
x_motivation = np.arange(0, 1.25, 0.25)

motivation_TF = fuzz.trimf(x_motivation, [0, 0, 0.25])
motivation_F = fuzz.trimf(x_motivation, [0, 0.25, 0.5])
motivation_M = fuzz.trimf(x_motivation, [0.25, 0.5, 0.75])
motivation_B = fuzz.trimf(x_motivation, [0.5, 0.75, 1])
motivation_TB = fuzz.trimf(x_motivation, [0.75, 1, 1])


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
motivation_percue = ctrl.Antecedent(x_motivation_percue, 'motivation_percue')
qualite_lettre_de_motivation = ctrl.Antecedent(x_qualite_lettre_de_motivation, 'qualite_lettre_de_motivation')
motivation = ctrl.Consequent(x_motivation, 'motivation')

motivation_percue['TI'] = motivation_percue_TI
motivation_percue['I'] = motivation_percue_I
motivation_percue['M'] = motivation_percue_M
motivation_percue['B'] = motivation_percue_B
motivation_percue['TB'] = motivation_percue_TB

qualite_lettre_de_motivation['TI'] = qualite_lettre_de_motivation_TI
qualite_lettre_de_motivation['I'] = qualite_lettre_de_motivation_I
qualite_lettre_de_motivation['M'] = qualite_lettre_de_motivation_M
qualite_lettre_de_motivation['B'] = qualite_lettre_de_motivation_B
qualite_lettre_de_motivation['TB'] = qualite_lettre_de_motivation_TB

motivation['TF'] = motivation_TF
motivation['F'] = motivation_F
motivation['M'] = motivation_M
motivation['B'] = motivation_B
motivation['TB'] = motivation_TB

liste_regles = []

for x, qualite_lettre_de_motivation_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
    for y,motivation_label  in enumerate(['TI', 'I', 'M', 'B', 'TB']):
        # Définir la motivation cible
        motivation_target = tab_motivation[x][y]
        
        # Créer une règle
        rule = ctrl.Rule(
            motivation_percue[motivation_label] & 
            qualite_lettre_de_motivation[qualite_lettre_de_motivation_label], 
            motivation[motivation_target]
        )
        
        liste_regles.append(rule)
        
# Créer le système de contrôle
motivation_ctrl = ctrl.ControlSystem(liste_regles)

# Créer la simulation
motivation_sim = ctrl.ControlSystemSimulation(motivation_ctrl)

#FIN SF3




#SF4
#Entrees
#Résultat scolaire
x_resultat_scolaire = np.arange(0, 21, 1)

resultat_scolaire_TI = fuzz.trimf(x_resultat_scolaire, [0, 0, 5])   
resultat_scolaire_I = fuzz.trimf(x_resultat_scolaire, [0, 5, 10])
resultat_scolaire_M = fuzz.trimf(x_resultat_scolaire, [5, 10, 15])
resultat_scolaire_B = fuzz.trimf(x_resultat_scolaire, [10, 15, 18])
resultat_scolaire_TB = fuzz.trapmf(x_resultat_scolaire, [15, 18, 20, 20])
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

niveau_scientifique_TI = fuzz.trimf(x_niveau_scientifique, [0, 0, 5])
niveau_scientifique_I = fuzz.trimf(x_niveau_scientifique, [0, 5, 10])
niveau_scientifique_M = fuzz.trimf(x_niveau_scientifique, [5, 10, 15])
niveau_scientifique_B = fuzz.trimf(x_niveau_scientifique, [10, 15, 18])
niveau_scientifique_TB = fuzz.trapmf(x_niveau_scientifique, [15, 18, 20, 20])

#Niveau litteraire
x_niveau_litteraire = np.arange(0, 21, 1)

niveau_litteraire_TI = fuzz.trimf(x_niveau_litteraire, [0, 0, 5])
niveau_litteraire_I = fuzz.trimf(x_niveau_litteraire, [0, 5, 10])
niveau_litteraire_M = fuzz.trimf(x_niveau_litteraire, [5, 10, 15])
niveau_litteraire_B = fuzz.trimf(x_niveau_litteraire, [10, 15, 18])
niveau_litteraire_TB = fuzz.trapmf(x_niveau_litteraire, [15, 18, 20, 20])

#Sortie
#score academique global
x_score_academique_global = np.arange(0, 1.25, 0.25)

score_academique_global_TF = fuzz.trimf(x_score_academique_global, [0, 0, 0.25])
score_academique_global_F = fuzz.trimf(x_score_academique_global, [0, 0.25, 0.5])
score_academique_global_M = fuzz.trimf(x_score_academique_global, [0.25, 0.5, 0.75])
score_academique_global_B = fuzz.trimf(x_score_academique_global, [0.5, 0.75, 1])
score_academique_global_TB = fuzz.trimf(x_score_academique_global, [0.75, 1, 1])


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

resultat_scolaire = ctrl.Antecedent(x_resultat_scolaire, 'resultat_scolaire')
niveau_scientifique = ctrl.Antecedent(x_niveau_scientifique, 'niveau_scientifique')
niveau_litteraire = ctrl.Antecedent(x_niveau_litteraire, 'niveau_litteraire')
score_academique_global = ctrl.Consequent(x_score_academique_global, 'score_academique_global')

resultat_scolaire['TI'] = resultat_scolaire_TI
resultat_scolaire['I'] = resultat_scolaire_I
resultat_scolaire['M'] = resultat_scolaire_M
resultat_scolaire['B'] = resultat_scolaire_B
resultat_scolaire['TB'] = resultat_scolaire_TB

niveau_scientifique['TI'] = niveau_scientifique_TI
niveau_scientifique['I'] = niveau_scientifique_I
niveau_scientifique['M'] = niveau_scientifique_M
niveau_scientifique['B'] = niveau_scientifique_B
niveau_scientifique['TB'] = niveau_scientifique_TB

niveau_litteraire['TI'] = niveau_litteraire_TI
niveau_litteraire['I'] = niveau_litteraire_I
niveau_litteraire['M'] = niveau_litteraire_M
niveau_litteraire['B'] = niveau_litteraire_B
niveau_litteraire['TB'] = niveau_litteraire_TB

score_academique_global['TF'] = score_academique_global_TF
score_academique_global['F'] = score_academique_global_F
score_academique_global['M'] = score_academique_global_M
score_academique_global['B'] = score_academique_global_B
score_academique_global['TB'] = score_academique_global_TB

liste_regles = []

for x, resultat_scolaire_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
    for y, niveau_litteraire_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
        for z, niveau_scientifique_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
            # Définir le score académique global cible
            score_academique_global_target = tab_score_academique_global[x][y][z]
            
            # Créer une règle
            rule = ctrl.Rule(
                resultat_scolaire[resultat_scolaire_label] & 
                niveau_litteraire[niveau_litteraire_label] & 
                niveau_scientifique[niveau_scientifique_label], 
                score_academique_global[score_academique_global_target]
            )
            
            liste_regles.append(rule)

# Créer le système de contrôle
score_academique_global_ctrl = ctrl.ControlSystem(liste_regles)

# Créer la simulation
score_academique_global_sim = ctrl.ControlSystemSimulation(score_academique_global_ctrl)

#FIN SF4




#SF5
#Entrees
#Niveau du Lycée
x_niveau_lycee = np.arange(0, 1.25, 0.25)

niveau_lycee_TI = fuzz.trimf(x_niveau_lycee, [0, 0, 0.25]) #<20%
niveau_lycee_I = fuzz.trimf(x_niveau_lycee, [0, 0.25, 0.5]) #20-40%
niveau_lycee_M = fuzz.trimf(x_niveau_lycee, [0.25, 0.5, 0.75]) #40-60%
niveau_lycee_B = fuzz.trimf(x_niveau_lycee, [0.5, 0.75, 1]) #60-80%
niveau_lycee_TB = fuzz.trimf(x_niveau_lycee, [0.75, 1, 1]) #>80%

niveau_lycee = ctrl.Antecedent(x_niveau_lycee, 'niveau_lycee')

niveau_lycee['TI'] = niveau_lycee_TI
niveau_lycee['I'] = niveau_lycee_I
niveau_lycee['M'] = niveau_lycee_M
niveau_lycee['B'] = niveau_lycee_B
niveau_lycee['TB'] = niveau_lycee_TB

#Niveau de la Classe
x_niveau_classe = np.arange(0, 1.25, 0.25)

niveau_classe_TI = fuzz.trimf(x_niveau_classe, [0, 0, 0.25])
niveau_classe_I = fuzz.trimf(x_niveau_classe, [0, 0.25, 0.5])
niveau_classe_M = fuzz.trimf(x_niveau_classe, [0.25, 0.5, 0.75])
niveau_classe_B = fuzz.trimf(x_niveau_classe, [0.5, 0.75, 1])
niveau_classe_TB = fuzz.trimf(x_niveau_classe, [0.75, 1, 1])

niveau_classe = ctrl.Antecedent(x_niveau_classe, 'niveau_classe')

niveau_classe['TI'] = niveau_classe_TI
niveau_classe['I'] = niveau_classe_I
niveau_classe['M'] = niveau_classe_M
niveau_classe['B'] = niveau_classe_B
niveau_classe['TB'] = niveau_classe_TB

#classement de l'eleve dans la classe
x_classement_eleve = np.arange(0, 1.5, 0.5)

classement_eleve_B = fuzz.trimf(x_classement_eleve, [0, 0, 0.5])
classement_eleve_M = fuzz.trimf(x_classement_eleve, [0, 0.5, 1])
classement_eleve_H = fuzz.trimf(x_classement_eleve, [0.5, 1, 1])

classement_eleve = ctrl.Antecedent(x_classement_eleve, 'classement_eleve')

classement_eleve['B'] = classement_eleve_B
classement_eleve['M'] = classement_eleve_M
classement_eleve['H'] = classement_eleve_H
#Sortie
#Score d'ajustement lycée-classe
x_score_ajustement_lycee_classe = np.arange(0, 1.25, 0.25)

score_ajustement_lycee_classe_TF = fuzz.trimf(x_score_ajustement_lycee_classe, [0, 0, 0.25])
score_ajustement_lycee_classe_F = fuzz.trimf(x_score_ajustement_lycee_classe, [0, 0.25, 0.5])
score_ajustement_lycee_classe_M = fuzz.trimf(x_score_ajustement_lycee_classe, [0.25, 0.5, 0.75])
score_ajustement_lycee_classe_B = fuzz.trimf(x_score_ajustement_lycee_classe, [0.5, 0.75, 1])
score_ajustement_lycee_classe_TB = fuzz.trimf(x_score_ajustement_lycee_classe, [0.75, 1, 1])

score_ajustement_lycee_classe = ctrl.Consequent(x_score_ajustement_lycee_classe, 'score_ajustement_lycee_classe')

score_ajustement_lycee_classe['TF'] = score_ajustement_lycee_classe_TF
score_ajustement_lycee_classe['F'] = score_ajustement_lycee_classe_F
score_ajustement_lycee_classe['M'] = score_ajustement_lycee_classe_M
score_ajustement_lycee_classe['B'] = score_ajustement_lycee_classe_B
score_ajustement_lycee_classe['TB'] = score_ajustement_lycee_classe_TB
#Regles

tab_score_ajustement_lycee_classe = [
    # Niveau du Lycée
    # "TI"  "I"   "M"  "B"   "TB"
    
    # classement de l'eleve dans la classe 'B'
    [
        ['TF', 'TF', 'TF', 'TF', 'TF'],  # Niveau de la Classe 'TI'
        ['TF', 'TF', 'TF', 'F', 'F'],   # Niveau de la Classe 'I'
        ['TF', 'TF', 'F', 'F', 'M'],    # Niveau de la Classe 'M'
        ['TF', 'TF', 'F', 'B', 'B'],    # Niveau de la Classe 'B'
        ['TF', 'F', 'M', 'B', 'B'],    # Niveau de la Classe 'TB'
    ],
    
    # classement de l'eleve dans la classe 'M'
    [
        ['TF', 'TF', 'F', 'F', 'F'],  # Niveau de la Classe 'TI'
        ['TF', 'TF', 'F', 'F', 'M'],   # Niveau de la Classe 'I'
        ['TF', 'TF', 'F', 'M', 'B'],    # Niveau de la Classe 'M'
        ['TF', 'F', 'M', 'B', 'B'],    # Niveau de la Classe 'B'
        ['TF', 'F', 'B', 'B', 'TB'],    # Niveau de la Classe 'TB'
    ],
    
    # classement de l'eleve dans la classe 'H'
    [
        ['F', 'F', 'M', 'B', 'B'],  # Niveau de la Classe 'TI'
        ['F', 'M', 'B', 'B', 'TB'],   # Niveau de la Classe 'I'
        ['F', 'B', 'B', 'TB', 'TB'],    # Niveau de la Classe 'M'
        ['M', 'B', 'B', 'TB', 'TB'],    # Niveau de la Classe 'B'
        ['M', 'B', 'TB', 'TB', 'TB'],    # Niveau de la Classe 'TB'
    ],
]

liste_regles = []

for x, classement_eleve_label in enumerate(['B', 'M', 'H']):
    for y, niveau_classe_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
        for z, niveau_lycee_label in enumerate(['TI', 'I', 'M', 'B', 'TB']):
            # Définir le score d'ajustement lycée-classe cible
            score_ajustement_lycee_classe_target = tab_score_ajustement_lycee_classe[x][y][z]
            
            # Créer une règle
            rule = ctrl.Rule(
                niveau_lycee[niveau_lycee_label] & 
                niveau_classe[niveau_classe_label] & 
                classement_eleve[classement_eleve_label], 
                score_ajustement_lycee_classe[score_ajustement_lycee_classe_target]
            )
            
            liste_regles.append(rule)

# Créer le système de contrôle
score_ajustement_lycee_classe_ctrl = ctrl.ControlSystem(liste_regles)

# Créer la simulation
score_ajustement_lycee_classe_sim = ctrl.ControlSystemSimulation(score_ajustement_lycee_classe_ctrl)

#FIN SF5




#SF6
#Entrees
#Score académique global
score_academique_global = ctrl.Antecedent(x_score_academique_global, 'score_academique_global')

score_academique_global['TF'] = score_academique_global_TF
score_academique_global['F'] = score_academique_global_F
score_academique_global['M'] = score_academique_global_M
score_academique_global['B'] = score_academique_global_B
score_academique_global['TB'] = score_academique_global_TB


#score d'ajustement lycée-classe
score_ajustement_lycee_classe = ctrl.Antecedent(x_score_ajustement_lycee_classe, 'score_ajustement_lycee_classe')

score_ajustement_lycee_classe['TF'] = score_ajustement_lycee_classe_TF
score_ajustement_lycee_classe['F'] = score_ajustement_lycee_classe_F
score_ajustement_lycee_classe['M'] = score_ajustement_lycee_classe_M
score_ajustement_lycee_classe['B'] = score_ajustement_lycee_classe_B
score_ajustement_lycee_classe['TB'] = score_ajustement_lycee_classe_TB
#Sortie
#Niveau scolaire ajusté
x_niveau_scolaire_ajuste = np.arange(0, 1.25, 0.25)

niveau_scolaire_ajuste_TF = fuzz.trimf(x_niveau_scolaire_ajuste, [0, 0, 0.25])
niveau_scolaire_ajuste_F = fuzz.trimf(x_niveau_scolaire_ajuste, [0 ,0.25, 0.5])
niveau_scolaire_ajuste_M = fuzz.trimf(x_niveau_scolaire_ajuste, [0.25, 0.5, 0.75])
niveau_scolaire_ajuste_B = fuzz.trimf(x_niveau_scolaire_ajuste, [0.5, 0.75, 1])
niveau_scolaire_ajuste_TB = fuzz.trimf(x_niveau_scolaire_ajuste, [0.75, 1, 1])

niveau_scolaire_ajuste = ctrl.Consequent(x_niveau_scolaire_ajuste, 'niveau_scolaire_ajuste')

niveau_scolaire_ajuste['TF'] = niveau_scolaire_ajuste_TF
niveau_scolaire_ajuste['F'] = niveau_scolaire_ajuste_F
niveau_scolaire_ajuste['M'] = niveau_scolaire_ajuste_M
niveau_scolaire_ajuste['B'] = niveau_scolaire_ajuste_B
niveau_scolaire_ajuste['TB'] = niveau_scolaire_ajuste_TB

#Regles

tab_niveau_scolaire_ajuste = [
    # Score académique global
    #"TF"  "F"   "M"   "B"   "TB"
    ['TF', 'TF', 'TF', 'F', 'M'],  # Score d'ajustement lycée-classe 'TF'
    ['TF', 'TF', 'F', 'M', 'B'],  # Score d'ajustement lycée-classe 'F'
    ['TF', 'TF', 'F', 'M', 'TB'],  # Score d'ajustement lycée-classe 'M'
    ['TF', 'TF', 'M', 'B', 'TB'],  # Score d'ajustement lycée-classe 'B'
    ['TF', 'F', 'M', 'TB', 'TB'],  # Score d'ajustement lycée-classe 'TB'
]



liste_regles = []

for x, score_ajustement_lycee_classe_label  in enumerate(['TF', 'F', 'M', 'B', 'TB']):
    for y, score_academique_global_label  in enumerate(['TF', 'F', 'M', 'B', 'TB']):
        # Définir le niveau scolaire ajusté cible
        niveau_scolaire_ajuste_target = tab_niveau_scolaire_ajuste[x][y]
        
        # Créer une règle
        rule = ctrl.Rule(
            score_academique_global[score_academique_global_label] & 
            score_ajustement_lycee_classe[score_ajustement_lycee_classe_label], 
            niveau_scolaire_ajuste[niveau_scolaire_ajuste_target]
        )
       
        liste_regles.append(rule)
        
# Créer le système de contrôle
niveau_scolaire_ajuste_ctrl = ctrl.ControlSystem(liste_regles)

# Créer la simulation
niveau_scolaire_ajuste_sim = ctrl.ControlSystemSimulation(niveau_scolaire_ajuste_ctrl)

#FIN SF6




#SF7
#Entrees
#engagement
engagement = ctrl.Antecedent(x_engagement, 'engagement')

engagement['TF'] = engagement_TF
engagement['F'] = engagement_F
engagement['M'] = engagement_M
engagement['B'] = engagement_B
engagement['E'] = engagement_E
#Motivation
motivation = ctrl.Antecedent(x_motivation, 'motivation')

motivation['TF'] = motivation_TF
motivation['F'] = motivation_F
motivation['M'] = motivation_M
motivation['B'] = motivation_B
motivation['TB'] = motivation_TB
#sortie
#predisposition academique
x_predisposition_academique = np.arange(0, 1.25, 0.25)

predisposition_academique_TF = fuzz.trimf(x_predisposition_academique, [0, 0, 0.25])
predisposition_academique_F = fuzz.trimf(x_predisposition_academique, [0, 0.25, 0.5])
predisposition_academique_M = fuzz.trimf(x_predisposition_academique, [0.25, 0.5, 0.75])
predisposition_academique_B = fuzz.trimf(x_predisposition_academique, [0.5, 0.75, 1])
predisposition_academique_TB = fuzz.trimf(x_predisposition_academique, [0.75, 1, 1])

predisposition_academique = ctrl.Consequent(x_predisposition_academique, 'predisposition_academique')

predisposition_academique['TF'] = predisposition_academique_TF
predisposition_academique['F'] = predisposition_academique_F
predisposition_academique['M'] = predisposition_academique_M
predisposition_academique['B'] = predisposition_academique_B
predisposition_academique['TB'] = predisposition_academique_TB

#Regles

tab_predisposition_academique = [
    # Engagement
    #"TF"  "F"   "M"   "B"   "E"
    ['TF', 'TF', 'TF', 'F', 'F'],  # Motivation 'TF'
    ['TF', 'TF', 'F', 'F', 'M'],  # Motivation 'F'
    ['F', 'F', 'M', 'M', 'B'],  # Motivation 'M'
    ['M', 'B', 'B', 'B', 'TB'],  # Motivation 'B'
    ['B', 'B', 'B', 'TB', 'TB'],  # Motivation 'TB'
]



liste_regles = []

for x, motivation_label in enumerate(['TF', 'F', 'M', 'B', 'TB']):
    for y, engagement_label in enumerate(['TF', 'F', 'M', 'B', 'E']):
        # Définir la predisposition academique cible
        predisposition_academique_target = tab_predisposition_academique[x][y]
        
        # Créer une règle
        rule = ctrl.Rule(
            engagement[engagement_label] & 
            motivation[motivation_label], 
            predisposition_academique[predisposition_academique_target]
        )
        
        liste_regles.append(rule)
        
# Créer le système de contrôle
predisposition_academique_ctrl = ctrl.ControlSystem(liste_regles)

# Créer la simulation
predisposition_academique_sim = ctrl.ControlSystemSimulation(predisposition_academique_ctrl)

#FIN SF7




#SF8
#Entrees
#predisposition academique
predisposition_academique = ctrl.Antecedent(x_predisposition_academique, 'predisposition_academique')

predisposition_academique['TF'] = predisposition_academique_TF
predisposition_academique['F'] = predisposition_academique_F
predisposition_academique['M'] = predisposition_academique_M
predisposition_academique['B'] = predisposition_academique_B
predisposition_academique['TB'] = predisposition_academique_TB

#niveau scolaire ajusté
niveau_scolaire_ajuste = ctrl.Antecedent(x_niveau_scolaire_ajuste, 'niveau_scolaire_ajuste')

niveau_scolaire_ajuste['TF'] = niveau_scolaire_ajuste_TF
niveau_scolaire_ajuste['F'] = niveau_scolaire_ajuste_F
niveau_scolaire_ajuste['M'] = niveau_scolaire_ajuste_M
niveau_scolaire_ajuste['B'] = niveau_scolaire_ajuste_B
niveau_scolaire_ajuste['TB'] = niveau_scolaire_ajuste_TB

#sortie
#Score de l'élève
x_score_eleve = np.arange(0, 1.25, 0.25)

score_eleve_TF = fuzz.trimf(x_score_eleve, [0, 0, 0.25])
score_eleve_F = fuzz.trimf(x_score_eleve, [0, 0.25, 0.5])
score_eleve_M = fuzz.trimf(x_score_eleve, [0.25, 0.5, 0.75])
score_eleve_B = fuzz.trimf(x_score_eleve, [0.5, 0.75, 1])
score_eleve_TB = fuzz.trimf(x_score_eleve, [0.75, 1, 1])
#afficher les fonctions d'appartenance
# fig, ax = plt.subplots()
# ax.plot(x_score_eleve, score_eleve_TF, 'b', linewidth=1.5, label='TF')
# ax.plot(x_score_eleve, score_eleve_F, 'g', linewidth=1.5, label='F')
# ax.plot(x_score_eleve, score_eleve_M, 'r', linewidth=1.5, label='M')
# ax.plot(x_score_eleve, score_eleve_B, 'y', linewidth=1.5, label='B')

# ax.plot(x_score_eleve, score_eleve_TB, 'm', linewidth=1.5, label='TB')

# ax.set_title('Score de l\'élève')
# ax.legend()
# plt.show()
score_eleve = ctrl.Consequent(x_score_eleve, 'score_eleve')

score_eleve['TF'] = score_eleve_TF
score_eleve['F'] = score_eleve_F
score_eleve['M'] = score_eleve_M
score_eleve['B'] = score_eleve_B
score_eleve['TB'] = score_eleve_TB
#Regles

tab_score_eleve = [
    # predisposition academique
    #"TF"  "F"   "M"   "B"   "TB"
    ['TF', 'TF', 'TF', 'TF', 'TF'],  # Niveau scolaire ajusté 'TF'
    ['TF', 'TF', 'TF', 'F', 'F'],  # Niveau scolaire ajusté 'F'
    ['TF', 'F', 'M', 'M', 'B'],  # Niveau scolaire ajusté 'M'
    ['F', 'M', 'B', 'B', 'TB'],  # Niveau scolaire ajusté 'B'
    ['M', 'B', 'B', 'TB', 'TB'],  # Niveau scolaire ajusté 'TB'
]


liste_regles = []

for x, niveau_scolaire_ajuste_label in enumerate(['TF', 'F', 'M', 'B', 'TB']):
    for y,predisposition_academique_label  in enumerate(['TF', 'F', 'M', 'B', 'TB']):
        # Définir le score de l'élève cible
        score_eleve_target = tab_score_eleve[x][y]
        
        # Créer une règle
        rule = ctrl.Rule(
            predisposition_academique[predisposition_academique_label] & 
            niveau_scolaire_ajuste[niveau_scolaire_ajuste_label], 
            score_eleve[score_eleve_target]
        )

        liste_regles.append(rule)

# Créer le système de contrôle
score_eleve_ctrl = ctrl.ControlSystem(liste_regles)

# Créer la simulation
score_eleve_sim = ctrl.ControlSystemSimulation(score_eleve_ctrl)

#FIN SF8


systemes_flous_dico = {
    'engagement': [engagement_sim, x_engagement, [engagement_TF, engagement_F, engagement_M, engagement_B, engagement_E]],
    'motivation': [motivation_sim, x_motivation, [motivation_TF, motivation_F, motivation_M, motivation_B, motivation_TB]], 
    'score_academique_global': [score_academique_global_sim, x_score_academique_global, [score_academique_global_TF, score_academique_global_F, score_academique_global_M, score_academique_global_B, score_academique_global_TB]],
    'score_ajustement_lycee_classe': [score_ajustement_lycee_classe_sim, x_score_ajustement_lycee_classe, [score_ajustement_lycee_classe_TF, score_ajustement_lycee_classe_F, score_ajustement_lycee_classe_M, score_ajustement_lycee_classe_B, score_ajustement_lycee_classe_TB]],
    'niveau_scolaire_ajuste': [niveau_scolaire_ajuste_sim, x_niveau_scolaire_ajuste, [niveau_scolaire_ajuste_TF, niveau_scolaire_ajuste_F, niveau_scolaire_ajuste_M, niveau_scolaire_ajuste_B, niveau_scolaire_ajuste_TB]],
    'predisposition_academique': [predisposition_academique_sim, x_predisposition_academique, [predisposition_academique_TF, predisposition_academique_F, predisposition_academique_M, predisposition_academique_B, predisposition_academique_TB]],
    'score_eleve': [score_eleve_sim, x_score_eleve, [score_eleve_TF, score_eleve_F, score_eleve_M, score_eleve_B, score_eleve_TB]]
}

import pickle

with open('systemes_flous.pkl', 'wb') as f:
    pickle.dump(systemes_flous_dico, f)
    
print("Systèmes flous sauvegardés dans 'systemes_flous.pkl'")