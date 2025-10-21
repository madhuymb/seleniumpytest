import yaml
import os

class YamlReader:
    @staticmethod
    def read_yaml(file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
