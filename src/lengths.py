# src/lengths.py

def get_lengths(system_config):
    """
    Extract pendulum lengths from system config.

    Parameters
    ----------
    system_config : dict

    Returns
    -------
    tuple
        (L1, L2, L3, ...)
    """

    lengths = system_config.get("lengths")

    if lengths is None:
        raise ValueError("Lengths not found in system config")

    if not isinstance(lengths, (list, tuple)):
        raise ValueError("Lengths must be a list or tuple")

    return tuple(lengths)
