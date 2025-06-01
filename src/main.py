import questionary

from config import config_manager
from config.config import GEMINI_KEY_PROPERTY, INSTRUCTIONS_PROPERTY
from gemini.PromptManager import PromptManager
from gemini.PrPrompt import PrPrompt
from gh import GhManager


def ask_create_instruction():
  instruction = questionary.text("Write instructions for the AI").ask()
  saved_instructions = config_manager.get(INSTRUCTIONS_PROPERTY) or []

  saved_instructions.append(instruction)
  config_manager.save(INSTRUCTIONS_PROPERTY, saved_instructions)
  return saved_instructions


def ensure_instructions():
  instructions = config_manager.get(INSTRUCTIONS_PROPERTY)
  if not instructions:
    instructions = ask_create_instruction()
  return instructions


def ask_ai_instruction():
  instructions: list[str] = ensure_instructions()

  choices: list[questionary.Choice] = []
  choices.append(questionary.Choice("Create new prompt", "new_prompt"))

  for instruction in instructions:
    choices.append(questionary.Choice(instruction, instruction))

  selected_instruction = questionary.select(
    "Choose the AI prompt", choices=["Create new prompt"] + instructions
  ).ask()

  if selected_instruction == "new_prompt":
    ask_create_instruction()
    ask_ai_instruction()

  return selected_instruction


def ensure_ai_key():
  if not config_manager.get(GEMINI_KEY_PROPERTY):
    key = questionary.text("What's your Gemini AI key").ask()
    config_manager.save(GEMINI_KEY_PROPERTY, key)


def create_pull_request(instruction: str):
  ai_manager = PromptManager()
  pr_json = GhManager.create_dry_pr()
  new_pr = ai_manager.prompt_pr(PrPrompt(pr_json, instruction))

  return GhManager.create_pr(new_pr)


def main():
  ensure_ai_key()
  instruction = ask_ai_instruction()

  gh_response = create_pull_request(instruction)

  print(gh_response)
  print("Succesfully created pull request")


if __name__ == "__main__":
  main()
