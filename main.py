if __name__ == "__main__":
    import pickle
    import numpy as np
    import skfuzzy as fuzz
    from Systeme_flou import SystemeFlou, defuzzification
    with open('systemes_flous.pkl', 'rb') as f:
        systemes_flous = pickle.load(f)
        #engagement, motivation, score_academique_global, score_ajustement_lycee_classe, niveau_scolaire_ajuste, predisposition_academique, score_eleve
    
    # Variables
    activites_sportives = 1           # compris entre 0 et 1
    activites_sociales = 0            # compris entre 0 et 1.5
    projet_personnel = 0            # compris entre 0 et 1.5
    appreciation_des_professeurs = 0.7  # compris entre 0 et 1
    potentiel_academique_percu = 0.3    # compris entre 0 et 1
    motivation_percue = 1              # compris entre 0 et 1
    qualite_lettre_de_motivation = 0.9    # compris entre 0 et 1
    resultat_scolaire = 18          # compris entre 0 et 20 (moyenne générale)
    niveau_scientifique = 18            # compris entre 0 et 20
    niveau_litteraire = 14           # compris entre 0 et 20
    niveau_lycee = 0.6                 # compris entre 0 et 1
    niveau_classe = 0.8                 # compris entre 0 et 1
    classement_eleve = 0.7        # compris entre 0 et 1 (0 = bas, 1 = haut)
    
    
    
    # Compute CAF1
    activites_extrascolaires = activites_sportives + activites_sociales + projet_personnel

    print(f"Output of CAF1 - Activités Extrascolaires: {activites_extrascolaires}")

    # Compute SF2 (Engagement)
    # Set inputs for SF2
    valeur_entrees = {
        "potentiel_academique_percu": potentiel_academique_percu,
        "activites_extrascolaires": activites_extrascolaires/4,  # Output from SF1
        "appreciation_des_professeurs": appreciation_des_professeurs
    }
    
    # Compute SF2
    valeur_fuzzifier = systemes_flous["engagement"][0].fuzzifier(valeur_entrees)
    engagement = systemes_flous["engagement"][0].compute(valeur_fuzzifier)
    print(f"Output of SF2 - Engagement: {engagement}")

    # Compute SF3 (Motivation
    # Set inputs for SF3
    valeur_entrees = {
        "motivation_percue": motivation_percue,
        "qualite_lettre_de_motivation": qualite_lettre_de_motivation
    }

    # Compute SF3
    valeur_fuzzifier = systemes_flous["motivation"][0].fuzzifier(valeur_entrees)
    motivation = systemes_flous["motivation"][0].compute(valeur_fuzzifier)
    print(f"Output of SF3 - Motivation: {motivation}")

    # Compute SF4 (Score Académique Global)
    # Set inputs for SF4
    
    valeur_entrees = {
        "resultat_scolaire": resultat_scolaire,
        "niveau_scientifique": niveau_scientifique,
        "niveau_litteraire": niveau_litteraire
    }
    # Compute SF4
    valeur_fuzzifier = systemes_flous["score_academique_global"][0].fuzzifier(valeur_entrees)
    score_academique_global = systemes_flous["score_academique_global"][0].compute(valeur_fuzzifier)
    print(f"Output of SF4 - Score Académique Global: {score_academique_global}")

    # Compute SF5 (Score Ajustement Lycée-Classe)
    # Set inputs for SF5
    valeur_entrees = {
        "niveau_lycee": niveau_lycee,
        "niveau_classe": niveau_classe,
        "classement_eleve": classement_eleve
    }
    # Compute SF5
    valeur_fuzzifier = systemes_flous["score_ajustement_lycee_classe"][0].fuzzifier(valeur_entrees)
    # print("valeur fuzz: ",valeur_fuzzifier)
    score_ajustement_lycee_classe = systemes_flous["score_ajustement_lycee_classe"][0].compute(valeur_fuzzifier)
    print(f"Output of SF5 - Score d'ajustement lycée-classe: {score_ajustement_lycee_classe}")

    # Compute SF6 (Niveau Scolaire Ajusté)
    # Set inputs for SF6
    valeur_fuzzifier = {
        "score_academique_global": score_academique_global,
        "score_ajustement_lycee_classe": score_ajustement_lycee_classe
    }
    
    # Compute SF6
    niveau_scolaire_ajuste = systemes_flous["niveau_scolaire_ajuste"][0].compute(valeur_fuzzifier)
    print(f"Output of SF6 - Niveau scolaire ajusté: {niveau_scolaire_ajuste}")

    # Compute SF7 (Prédisposition Académique)
    # Set inputs for SF7
    valeur_fuzzifier = {
        "engagement": engagement,
        "motivation": motivation
    }
    # Compute SF7
    
    predisposition_academique = systemes_flous["predisposition_academique"][0].compute(valeur_fuzzifier)
    print(f"Output of SF7 - Prédisposition Académique: {predisposition_academique}")

    # Compute SF8 (Score de l'Élève)
    # Set inputs for SF8
    valeur_fuzzifier = {
        "predisposition_academique": predisposition_academique,
        "niveau_scolaire_ajuste": niveau_scolaire_ajuste
    }
    # Compute SF8
    score_final = systemes_flous["score_eleve"][0].compute(valeur_fuzzifier)
    score_final = defuzzification(score_final) * 100
    
    print(f"Output of SF8 - Score de l'Élève: {score_final}")
