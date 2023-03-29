from collections import namedtuple

import arcade
import modèle_plinko

NOMBRE_DE_JETS = 10_000
TAILLE_PLINKO = 30
BALLES_EN_JEU = 30
DIMENSIONS_FENETRE = (800, 600)
FACTEUR_REDUCTION_BALLE = 0.25


TrajectoireEtSprite = namedtuple("TrajectoireEtSprite", "trajectoire sprite")


def nouveau_TES():
    return TrajectoireEtSprite(
        trajectoire=iter(modèle_plinko.simuler(TAILLE_PLINKO)),
        sprite=arcade.Sprite("balle.png", FACTEUR_REDUCTION_BALLE),
    )


def convertir_pour_écran(coordonnées):
    x, y = coordonnées
    return (
        (x + TAILLE_PLINKO) * DIMENSIONS_FENETRE[0] / TAILLE_PLINKO / 2,
        y * DIMENSIONS_FENETRE[1] / TAILLE_PLINKO,
    )


class MonJeu(arcade.Window):
    def __init__(self):
        super().__init__(DIMENSIONS_FENETRE[0], DIMENSIONS_FENETRE[1], "Plinko")
        self.set_mouse_visible(False)
        self.tes = None
        self.sprite_list = None

    def setup(self):
        trajectoire_et_sprite = nouveau_TES()
        self.tes = [trajectoire_et_sprite]
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(trajectoire_et_sprite.sprite)

    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()

    def update(self, delta_time):
        for trajectoire_et_sprite in self.tes:
            trajectoire, sprite = trajectoire_et_sprite
            prochaines_coordonnées = next(trajectoire)
            if prochaines_coordonnées:
                sprite.center_x, sprite.center_y = convertir_pour_écran(
                    prochaines_coordonnées
                )
            else:
                self.tes.remove()
                self.sprite_list.remove(sprite)


if __name__ == "__main__":
    MonJeu().setup()
    arcade.run()
