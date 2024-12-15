import yaml

class YAMLParser:
    @staticmethod
    def load_yaml(file_path):
        """Load and validate the YAML configuration file."""
        with open(file_path, 'r') as file:
            try:
                return yaml.safe_load(file)
            except yaml.YAMLError as e:
                raise ValueError(f"Invalid YAML file: {e}")