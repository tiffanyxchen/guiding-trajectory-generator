import numpy as np
def triangle_wave(time, theta_min, theta_max, omega, start_at_max=False):
    period = 2 * (theta_max - theta_min) / omega
    theta = []
    for t in time:
        t_mod = t % period
        if t_mod <= (theta_max - theta_min) / omega:
            val = theta_max - omega*t_mod if start_at_max else theta_min + omega*t_mod
        else:
            val = theta_min + omega*(t_mod - (theta_max-theta_min)/omega) if start_at_max else theta_max - omega*(t_mod - (theta_max-theta_min)/omega)
        theta.append(val)
    return np.array(theta)
