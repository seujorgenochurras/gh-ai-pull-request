import json

from pydantic_ai.agent import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider

from config import config_manager
from config.config import GEMINI_KEY_PROPERTY
from gemini.pr_prompt import PrPrompt
from gh.pull_request import PullRequest


class PromptManager:
  def __init__(self):
    self.gemini_client = Agent(
      model=GeminiModel(
        model_name="gemini-2.0-flash",
        provider=GoogleGLAProvider(api_key=config_manager.get(GEMINI_KEY_PROPERTY)),
      ),
      output_type=PullRequest,
    )

  def prompt_pr(self, pr_prompt_ctx: PrPrompt) -> PullRequest:
    prompt = f"""
      I'll give you a json containing some Pull request data,
      I'll then ask you something and your answer must be a JSON 
      changing only the data that I gave you, do not answer anything other than a JSON
      do not add new properties.
      
      
      JSON: {json.dumps(pr_prompt_ctx.pr_data)} 
      
      
      Instructions: {pr_prompt_ctx.instruction}
    """

    ai_response = self.gemini_client.run_sync(prompt)

    return ai_response.output
