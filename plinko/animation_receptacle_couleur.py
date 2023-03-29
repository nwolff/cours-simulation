import random
import sys

import modèle_plinko
import modèle_receptacle
import pygame

NOMBRE_DE_JETS = 10_000
TAILLE_PLINKO = 30
TAILLE_DE_LOT = 20

DIMENSIONS_FENETRE = [800, 800]
NOIR = (0, 0, 0)

ETAPES_ENTRE_COULEURS = 1000


def générateur_de_couleurs():
    couleur_de_départ = couleur_aléatoire()
    while True:
        couleur_arrivée = couleur_aléatoire()
        for alpha in range(0, ETAPES_ENTRE_COULEURS):
            yield [
                int(
                    comp_1 * (1 - alpha / ETAPES_ENTRE_COULEURS)
                    + comp_2 * alpha / ETAPES_ENTRE_COULEURS
                )
                for comp_1, comp_2 in zip(couleur_de_départ, couleur_arrivée)
            ]
        couleur_de_départ = couleur_arrivée


def couleur_aléatoire():
    niveaux = range(32, 256, 32)  # On évite le noir et les couleurs trop subtiles
    return [random.choice(niveaux) for _ in range(3)]


def convertir_pour_écran(x, y):
    return (
        x * DIMENSIONS_FENETRE[0] / TAILLE_PLINKO,
        DIMENSIONS_FENETRE[1] - y * DIMENSIONS_FENETRE[1] / NOMBRE_DE_JETS * 6,
    )


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(DIMENSIONS_FENETRE)
    screen.fill(NOIR)
    couleurs = générateur_de_couleurs()

    receptacle = modèle_receptacle.nouveau_receptacle(TAILLE_PLINKO)
    for _ in range(NOMBRE_DE_JETS // TAILLE_DE_LOT):
        rectangles = []
        for _ in range(TAILLE_DE_LOT):
            trajectoire = modèle_plinko.simuler(TAILLE_PLINKO)
            x_de_sortie, _ = trajectoire[-1]
            value = modèle_receptacle.ajouter_au_godet(receptacle, x_de_sortie)
            rect_x, rect_y = convertir_pour_écran(x_de_sortie, value)
            rect = (rect_x, rect_y, 17, 1)
            pygame.draw.rect(screen, next(couleurs), rect)
            rectangles.append(rect)
        pygame.display.update(rectangles)
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (
                e.type == pygame.KEYUP and e.key == pygame.K_ESCAPE
            ):
                sys.exit(0)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (
                e.type == pygame.KEYUP and e.key == pygame.K_ESCAPE
            ):
                sys.exit(0)
