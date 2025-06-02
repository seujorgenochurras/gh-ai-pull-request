import os
from .config_manager import ConfigManager


config_manager = ConfigManager(os.path.expanduser("~/.gh-ai-pr/config"))
