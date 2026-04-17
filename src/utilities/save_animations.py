import os
from matplotlib.animation import FFMpegWriter


def save_animation(anim, experiment_name, fps=30):
    """
    Save a matplotlib animation to output/animations/.

    Parameters
    ----------
    anim : matplotlib.animation.FuncAnimation
        The animation object to save
    experiment_name : str
        Name of the experiment (used as filename)
    fps : int
        Frames per second
    """

    # -----------------------------
    # Create output directory
    # -----------------------------
    output_dir = os.path.join("outputs", "animations")
    os.makedirs(output_dir, exist_ok=True)

    # -----------------------------
    # Build file path
    # -----------------------------
    filename = f"{experiment_name}.mp4"
    save_path = os.path.join(output_dir, filename)

    # -----------------------------
    # Save animation
    # -----------------------------
    writer = FFMpegWriter(fps=fps)
    anim.save(save_path, writer=writer)

    print(f"✅ Animation saved to: {save_path}")
