import numpy as np
from copy import deepcopy

from src.config_loader import load_config
from src.timeline import generate_timeline
from src.trajectory import generate_trajectories
from src.renderer.phase_space import plot_phase_space_3d

def main():
    base_config = load_config("configs")

    omega_values = np.linspace(1.0, 2.0, 5)

    for w1 in omega_values:
        for w2 in omega_values:
            for w3 in omega_values:

                config = deepcopy(base_config)

                config["motion"]["links"][0]["omega"] = w1
                config["motion"]["links"][1]["omega"] = w2
                config["motion"]["links"][2]["omega"] = w3

                print(f"Omega: {w1:.2f}, {w2:.2f}, {w3:.2f}")

                time = generate_timeline(config["timeline"])
                trajectories = generate_trajectories(time, config["motion"])

                plot_phase_space_3d(trajectories)

if __name__ == "__main__":
    main()
