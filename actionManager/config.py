import yaml, os

def source_config():
    CONFIG_PATH = os.environ["HOME"] + "/.config/todo_cli/config.yaml"
    with open(CONFIG_PATH) as config_file:
        try:
            config = yaml.safe_load(config_file)
            return config
        except yaml.YAMLError as exc:
            print(exc)
            return None
