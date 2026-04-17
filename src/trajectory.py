from .signals import triangle_wave
def generate_trajectories(time, motion_cfg):
    out = []
    for link in motion_cfg["links"]:
        out.append(triangle_wave(time, link["theta_min"], link["theta_max"], link["omega"], link.get("start_at_max", False)))
    return out
