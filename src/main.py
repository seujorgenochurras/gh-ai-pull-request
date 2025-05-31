# AIzaSyAPtaTERZKDaUb6gGwl1UWBOCK_qvBRGm0
import json
import subprocess
import questionary
from common import GhDryRunParser
from config import ConfigManager
from config.config import GEMINI_KEY_PROPERTY

config_manager = ConfigManager("teste")


def main():
  if not config_manager.get(GEMINI_KEY_PROPERTY):
    prompt_ai_key()


def prompt_ai_statement():
  pass


def prompt_ai_key():
  key = questionary.text("What's your Gemini AI key").ask()
  config_manager.save(GEMINI_KEY_PROPERTY, key)


def get_pr_json():
  command_output = (
    subprocess.Popen("gh pr create --dry-run -f", shell=True, stdout=subprocess.PIPE)
    .stdout.read()  # type: ignore
    .decode()
  ).split("\n", 1)[1]
  parser = GhDryRunParser(command_output)
  return parser.parse_output()

print(json.dumps(get_pr_json()))
