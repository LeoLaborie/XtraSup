import numpy as np
import pandas as pd
from Systeme_flou import defuzzification, normalisation
import pickle

# Charger les systèmes flous depuis le fichier pickle
with open('systemes_flous.pkl', 'rb') as f:
    systemes_flous = pickle.load(f)

# Définir le nombre d'élèves
NB_ELEVES = 8000

def calculer_score_eleve(eleve):
    """
    Calcule le score de l'élève en fonction des données fournies.
    """
    
    # Récupérer les données de l'élève
    activites_sportives = eleve["activites_sportives"]
    activites_sociales = eleve["activites_sociales"]
    projet_personnel = eleve["projet_personnel"]
    appreciation_des_professeurs = eleve["appreciation_des_professeurs"]
    potentiel_academique_percu = eleve["potentiel_academique_percu"]
    motivation_percue = eleve["motivation_percue"]
    qualite_lettre_de_motivation = eleve["qualite_lettre_de_motivation"]
    resultat_scolaire = eleve["resultat_scolaire"]
    niveau_scientifique = eleve["niveau_scientifique"]
    niveau_litteraire = eleve["niveau_litteraire"]
    niveau_lycee = eleve["niveau_lycee"]
    niveau_classe = eleve["niveau_classe"]
    classement_eleve = eleve["classement_eleve"]
    
    
        # Compute CAF1
    activites_extrascolaires = activites_sportives + activites_sociales + projet_personnel

    # Compute SF1 (Engagement)
    # Set inputs for SF1
    valeur_entrees = {
        "potentiel_academique_percu": potentiel_academique_percu,
        "activites_extrascolaires": activites_extrascolaires/4,  # Output from SF1
        "appreciation_des_professeurs": appreciation_des_professeurs
    }
    
    # Compute SF1
    valeur_fuzzifier = systemes_flous["engagement"][0].fuzzifier(valeur_entrees)
    engagement = systemes_flous["engagement"][0].compute(valeur_fuzzifier)

    #normalisation
    engagement = normalisation(engagement, systemes_flous["engagement"][1][-1])

    # Compute SF2 (Motivation
    # Set inputs for SF2
    valeur_entrees = {
        "motivation_percue": motivation_percue,
        "qualite_lettre_de_motivation": qualite_lettre_de_motivation
    }

    # Compute SF2
    valeur_fuzzifier = systemes_flous["motivation"][0].fuzzifier(valeur_entrees)
    motivation = systemes_flous["motivation"][0].compute(valeur_fuzzifier)

    #normalisation
    motivation = normalisation(motivation, systemes_flous["motivation"][1][-1])
    
    # Compute SF3 (Score Académique Global)
    # Set inputs for SF3
    
    valeur_entrees = {
        "resultat_scolaire": resultat_scolaire,
        "niveau_scientifique": niveau_scientifique,
        "niveau_litteraire": niveau_litteraire
    }
    # Compute SF3
    valeur_fuzzifier = systemes_flous["score_academique_global"][0].fuzzifier(valeur_entrees)
    score_academique_global = systemes_flous["score_academique_global"][0].compute(valeur_fuzzifier)

    #normalisation
    score_academique_global = normalisation(score_academique_global, systemes_flous["score_academique_global"][1][-1])
    # Compute SF4 (Score Ajustement Lycée-Classe)
    # Set inputs for SF4
    valeur_entrees = {
        "niveau_lycee": niveau_lycee,
        "niveau_classe": niveau_classe,
        "classement_eleve": classement_eleve
    }
    # Compute SF4
    valeur_fuzzifier = systemes_flous["score_ajustement_lycee_classe"][0].fuzzifier(valeur_entrees)
    score_ajustement_lycee_classe = systemes_flous["score_ajustement_lycee_classe"][0].compute(valeur_fuzzifier)

    #normalisation
    score_ajustement_lycee_classe = normalisation(score_ajustement_lycee_classe, systemes_flous["score_ajustement_lycee_classe"][1][-1])
    # Compute SF5 (Niveau Scolaire Ajusté)
    # Set inputs for SF5
    valeur_fuzzifier = {
        "score_academique_global": score_academique_global,
        "score_ajustement_lycee_classe": score_ajustement_lycee_classe
    }
    
    # Compute SF5
    niveau_scolaire_ajuste = systemes_flous["niveau_scolaire_ajuste"][0].compute(valeur_fuzzifier)

    #normalisation
    niveau_scolaire_ajuste = normalisation(niveau_scolaire_ajuste, systemes_flous["niveau_scolaire_ajuste"][1][-1])
    
    # Compute SF6 (Prédisposition Académique)
    # Set inputs for SF6
    valeur_fuzzifier = {
        "engagement": engagement,
        "motivation": motivation
    }
    # Compute SF6
    
    predisposition_academique = systemes_flous["predisposition_academique"][0].compute(valeur_fuzzifier)

    #normalisation
    predisposition_academique = normalisation(predisposition_academique, systemes_flous["predisposition_academique"][1][-1])
    # Compute SF7 (Score de l'Élève)
    # Set inputs for SF7
    valeur_fuzzifier = {
        "predisposition_academique": predisposition_academique,
        "niveau_scolaire_ajuste": niveau_scolaire_ajuste
    }
    # Compute SF7
    score_final = systemes_flous["score_eleve"][0].compute(valeur_fuzzifier)
    score_final = defuzzification(score_final) * 100
    

    return score_final

def generer_donnees_eleves(nb_eleves):
    """
    Génère un DataFrame contenant les données aléatoires pour un ensemble d'élèves.
    """
    # Générer les colonnes avec les plages définies
    data = {
        "activites_sportives": np.random.choice([0, 1], nb_eleves),
        "activites_sociales": np.random.choice([0, 1.5], nb_eleves),
        "projet_personnel": np.random.choice([0, 1.5], nb_eleves),
        "appreciation_des_professeurs": np.round(np.random.uniform(0, 1, nb_eleves), 2),
        "potentiel_academique_percu": np.round(np.random.uniform(0, 1, nb_eleves), 2),
        "motivation_percue": np.round(np.random.uniform(0, 1, nb_eleves), 2),
        "qualite_lettre_de_motivation": np.round(np.random.uniform(0, 1, nb_eleves), 2),
        "resultat_scolaire": np.round(np.random.uniform(5, 20, nb_eleves), 2),
        "niveau_scientifique": np.round(np.random.uniform(5, 20, nb_eleves), 2),
        "niveau_litteraire": np.round(np.random.uniform(5, 20, nb_eleves), 2),
        "niveau_lycee": np.round(np.random.uniform(0, 1, nb_eleves), 2),
        "niveau_classe": np.round(np.random.uniform(0, 1, nb_eleves), 2),
        "classement_eleve": np.round(np.random.uniform(0, 1, nb_eleves), 2)
    }
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Générer les données pour 8000 élèves
    eleves = generer_donnees_eleves(NB_ELEVES)

    # Calculer le score final pour chaque élève
    eleves["score_final"] = eleves.apply(calculer_score_eleve, axis=1)

    # Sauvegarder dans un fichier CSV
    eleves.to_csv("eleves.csv", index=False)

    # Afficher un aperçu des données générées
    print(eleves.head())
