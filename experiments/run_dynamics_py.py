import numpy as np

from src.config_loader import load_config
from src.timeline import generate_timeline
from src.renderer.animations import animate_pendulum
from src.utilities.save_states import save_state

# 👇 your Python dynamics solver
from src.triple_pendulum import simulate_triple_pendulum


def run_experiment(config):
    # -----------------------------
    # Time
    # -----------------------------
    time_cfg = config["timeline"]
    time = generate_timeline(time_cfg)

    # -----------------------------
    # Physics
    # -----------------------------
    links = config["physics"]["links"]

    theta0 = [link["theta_0"] for link in links]
    p0     = [link["p_0"] for link in links]

    x0 = theta0 + p0

    # Parameters
    g = config["gravity"]["value"]
    L = links[0].get("length", 1.0)
    m = links[0]["mass"]

    params = {
        "g": g,
        "L": L,
        "m": m
    }

    # -----------------------------
    # Run Python simulation
    # -----------------------------
    result = simulate_triple_pendulum(time, x0, params)

    result = np.array(result)
    print("result shape:", result.shape)

    # -----------------------------
    # Save state (PY version)
    # -----------------------------
    theta_init = theta0

    save_state(
        time,
        result,
        theta_init,
        tag="PY"   # 👈 distinguish from CPP
    )

    # -----------------------------
    # Extract angles for animation
    # -----------------------------
    theta1 = result[:, 0]
    theta2 = result[:, 1]
    theta3 = result[:, 2]

    trajectories = [theta1, theta2, theta3]
    lengths = (L, L, L)

    # -----------------------------
    # Animate
    # -----------------------------
    animate_pendulum(time, trajectories, lengths)


if __name__ == "__main__":
    config = load_config("configs")
    run_experiment(config)
