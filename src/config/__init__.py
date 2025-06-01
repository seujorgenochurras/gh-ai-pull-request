from .config_manager import ConfigManager

config_manager = ConfigManager()

__all__ = ["ConfigManager", "config_manager"]


DEFAULT_CONFIG_DIR_PATH = "config"
GEMINI_KEY_PROPERTY = "gemini_key"
INSTRUCTIONS_PROPERTY = "instructions"