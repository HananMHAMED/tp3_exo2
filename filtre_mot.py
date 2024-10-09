def filtre(path):
    with open(path, "r") as f:
        contenu = f.read()
    mots = contenu.split("\n")
    mots_filtre = []
    for mot in mots:
        if est_normale(mot):
            mots_filtre.append(mot)
    return mots_filtre


def est_normale(mot):
    for lettre in mot:
        if len(mot) < 5 or len(mot) > 10:
            return False
        if not (ord("A") <= ord(lettre) <= ord("z")):
            return False
    return True

def creer():
    mots_filtre = filtre("./liste.de.mots.francais.frgut.txt")
    with open("mot_franc_filtrer.txt", "w") as f:
        for mot in mots_filtre:
            f.write(f"{mot}\n")

creer()
