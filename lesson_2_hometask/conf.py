import yaml

class Conf:
    def __init__(self, path):
        with open(path, 'r') as yaml_file:
            self.__conf = yaml.safe_load(yaml_file)

    def get_config(self, application):
        return self.__conf.get(application)