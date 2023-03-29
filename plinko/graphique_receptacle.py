import modèle_plinko
import modèle_receptacle
from matplotlib import pyplot as plt

NOMBRE_DE_JETS = 10_000
TAILLE_PLINKO = 30

if __name__ == "__main__":
    receptacle = modèle_receptacle.nouveau_receptacle(TAILLE_PLINKO)
    for _ in range(NOMBRE_DE_JETS):
        trajectoire = modèle_plinko.simuler(TAILLE_PLINKO)
        x_de_sortie, _ = trajectoire[-1]
        modèle_receptacle.ajouter_au_godet(receptacle, x_de_sortie)

    plt.plot(receptacle)
    plt.show()
