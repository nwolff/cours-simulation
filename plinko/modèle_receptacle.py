def nouveau_receptacle(taille):
    return [0 for _ in range(taille)]


def ajouter_au_godet(receptacle, index):
    receptacle[index] += 1
    return receptacle[index]
