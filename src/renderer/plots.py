import matplotlib.pyplot as plt
def plot_time_series(time, trajectories):
    for i, th in enumerate(trajectories):
        plt.plot(time, th, label=f"theta_{i+1}")
    plt.xlabel("Time"); plt.ylabel("Angle")
    plt.legend(); plt.show()
