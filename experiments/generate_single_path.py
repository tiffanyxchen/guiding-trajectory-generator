from src.config_loader import load_config
from src.timeline import generate_timeline
from src.trajectory import generate_trajectories
from src.lengths import get_lengths
from src.renderer.plots import plot_time_series
from src.renderer.animations import animate_pendulum

def main():
    config = load_config("configs")

    time = generate_timeline(config["timeline"])
    trajectories = generate_trajectories(time, config["motion"])
    lengths = get_lengths(config["system"])

    plot_time_series(time, trajectories)
    animate_pendulum(time, trajectories, lengths)

if __name__ == "__main__":
    main()
