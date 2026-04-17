# experiments/run_single_reverse_second.py

from copy import deepcopy

from src.config_loader import load_config
from src.timeline import generate_timeline
from src.trajectory import generate_trajectories
from src.lengths import get_lengths
from src.renderer.animations import animate_pendulum


def main():
    # -----------------------------
    # Load config
    # -----------------------------
    config = load_config("configs")

    # -----------------------------
    # Modify ONLY second pendulum
    # -----------------------------
    motion = config["motion"]["links"]

    # flip direction: +pi/2 -> -pi/2
    motion[1]["start_at_max"] = True
    motion[1]["omega"] = 2
    motion[2]["omega"] = 3

    # -----------------------------
    # Generate data
    # -----------------------------
    time = generate_timeline(config["timeline"])
    trajectories = generate_trajectories(time, config["motion"])
    lengths = get_lengths(config["system"])

    # -----------------------------
    # Animate
    # -----------------------------
    animate_pendulum(time, trajectories, lengths)


if __name__ == "__main__":
    main()
