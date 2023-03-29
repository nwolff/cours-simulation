import matplotlib.animation as animation
import modèle_plinko
import modèle_receptacle
import numpy as np
from matplotlib import pyplot as plt

NOMBRE_DE_JETS = 10_000
TAILLE_PLINKO = 30
TAILLE_DE_LOT = 200


def preparer_animation(barres):
    def animer(_):
        for _ in range(TAILLE_DE_LOT):
            trajectoire = modèle_plinko.simuler(TAILLE_PLINKO)
            x_de_sortie, _ = trajectoire[-1]
            modèle_receptacle.ajouter_au_godet(receptacle, x_de_sortie)
        for nombre, rectangle in zip(receptacle, barres.patches):
            rectangle.set_height(nombre)

    return animer


if __name__ == "__main__":
    receptacle = modèle_receptacle.nouveau_receptacle(TAILLE_PLINKO)
    hist_bins = np.linspace(start=0, stop=TAILLE_PLINKO, num=TAILLE_PLINKO)
    fig, ax = plt.subplots()
    _, _, bar_container = ax.hist(receptacle, hist_bins)
    ax.set_ylim(top=NOMBRE_DE_JETS / 5)
    ani = animation.FuncAnimation(
        fig,
        preparer_animation(bar_container),
        interval=1,
        frames=NOMBRE_DE_JETS // TAILLE_DE_LOT,
        repeat=False,
    )
    plt.show()
