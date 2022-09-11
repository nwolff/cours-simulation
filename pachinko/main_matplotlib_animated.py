"""
Ref :
    https://matplotlib.org/stable/gallery/animation/animated_histogram.html
"""
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.animation as animation
import pachinko_model
import receptacle_model

RUNS = 10000
BATCH_SIZE = 30


def prepare_animation(bar_container):
    def animate(frame_number):
        for _ in range(BATCH_SIZE):
            trajectory = pachinko_model.simulate(size)
            exit_x, _ = trajectory[-1]
            receptacle_model.add_to_bucket(receptacle, exit_x)
        for count, rect in zip(receptacle, bar_container.patches):
            rect.set_height(count)

    return animate


if __name__ == "__main__":
    size = 30
    receptacle = receptacle_model.new_receptacle(size)
    hist_bins = np.linspace(start=0, stop=size, num=size)
    fig, ax = plt.subplots()
    _, _, bar_container = ax.hist(receptacle, hist_bins)
    ax.set_ylim(top=RUNS / 5)
    ani = animation.FuncAnimation(
        fig,
        prepare_animation(bar_container),
        interval=1,
        frames=RUNS // BATCH_SIZE,
        repeat=False,
    )
    plt.show()
