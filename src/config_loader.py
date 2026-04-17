import yaml, os
def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def merge_dicts(base, new):
    for k, v in new.items():
        if isinstance(v, dict) and k in base:
            base[k] = merge_dicts(base[k], v)
        else:
            base[k] = v
    return base

def load_config(config_dir, base_file="base.yaml"):
    base = load_yaml(os.path.join(config_dir, base_file))
    final = {}
    for f in base["includes"]:
        sub = load_yaml(os.path.join(config_dir, f))
        final = merge_dicts(final, sub)
    return final
