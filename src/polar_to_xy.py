import numpy as np


def compute_positions(time, theta, lengths=(1.0, 1.0, 1.0)):
    """
    Convert triple pendulum angles into Cartesian coordinates.

    Parameters
    ----------
    time : array-like, shape (N,)
        Time array (not directly used, but kept for consistency)
    theta : array-like, shape (N, 3)
        Angles [theta1, theta2, theta3] in radians
    lengths : tuple of 3 floats
        Lengths of the pendulum links (L1, L2, L3)

    Returns
    -------
    x1, y1, x2, y2, x3, y3 : arrays of shape (N,)
        Cartesian coordinates of each mass
    """

    theta = np.asarray(theta)
    L1, L2, L3 = lengths

    # Extract angles
    theta1 = theta[:, 0]
    theta2 = theta[:, 1]
    theta3 = theta[:, 2]

    # First mass
    x1 = L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)

    # Second mass
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    # Third mass
    x3 = x2 + L3 * np.sin(theta3)
    y3 = y2 - L3 * np.cos(theta3)

    return x1, y1, x2, y2, x3, y3
