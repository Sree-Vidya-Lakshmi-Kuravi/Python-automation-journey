import configparser
import os

def _get_config():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", "config.ini")
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def get_config_value(section, key):
    config = _get_config()
    return config.get(section, key)

def get_base_url():
    return get_config_value("env", "base_url")

def get_timeout():
    return int(get_config_value("env", "timeout"))

def get_api_key():
    return get_config_value("env", "api_key")

def get_data_format():
    return get_config_value("data", "default_data_format")