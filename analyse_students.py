import pandas as pd

NB_ELEVES = 400
eleves = pd.read_csv("eleves.csv")

# Afficher toutes les colonnes des 5 premiers élèves avec le plus haut score final
meilleurs_eleves = eleves.nlargest(NB_ELEVES, "score_final")

print(f"Meilleurs élèves {1}:")
print(meilleurs_eleves.iloc[0])

print(f"Meilleur élève {NB_ELEVES}:")
print(meilleurs_eleves.iloc[NB_ELEVES-1])
