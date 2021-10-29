'''
FileName: load_config.py
Author: John Delgado
Created Date: 10/28/2021
Version: 1.0 Initial Development
'''

import yaml
import os


def load_config():
    # import config yaml file and then return the python object
    # requirements could change at a later date and easy to use same configs for test cases
    print("Loading config")
    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.split(current_directory)[0]
    config_file = os.path.join(parent_directory, 'config', 'config.yaml')
    print("Loading from: {}".format(config_file))
    try:
        yaml_file = open(config_file, "r")
        return yaml.safe_load(yaml_file)
    except FileNotFoundError as fnf:
        print("Config file does not exist at {}. \n {}".format(
            config_file, fnf))
