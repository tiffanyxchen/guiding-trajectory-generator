# experiments/run_single_reverse_second.py
import numpy as np
from copy import deepcopy
from src.utilities.save_animations import save_animation
from src.utilities.save_paths import save_simulation_path
from src.polar_to_xy import compute_positions

import os
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


    # -----------------------------
    # Generate data
    # -----------------------------
    # time         = generate_timeline(config["timeline"])
    
    dt = 0.01
    time = np.arange(0.0, 5.0 + dt, dt)
    
    trajectories = generate_trajectories(time, config["motion"])
    lengths      = get_lengths(config["system"])


    # -----------------------------
    # Auto-name from file
    # -----------------------------
    experiment_name = os.path.splitext(os.path.basename(__file__))[0]


    # -----------------------------
    # Animate
    # -----------------------------
    
    anim = animate_pendulum(time, trajectories, lengths)
    
    # -----------------------------
    # Save animation
    # -----------------------------
    # save_animation(anim, experiment_name)
    
    # -----------------------------
    # Save
    # -----------------------------
    x = np.column_stack(trajectories)
    x1, y1, x2, y2, x3, y3 = compute_positions(time, x, lengths)
    
    save_simulation_path(time, x1, y1, x2, y2, x3, y3, experiment_name)
    
if __name__ == "__main__":
    main()
