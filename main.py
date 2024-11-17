if __name__ == "__main__":
    import pickle
    
    with open('systemes_flous.pkl', 'rb') as f:
        systemes_flous = pickle.load(f)
        #engagement, motivation, score_academique_global, score_ajustement_lycee_classe, niveau_scolaire_ajuste, predisposition_academique, score_eleve
    
    # Variables
    activites_sportives = 0             # compris entre 0 et 1
    activites_sociales = 1.5            # compris entre 0 et 1.5
    projet_personnel = 0                # compris entre 0 et 1.5
    appreciation_des_professeurs = 1.5  # compris entre -2 et 3.5
    potentiel_academique_percu = 0.5    # compris entre -2 et 3
    motivation_percue = 7               # compris entre 0 et 9
    qualite_lettre_de_motivation = 8    # compris entre 0 et 9
    resultat_scolaire = 15              # compris entre 0 et 20 (moyenne générale)
    niveau_scientifique = 14            # compris entre 0 et 20
    niveau_litteraire = 13              # compris entre 0 et 20
    niveau_lycee = 1.5                  # compris entre 0 et 2
    niveau_classe = 1.0                 # compris entre 0 et 2
    classement_eleve = 0.3              # compris entre 0 et 1
    
    
    
    # Compute SF1
    activites_extrascolaires = activites_sportives + activites_sociales + projet_personnel
    print(f"Output of SF1 - Activités Extrascolaires: {activites_extrascolaires}")

    # Compute SF2 (Engagement)
    # Set inputs for SF2
    systemes_flous["engagement"].input['appreciation_des_professeurs'] = appreciation_des_professeurs  
    systemes_flous["engagement"].input['potentiel_academique_percu'] = potentiel_academique_percu
    systemes_flous["engagement"].input['activites_extrascolaires'] = activites_extrascolaires  # Output from SF1

    # Compute SF2
    systemes_flous["engagement"].compute()
    engagement = systemes_flous["engagement"].output['engagement']
    print(f"Output of SF2 - Engagement: {engagement}")

    # Compute SF3 (Motivation)
    # Set inputs for SF3
    systemes_flous["motivation"].input['motivation_percue'] = motivation_percue 
    systemes_flous["motivation"].input['qualite_lettre_de_motivation'] = qualite_lettre_de_motivation

    # Compute SF3
    systemes_flous["motivation"].compute()
    motivation = systemes_flous["motivation"].output['motivation']
    print(f"Output of SF3 - Motivation: {motivation}")

    # Compute SF4 (Score Académique Global)
    # Set inputs for SF4
    systemes_flous["score_academique_global"].input['resultat_scolaire'] = resultat_scolaire
    systemes_flous["score_academique_global"].input['niveau_scientifique'] = niveau_scientifique
    systemes_flous["score_academique_global"].input['niveau_litteraire'] = niveau_litteraire

    # Compute SF4
    systemes_flous["score_academique_global"].compute()
    score_academique_global = systemes_flous["score_academique_global"].output['score_academique_global']
    print(f"Output of SF4 - Score Académique Global: {score_academique_global}")

    # Compute SF5 (Score Ajustement Lycée-Classe)
    # Set inputs for SF5
    systemes_flous["score_ajustement_lycee_classe"].input['niveau_lycee'] = niveau_lycee
    systemes_flous["score_ajustement_lycee_classe"].input['niveau_classe'] = niveau_classe  # Moyen
    systemes_flous["score_ajustement_lycee_classe"].input['classement_eleve'] = classement_eleve  # Haut

    # Compute SF5
    systemes_flous["score_ajustement_lycee_classe"].compute()
    score_ajustement_lycee_classe = systemes_flous["score_ajustement_lycee_classe"].output['score_ajustement_lycee_classe']
    print(f"Output of SF5 - Score d'ajustement lycée-classe: {score_ajustement_lycee_classe}")

    # Compute SF6 (Niveau Scolaire Ajusté)
    # Set inputs for SF6
    systemes_flous["niveau_scolaire_ajuste"].input['score_academique_global'] = score_academique_global
    systemes_flous["niveau_scolaire_ajuste"].input['score_ajustement_lycee_classe'] = score_ajustement_lycee_classe

    # Compute SF6
    systemes_flous["niveau_scolaire_ajuste"].compute()
    niveau_scolaire_ajuste = systemes_flous["niveau_scolaire_ajuste"].output['niveau_scolaire_ajuste']
    print(f"Output of SF6 - Niveau scolaire ajusté: {niveau_scolaire_ajuste}")

    # Compute SF7 (Prédisposition Académique)
    # Set inputs for SF7
    systemes_flous["predisposition_academique"].input['engagement'] = engagement
    systemes_flous["predisposition_academique"].input['motivation'] = motivation

    # Compute SF7
    systemes_flous["predisposition_academique"].compute()
    predisposition_academique = systemes_flous["predisposition_academique"].output['predisposition_academique']
    print(f"Output of SF7 - Prédisposition Académique: {predisposition_academique}")

    # Compute SF8 (Score de l'Élève)
    # Set inputs for SF8
    systemes_flous["score_eleve"].input['predisposition_academique'] = predisposition_academique
    systemes_flous["score_eleve"].input['niveau_scolaire_ajuste'] = niveau_scolaire_ajuste

    # Compute SF8
    systemes_flous["score_eleve"].compute()
    score_final = systemes_flous["score_eleve"].output['score_eleve']
    print(f"Output of SF8 - Score de l'Élève: {score_final}")
