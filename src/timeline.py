import numpy as np
def generate_timeline(cfg):
    return np.arange(cfg["t0"], cfg["tf"], cfg["dt"])
