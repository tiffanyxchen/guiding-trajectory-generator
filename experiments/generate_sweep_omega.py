from copy import deepcopy

from src.config_loader import load_config
from src.timeline import generate_timeline
from src.trajectory import generate_trajectories
from src.lengths import get_lengths
from src.renderer.animations import animate_pendulum

def main():
    base_config = load_config("configs")

    omega_sets = [
        [1.0, 1.0, 1.0],
        [1.0, 1.01, 1.02],
        [1.0, 2.0, 3.0],
    ]

    for omegas in omega_sets:
        config = deepcopy(base_config)

        for i, omega in enumerate(omegas):
            config["motion"]["links"][i]["omega"] = omega

        print(f"Running omega set: {omegas}")

        time = generate_timeline(config["timeline"])
        trajectories = generate_trajectories(time, config["motion"])
        lengths = get_lengths(config["system"])

        animate_pendulum(time, trajectories, lengths)

if __name__ == "__main__":
    main()
