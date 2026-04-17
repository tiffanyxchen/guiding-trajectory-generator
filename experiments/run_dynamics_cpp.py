from src.utilities.save_states import save_state
import numpy as np
import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src/cpp"))
import cpp_bindings

from src.timeline import generate_timeline
from src.renderer.animations import animate_pendulum

def run_experiment(config):
    # Time
    time_cfg = config["timeline"]
    time = generate_timeline(time_cfg)

    # Physics
    links = config["physics"]["links"]
    theta0 = [link["theta_0"] for link in links]
    p0     = [link["p_0"] for link in links]

    x0 = theta0 + p0

    # Parameters (assuming same for all links)
    g = config["gravity"]["value"]
    L = links[0].get("length", 1.0)
    m = links[0]["mass"]

    # Run C++ simulation
    result = cpp_bindings.simulate(time.tolist(), x0, g, L, m)

    result = np.array(result)
    print("result shape:", result.shape)
    
    # -----------------------------
    # Save state (CPP version)
    # -----------------------------
    theta_init = theta0

    save_state(
        time,
        result,
        theta0,
        tag="CPP"   # 👈 important for comparison later
    )

    # Extract angles
    theta1 = result[:, 0]
    theta2 = result[:, 1]
    theta3 = result[:, 2]

    trajectories = [theta1, theta2, theta3]

    lengths = (L, L, L)

    # Animate
    animate_pendulum(time, trajectories, lengths)


if __name__ == "__main__":
    from src.config_loader import load_config

    config = load_config("configs")
    run_experiment(config)
