import numpy as np

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




def dict_to_arrays(fuzzy_dict, x_max=1):
        """
        Transforme un dictionnaire flou en deux np.array pour défuzzification.
        - fuzzy_dict : dict, les clés représentent les valeurs de l'univers
        (par exemple : 'TF', 'F', 'M', 'B', 'TB') et les valeurs sont 
        les degrés d'appartenance (flottants).

        Retourne :
        - x : np.array, les valeurs de l'univers sous forme numérique.
        - y : np.array, les degrés d'appartenance correspondants.
        """
        # x est l'univers de définition
        x = np.linspace(0, x_max, num=len(fuzzy_dict), endpoint=True)
        # y est la liste des degrés d'appartenance
        y = np.array(list(fuzzy_dict.values()), dtype=np.float64)
        
        return x, y
    

def normalisation(fuzzy_dict, x_max=1):
    """
    Normalise les degrés d'appartenance d'un dictionnaire flou sous la forme {clé1: valeur1, clé2:valeur2, ... clé:valeur}.
    - fuzzy_dict : dict, les clés représentent les valeurs de l'univers
        (par exemple : 'TF', 'F', 'M', 'B', 'TB') et les valeurs sont 
        les degrés d'appartenance (flottants).
    - x_max : float, la valeur maximale de l'univers de définition.
    """
    # Conversion du dictionnaire flou en np.array
    x, y = dict_to_arrays(fuzzy_dict, x_max)
    
    # Normalisation 
    y_norm = (y / np.max(y)) * x_max
    
    # mettre a jour le dictionnaire flou avec les nouvelles valeurs normalisées
    for i, key in enumerate(fuzzy_dict.keys()):
        fuzzy_dict[key] = y_norm[i]
        
    return fuzzy_dict

def defuzzification(fuzzy_dict, gamma=3):
    """
    Défuzzification par méthode paramétrée ZZ-gamma.
    - fuzzy_dict : dict, les clés représentent les valeurs de l'univers
        (par exemple : 'TF', 'F', 'M', 'B', 'TB') et les valeurs sont 
        les degrés d'appartenance (flottants).
    - gamma : float ou int, paramètre de la méthode ZZ-gamma.
    """
    # Conversion du dictionnaire flou en np.array
    x, y = dict_to_arrays(fuzzy_dict)
    # Calcul du numérateur et du dénominateur suivant la formule ZZ-gamma
    numerateur = np.sum(x * y**gamma)
    denominateur = np.sum(y**gamma)
    
    # Éviter la division par zéro (c'est mieux)
    if denominateur == 0:
        raise ValueError("La somme des degrés d'appartenance est nulle. Impossible d'effectuer une defuzzification.")
    
    # Calcul et retour du ZZ-gamma
    return numerateur / denominateur

class NombreFlou:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

def calcul_point_intersection_de_droites(a1, b1, a2, b2):
    """
    Calcule le point d'intersection de deux droites définies par leurs coordonnées.

    Paramètres :
    a1, b1 : float - coordonnées de la première droite (x pour y=0 et y=1).
    a2, b2 : float - coordonnées de la deuxième droite (x pour y=0 et y=1).

    Retourne :
    tuple (x, y) - coordonnées du point d'intersection ou None si les droites sont parallèles.
    """
    if a1 == b1 or a2 == b2:
        if a1 == b1 and a2 == b2:
            if a1 == a2:
                return (a1, 1)
            
        elif b1 == a1:
            m2 = 1/(b2 - a2)
            c2 = a2 * m2 * -1
            y = m2 * a1 + c2
            if 0 <= y <= 1:
                return (a1, y)
            
        elif b2 == a2:
            m1 = 1/(b1 - a1)
            c1 = a1 * m1 * -1
            y = m1 * a2 + c1
            if 0 <= y <= 1:
                return (a2, y)
            
        return None
    
    # Calcul des pentes (m1 et m2) et des ordonnées à l'origine (c1 et c2)
    m1 = 1/(b1 - a1)
    c1 = a1 * m1 * -1
    m2 = 1/(b2 - a2)
    c2 = a2 * m2 * -1

    # Vérifier si les droites sont parallèles (même pente)
    if m1 == m2:
        if c1 == c2: # Les droites sont confondues
            return (b1, 1)
        
        return None  # Les droites sont parallèles et ne se croisent pas

    # Calcul de l'intersection (x, y)
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1
    
    if 0 <= y <= 1:
        return (x, y)
    
    return None

def calcul_degre(valeur, univers, ensemble):
    """
    Calcule le degré d'appartenance de `valeur` à un ensemble flou défini par `univers` et `ensemble`.

    - valeur : valeur précise à évaluer.
    - univers : liste des points de l'univers de définition (les x de l'univers)
    - ensemble : liste des degrés d'appartenance correspondants (les y en fonction de x).

    Retourne : float degré d'appartenance de `valeur`.
    """
    
    if type(valeur) == NombreFlou:
        # valeur est un nombre flou de la forme d'une trimf: (x,y,z)
        if valeur.a >= univers[-1]:
            return ensemble[0]
        if valeur.c <= univers[0]:
            return ensemble[-1]
        
        resultats = []
        for i in range(len(univers)-1):
            
            if ensemble[i] == 0 and ensemble[i + 1] == 1:
                p1 = calcul_point_intersection_de_droites(univers[i], univers[i + 1], valeur.a, valeur.b)
                p2 = calcul_point_intersection_de_droites(univers[i], univers[i + 1], valeur.c, valeur.b)
                
                if p1 is not None and p2 is not None:
                    resultats.append(max(p1[1], p2[1]))
                elif p1 is not None:
                    resultats.append(p1[1])
                elif p2 is not None:
                    resultats.append(p2[1])
                else:
                    resultats.append(0)

            elif ensemble[i] == 1 and ensemble[i + 1] == 0:
                p1 = calcul_point_intersection_de_droites(univers[i + 1], univers[i], valeur.a, valeur.b)
                p2 = calcul_point_intersection_de_droites(univers[i + 1], univers[i], valeur.c, valeur.b)
                if p1 is not None and p2 is not None:
                    resultats.append(max(p1[1], p2[1]))
                elif p1 is not None:
                    resultats.append(p1[1])
                elif p2 is not None:
                    resultats.append(p2[1])
                else:
                    resultats.append(0)
        return max(resultats)
        
                
    #Sinon la valeur est un nombre net:       
                    
    # Si la valeur est en dehors de l'univers, retourner la valeur extrême
    if valeur <= univers[0]:
        return ensemble[0]
    if valeur >= univers[-1]:
        return ensemble[-1]

    # Trouver l'intervalle dans lequel se situe la valeur
    for i in range(len(univers) - 1):
        if univers[i] <= valeur <= univers[i + 1]:
            
            if ensemble[i] == 0 and ensemble[i+1] == 0:
                    return 0
                
            # Interpolation linéaire
            x0, x1 = univers[i], univers[i + 1]
            y0, y1 = ensemble[i], ensemble[i + 1]
            
            # Formule de l'interpolation linéaire
            degre = y0 + (valeur - x0) * (y1 - y0) / (x1 - x0)
            return degre


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