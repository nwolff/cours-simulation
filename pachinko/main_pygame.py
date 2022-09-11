#! /usr/bin/env python

"""
https://github.com/pygame/pygame/blob/main/examples/stars.py
"""
import pachinko_model
import receptacle_model
import pygame as pg
import sys
import random

NUM_BUCKETS = 40
RUNS = 10000
BATCH_SIZE = 30

WINSIZE = [800, 800]
BLACK = (0, 0, 0)


def random_color_generator():
    STEPS = 200
    while True:
        from_color, to_color = random_color(), random_color()
        for alpha in range(0, STEPS):
            yield [
                int(comp_1 * (1 - alpha / STEPS) + comp_2 * alpha / STEPS)
                for comp_1, comp_2 in zip(from_color, to_color)
            ]


def random_color():
    levels = range(32, 256, 32)
    return [random.choice(levels) for _ in range(3)]


def convert_to_screen(x, y):
    return x * WINSIZE[0] / NUM_BUCKETS, WINSIZE[1] - y * WINSIZE[1] / RUNS * 5


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    screen.fill(BLACK)
    colors = random_color_generator()

    receptacle = receptacle_model.new_receptacle(NUM_BUCKETS)
    for _ in range(RUNS // BATCH_SIZE):
        rects = []
        for _ in range(BATCH_SIZE):
            trajectory = pachinko_model.simulate(NUM_BUCKETS)
            last_coord = trajectory[-1]
            exit_x, _ = last_coord
            value = receptacle_model.add_to_bucket(receptacle, exit_x)
            rect_x, rect_y = convert_to_screen(exit_x, value)
            rect = (rect_x, rect_y, 17, 1)
            pg.draw.rect(screen, next(colors), rect)
            rects.append(rect)
        pg.display.update(rects)
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                sys.exit(0)

    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                sys.exit(0)
