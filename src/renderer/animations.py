import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.animation import FuncAnimation


def animate_pendulum(time, trajectories, lengths, save_path=None):
    """
    Animate triple pendulum motion using Cartesian coordinates.

    Parameters
    ----------
    time : array
    trajectories : list of arrays [theta1, theta2, theta3]
    lengths : tuple (L1, L2, L3)
    """

    theta1, theta2, theta3 = trajectories
    L1, L2, L3 = lengths

    # -----------------------------
    # Convert to Cartesian
    # -----------------------------
    x1 =  L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)

    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    x3 = x2 + L3 * np.sin(theta3)
    y3 = y2 - L3 * np.cos(theta3)

    # -----------------------------
    # Setup figure
    # -----------------------------
    fig, ax = plt.subplots(figsize=(6, 6))

    total_length = L1 + L2 + L3
    ax.set_xlim(-total_length, total_length)
    ax.set_ylim(-total_length, total_length)

    ax.set_aspect('equal')
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=2)

    # -----------------------------
    # Init
    # -----------------------------
    def init():
        line.set_data([], [])
        return line,

    # -----------------------------
    # Update
    # -----------------------------
    def update(frame):
        thisx = [0, x1[frame], x2[frame], x3[frame]]
        thisy = [0, y1[frame], y2[frame], y3[frame]]

        line.set_data(thisx, thisy)
        return line,

    # -----------------------------
    # Animate
    # -----------------------------
    n_steps = len(time)
    interval = 1000 * (time[-1] - time[0]) / n_steps
    
    skip = 1    # or 3 or 4
    ani = FuncAnimation(
        fig,
        update,
        frames=range(0, len(time), skip),
        init_func=init,
        interval=interval,
        blit=True
    )

    plt.title("Triple Pendulum Motion")
    
    if save_path:
        ani.save(save_path, writer="ffmpeg", dpi=150)

    plt.show()

    return ani

