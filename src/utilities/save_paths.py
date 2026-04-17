"""
Created on Fri Oct 17 15:38:25 2025

@author: star
"""

import pandas as pd
import os

def save_simulation_path(time, x1, y1, x2, y2, x3, y3, experiment_name):
    """
    Save triple pendulum simulation data to a CSV file inside 'outputs/paths' folder.
    The filename encodes the initial angles.
    """
    # -----------------------------
    # Create output directory
    # -----------------------------
    output_dir = os.path.join("outputs", "paths")
    os.makedirs(output_dir, exist_ok=True)
    
    # -----------------------------
    # Build file path
    # -----------------------------
    filename = f"{experiment_name}.csv"
    save_path = os.path.join(output_dir, filename)
    
    
    # -----------------------------
    # Create DataFrame
    # -----------------------------
    df = pd.DataFrame({
        "time": time,
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2,
        "x3": x3,
        "y3": y3
    })
    
    
    # -----------------------------
    # Save
    # -----------------------------
    df.to_csv(save_path, index=False)
    
    print(f"Saved simulation results to {save_path}")
