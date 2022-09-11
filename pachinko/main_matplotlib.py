from matplotlib import pyplot as plt
import pachinko_model
import receptacle_model

RUNS = 10000

if __name__ == "__main__":
    size = 50
    receptacle = receptacle_model.new_receptacle(size)
    for _ in range(RUNS):
        trajectory = pachinko_model.simulate(size)
        last_coord = trajectory[-1]
        exit_x, _ = last_coord
        receptacle_model.add_to_bucket(receptacle, exit_x)

    plt.plot(receptacle)
    plt.show()
