import numpy as np

# Définition des fonctions d'appartenance
def trimf(x, points):
    """
    Fonction d'appartenance triangulaire.
    x : valeurs sur l'univers
    points : trois points définissant le triangle (a, b, c)
    """
    if len(points) != 3:
        raise ValueError("La fonction trimf attend trois points.")
    #division par zéro
    
    a, b, c = points
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

def trapmf(x, points):
    """
    Fonction d'appartenance trapézoïdale.
    x : valeurs sur l'univers
    points : quatre points définissant le trapèze (a, b, c, d)
    """
    if len(points) != 4:
        raise ValueError("La fonction trapmf attend quatre points.")
    a, b, c, d = points
    return np.maximum(0, np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)))

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
                    degre = np.interp(valeur, self.variables_entree[var]["univers"], ensemble)
                    fuzzified_values[var][etat] = degre
        return fuzzified_values

    def evaluer_regles(self, valeurs_fuzzifiees, operateur=min):
        """
        Évalue les règles floues en utilisant les valeurs fuzzifiées.
        """
        conclusions = []
        for regle in self.regles:
            activation = []
            for var, etat in regle["conditions"].items():
                activation.append(valeurs_fuzzifiees[var][etat])
            degre_activation = operateur(activation)
            conclusions.append((degre_activation, regle["conclusion"]))
        return conclusions


if __name__ == "__main__":
    # Initialiser le système
    systeme = SystemeFlou()

    # Définir l'univers
    x_temperature = np.linspace(0, 100, 100)

    # Définir des ensembles flous à l'aide de trimf
    temperature_bas = trimf(x_temperature, [0, 0, 50])
    temperature_moyen = trimf(x_temperature, [25, 50, 75])
    temperature_eleve = trimf(x_temperature, [50, 100, 100])
    print(temperature_bas)
    # Ajouter une variable d'entrée
    systeme.ajouter_variable_entree(
        "temperature",
        x_temperature,
        {"bas": temperature_bas, "moyen": temperature_moyen, "eleve": temperature_eleve},
    )

    # Définir l'univers de sortie
    x_ventilateur = np.linspace(0, 100, 100)

    # Définir des ensembles flous pour la sortie
    ventilateur_lent = trimf(x_ventilateur, [0, 0, 50])
    ventilateur_moyen = trimf(x_ventilateur, [25, 50, 75])
    ventilateur_rapide = trimf(x_ventilateur, [50, 100, 100])

    # Ajouter une variable de sortie
    systeme.ajouter_variable_sortie(
        "ventilateur",
        x_ventilateur,
        {"lent": ventilateur_lent, "moyen": ventilateur_moyen, "rapide": ventilateur_rapide},
    )

    # Ajouter des règles
    systeme.ajouter_regle({"temperature": "bas"}, {"ventilateur": "lent"})
    systeme.ajouter_regle({"temperature": "moyen"}, {"ventilateur": "moyen"})
    systeme.ajouter_regle({"temperature": "eleve"}, {"ventilateur": "rapide"})

    # Entrées
    valeurs_entree = {"temperature": 30}
    valeurs_fuzzifiees = systeme.fuzzifier(valeurs_entree)

    # Évaluation des règles
    conclusions = systeme.evaluer_regles(valeurs_fuzzifiees)

    print("Valeurs fuzzifiées :", valeurs_fuzzifiees)
    print("Conclusions :", conclusions)
