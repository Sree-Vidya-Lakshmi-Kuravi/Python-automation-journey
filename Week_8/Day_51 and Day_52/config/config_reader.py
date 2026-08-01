import os
import  configparser

# Get the path of the current file
current_file = os.path.dirname(os.path.abspath(__file__))

# Combine that directory path with 'config.ini'
CONFIG_FILE_PATH = os.path.join(current_file, "config.ini")

# Read the configuration file
config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH)
BASE_URL = config.get("env", "base_url")

def get_url():
    return config.get("API", "BASE_URL")

def get_timeout():
    return config.getint("API", "timeout")

def get_posts_endpoint():
    return config.get("API", "posts_endpoint")

def get_users_endpoint():
    return config.get("API", "users_endpoint")

def get_html_report_dir():
    return config.get("REPORTS", "html_report_dir")

def get_allure_results_dir():
    return config.get("REPORTS", "allure_results_dir")

def get_log_file():
    # Gets the log file path or falls back to 'logs/framework.log'
    return config.get("LOGGING", "log_file", fallback="logs/framework.log")

def get_log_level():
    # Gets the log level or falls back to 'INFO'
    return config.get("LOGGING", "log_level", fallback="INFO")