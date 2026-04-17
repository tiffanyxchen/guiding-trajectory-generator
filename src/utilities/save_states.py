import pandas as pd
import os

def save_state(time, x, theta_init, tag="CPP"):
    """
    Save angles and momenta only.
    
    x shape: (n_steps, 6)
    columns: [theta1, theta2, theta3, p1, p2, p3]
    """
    save_dir = "outputs/states"
    os.makedirs(save_dir, exist_ok=True)

    filename = f"{save_dir}/state_{theta_init[0]:.2f}_{theta_init[1]:.2f}_{theta_init[2]:.2f}_{tag}"
    filename = filename.replace('.', 'p').replace('-', 'm') + ".csv"

    df = pd.DataFrame({
        "time": time,
        "theta1": x[:, 0],
        "theta2": x[:, 1],
        "theta3": x[:, 2],
        "p1": x[:, 3],
        "p2": x[:, 4],
        "p3": x[:, 5],
    })

    df.to_csv(filename, index=False)
    print(f"Saved state to {filename}")
