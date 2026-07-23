import configparser
import os

# Get the folder where this config_reader.py file lives
config_dir = os.path.dirname(os.path.abspath(__file__))

# Join that folder path with 'config.ini'
config_file_path = os.path.join(config_dir, "config.ini")

# Creating the parser object
config = configparser.RawConfigParser()

# Reading the file
config.read(config_file_path)

# config.get(section, key) works:
# section: The header in brackets, like [common] or [credentials].
# key: The variable name under that header, like browser or base_url.

class ConfigReader:
    """Reads configuration values and credentials from config.ini."""

    @staticmethod
    def get_base_url():
        """Reads 'base_url' under [common]."""
        return config.get("common", "base_url")

    @staticmethod
    def get_browser():
        """Reads 'browser' under [common]."""
        return config.get("common", "browser")

    @staticmethod
    def get_implicit_wait():
        """Reads 'implicit_wait' as an integer under [common]."""
        return config.getint("common", "implicit_wait")

    @staticmethod
    def get_explicit_wait():
        """Reads 'explicit_wait' as an integer under [common]."""
        return config.getint("common", "explicit_wait")

    @staticmethod
    def get_username(user_type="standard_user"):
        """Reads a specific username under [credentials]. Defaults to 'standard_user'."""
        return config.get("credentials", user_type)

    @staticmethod
    def get_password():
        """Reads 'password' under [credentials]."""
        return config.get("credentials", "password")