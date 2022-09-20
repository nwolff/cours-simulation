import random


def sommet(hauteur):
    return 0, hauteur


def successeur_gauche(coord):
    x, y = coord
    return x, y - 1


def successeur_droit(coord):
    x, y = coord
    return x + 1, y - 1


def est_en_bas(coord):
    _, y = coord
    return y <= 0


def un_pas_aléatoire(coord):
    choix = random.choice(("G", "D"))
    if choix == "G":
        return successeur_gauche(coord)
    else:
        return successeur_droit(coord)


def simuler(hauteur):
    """Retourne une trajectoire de coordonnées"""
    coord = sommet(hauteur)
    resultat = []
    while not est_en_bas(coord):
        nouvelle_coordonnée = un_pas_aléatoire(coord)
        resultat.append(nouvelle_coordonnée)
        coord = nouvelle_coordonnée
    return resultat
