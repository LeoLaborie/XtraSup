import numpy as np





def defuzzification(fuzzy_dict, gamma=3):
    """
    Défuzzification par méthode paramétrée ZZ-gamma.
    
    """
    
    
    def dict_to_arrays(fuzzy_dict):
        """
        Transforme un dictionnaire flou en deux np.array pour défuzzification.
        - fuzzy_dict : dict, les clés représentent les valeurs de l'univers
        (par exemple : 'TF', 'F', 'M', 'B', 'TB') et les valeurs sont 
        les degrés d'appartenance (flottants).

        Retourne :
        - x : np.array, les valeurs de l'univers sous forme numérique.
        - y : np.array, les degrés d'appartenance correspondants.
        """
        # Crée des indices numériques pour les clés, en respectant leur ordre
        x = np.linspace(0, 1, num=len(fuzzy_dict), endpoint=True)
        y = np.array(list(fuzzy_dict.values()), dtype=np.float64)
        
        return x, y
    
    # Conversion du dictionnaire flou en np.array
    x, y = dict_to_arrays(fuzzy_dict)
    # Calcul du numérateur et du dénominateur pour le barycentre
    numerateur = np.sum(x * y**gamma)
    denominateur = np.sum(y**gamma)
    
    # Éviter la division par zéro
    if denominateur == 0:
        raise ValueError("La somme des degrés d'appartenance est nulle. Impossible de calculer le barycentre.")
    
    # Calcul du barycentre
    return numerateur / denominateur


def calcul_degre(valeur, univers, ensemble):
    """
    Calcule le degré d'appartenance de `valeur` à un ensemble flou défini par `univers` et `ensemble`.

    - valeur : valeur précise à évaluer.
    - univers : liste des points de l'univers de définition (ex. : [0, 50, 100]).
    - ensemble : liste des degrés d'appartenance correspondants (ex. : [0, 0.5, 1]).

    Retourne : degré d'appartenance de `valeur`.
    """
    # Si la valeur est en dehors de l'univers, retourner la valeur extrême
    if valeur <= univers[0]:
        return ensemble[0]
    if valeur >= univers[-1]:
        return ensemble[-1]

    # Trouver l'intervalle dans lequel se situe la valeur
    for i in range(len(univers) - 1):
        if univers[i] <= valeur <= univers[i + 1]:
            # Interpolation linéaire
            x0, x1 = univers[i], univers[i + 1]
            y0, y1 = ensemble[i], ensemble[i + 1]
            
            # Formule de l'interpolation linéaire
            degre = y0 + (valeur - x0) * (y1 - y0) / (x1 - x0)
            return degre

# Définition des fonctions d'appartenance
def trimf(x, points):
    """
    Fonction d'appartenance triangulaire avec gestion des divisions par zéro.
    x : np.array des valeurs sur l'univers
    points : trois points définissant le triangle (a, b, c)
    Retourne un np.array de la même longueur que x.
    """
    a, b, c = points
    with np.errstate(divide='ignore', invalid='ignore'):
        y = np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))
    y[np.isnan(y)] = 1  # Remplace les NaN par 1
    return y

def trapmf(x, points):
    """
    Fonction d'appartenance trapézoïdale avec gestion des divisions par zéro.
    x : np.array des valeurs sur l'univers
    points : quatre points définissant le trapèze (a, b, c, d)
    Retourne un np.array de la même longueur que x.
    """
    a, b, c, d = points
    with np.errstate(divide='ignore', invalid='ignore'):
        y = np.maximum(
            0,
            np.minimum(
                np.minimum((x - a) / (b - a), 1),
                (d - x) / (d - c)
            )
        )
    y[np.isnan(y)] = 1  # Remplace les NaN par 1
    return y

class SystemeFlou:
    def __init__(self):
        self.variables_entree = {}  # Dictionnaire des variables d'entrée
        self.variables_sortie = {}  # Dictionnaire des variables de sortie
        self.regles = []  # Liste des règles floues

    def ajouter_variable_entree(self, nom, univers, fonctions_appartenance):
        """
        Ajoute une variable d'entrée au système flou.
        - nom : nom de la variable (str)
        - univers : np.array définissant les valeurs sur l'univers
        - fonctions_appartenance : dict avec des noms linguistiques et leurs ensembles flous
        """
        self.variables_entree[nom] = {"univers": univers, "fuzzy_sets": fonctions_appartenance}

    def ajouter_variable_sortie(self, nom, univers, fonctions_appartenance):
        """
        Ajoute une variable de sortie au système flou.
        """
        self.variables_sortie[nom] = {"univers": univers, "fuzzy_sets": fonctions_appartenance}

    def ajouter_regle(self, regle):
        """
        Ajoute une règle floue.
        - conditions : dict avec des variables d'entrée et leurs états linguistiques
        - conclusion : dict avec des variables de sortie et leurs états linguistiques
        """
        self.regles.append(regle)

    def fuzzifier(self, valeurs_entree):
        """
        Fuzzifie les valeurs d'entrée.
        - valeurs_entree : dict avec les noms des variables d'entrée et leurs valeurs précises
        - Retourne un dict contenant les degrés d'appartenance pour chaque état linguistique.
        """
        fuzzified_values = {}
        for var, valeur in valeurs_entree.items():
            if var in self.variables_entree:
                fuzzified_values[var] = {}
                for etat, ensemble in self.variables_entree[var]["fuzzy_sets"].items():
                    degre = calcul_degre(valeur, self.variables_entree[var]["univers"], ensemble)
                    fuzzified_values[var][etat] = degre
        return fuzzified_values

    def compute(self, valeurs_fuzzifiees, operateur=min):
        """
        Évalue les règles floues en utilisant les valeurs fuzzifiées.
        """
        conclusions = {}
        for regle in self.regles:
            activation = []
            for var, etat in regle["conditions"].items():
                activation.append(valeurs_fuzzifiees[var][etat])
            degre_activation = operateur(activation)
            
            already_in = False
            for consequence, degre in conclusions.items():
                if consequence == regle["conclusion"]:
                    if degre_activation >= degre:
                        conclusions[consequence] = round(degre_activation, 4)
                    already_in = True
                    
            if not already_in:
                # conclusions.append([round(degre_activation,4), regle["conclusion"]])
                conclusions[regle["conclusion"]] = round(degre_activation, 4)
        return conclusions


{
    'niveau_lycee': {
        'TI': np.float64(0.0), 'I': np.float64(0.0), 'M': np.float64(0.6000000000000001), 'B': np.float64(0.3999999999999999), 'TB': np.float64(0.0)
        }, 
    'niveau_classe': {
        'TI': np.float64(0.0), 'I': np.float64(0.0), 'M': np.float64(0.0), 'B': np.float64(0.0), 'TB': np.float64(1.0)
        }, 
    'classement_eleve': {
        'B': np.float64(0.0), 'M': np.float64(0.3999999999999999), 'H': np.float64(0.6000000000000001)
        }
}


{
    'score_academique_global': {
        'B': np.float64(0.2), 'TB': np.float64(0.8)
        }, 
    'score_ajustement_lycee_classe': {
        'B': np.float64(0.3999999999999999), 'TB': np.float64(0.6000000000000001)
        }
}