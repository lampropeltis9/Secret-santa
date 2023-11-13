# %%
import pandas as pd
import segno

def secret_santa(participants : pd.DataFrame) -> dict:
    """
    Pour une liste de participants donnée, affecte aléatoirement
    un père noël à un receveur.

    Paramètre
    ---------
    participants (pd.DataFrame): deux colonnes : NOM, EMAIL

    Sortie
    ------
    Dictionnaire : {donneur : receveur}
    """
    # Mélanger la liste des participants de manière aléatoire
    participants = participants.sample(frac=1).reset_index(drop=True)

    # Créer une correspondance entre chaque personne et la personne à qui elle doit offrir un cadeau
    assignments = {participants.loc[i, 'NOM']: \
                   participants.loc[(i + 1) % len(participants), 'NOM'] \
                    for i in range(len(participants))}

    return assignments

# Liste des participants
# participants = ["theophile", "marion", "alexis", "amandine", "ele"]
participants = pd.read_csv('lst_participants.csv',
                           dtype={'NOM':'str', 'EMAIL':'str'})

# Obtenir les correspondances
assignments = secret_santa(participants)

# Afficher les correspondances
for giver, receiver in assignments.items():
    print(f"{giver} offre un cadeau à {receiver}")
    qrcode = segno.make_qr(f"Tu offres un cadeau à {receiver}")
    qrcode.save(f"qrcode_{giver}.png", scale = 10)
# %%
