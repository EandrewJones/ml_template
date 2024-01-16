import configparser

# Instantiate ConfigParser
cfg = configparser.ConfigParser()

# Parse the config file
cfg.read("config/fastapi.conf")
