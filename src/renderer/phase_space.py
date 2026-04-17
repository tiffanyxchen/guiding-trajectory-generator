# src/renderer/phase_space.py

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


def plot_phase_space_3d(trajectories):
    """
    Plot trajectory in (theta1, theta2, theta3) space.
    """
    theta1, theta2, theta3 = trajectories

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(theta1, theta2, theta3, lw=1.5)

    ax.set_xlabel("theta1")
    ax.set_ylabel("theta2")
    ax.set_zlabel("theta3")

    plt.title("Trajectory in Configuration Space")
    plt.show()


def animate_phase_space_3d(trajectories, interval=20):
    """
    Animate trajectory in (theta1, theta2, theta3) space.
    """
    theta1, theta2, theta3 = trajectories

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    line, = ax.plot([], [], [], lw=1.5)

    ax.set_xlim(min(theta1), max(theta1))
    ax.set_ylim(min(theta2), max(theta2))
    ax.set_zlim(min(theta3), max(theta3))

    ax.set_xlabel("theta1")
    ax.set_ylabel("theta2")
    ax.set_zlabel("theta3")

    def update(frame):
        line.set_data(theta1[:frame], theta2[:frame])
        line.set_3d_properties(theta3[:frame])
        return line,

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=len(theta1),
        interval=interval
    )

    plt.title("Animated Trajectory in Configuration Space")
    plt.show()

    return ani
