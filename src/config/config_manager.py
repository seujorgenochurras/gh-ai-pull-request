import os
from typing import Any
import json

from config.config import DEFAULT_CONFIG_DIR_PATH




class ConfigManager:
  def __init__(self, config_dir_path: str = DEFAULT_CONFIG_DIR_PATH):
    self.config_dir_path = config_dir_path
    self.config_file_path = os.path.join(config_dir_path, "config.json")

    if not os.path.exists(self.config_file_path):
      self._create_initial_config_file()

    with open(self.config_file_path, "r") as config_file:
      self._config: dict[str, Any] = json.loads(config_file.read())

  def save(self, configName: str, value: Any):
    self._config[configName] = value
    self._rewrite_config_file()

  def get(self, key: str) -> Any:
    return self._config.get(key)

  def _rewrite_config_file(self):
    with open(self.config_file_path, "w") as config_file:
      config_file.write(json.dumps(self._config))
      config_file.flush()

  def _create_initial_config_file(self):
    os.makedirs(self.config_dir_path, exist_ok=True)
    with open(self.config_file_path, "w+") as config_file:
      config_file.write("{ }")
