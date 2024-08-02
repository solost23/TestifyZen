import yaml


def read_config(file_path: str = 'config/config.yaml'):
    with open(file_path, 'r') as fp:
        return yaml.safe_load(fp)
