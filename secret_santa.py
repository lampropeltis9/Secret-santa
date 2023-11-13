# %%
# Packages
import pandas as pd
import segno

# %%
# Liaison entre les père-noëls secrets et les receveurs
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
    participants = participants.sample(frac=1).reset_index(drop=True)

    return {participants.loc[i, 'NOM']: \
                participants.loc[(i + 1) % len(participants), 'NOM'] \
                    for i in range(len(participants))}

# Liste des participants
participants = pd.read_csv('infile/lst_participants.csv',
                           dtype={'NOM':'str', 'EMAIL':'str'})

# Correspondances
assignments = secret_santa(participants)

# Générer les QR codes
for giver, receiver in assignments.items():
    qrcode = segno.make_qr(f"Tu offres un cadeau à {receiver}")
    qrcode.save(f"qrcodes/qrcode_{giver}.png", scale = 10)
# %%
