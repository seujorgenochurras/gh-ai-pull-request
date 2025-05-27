import json
from google import genai

from config import config_manager
from config.config import GEMINI_KEY_PROPERTY
from gemini.PrPrompt import PrPrompt


class PromptManager:
  def __init__(self): 
    self.gemini_client = genai.Client(api_key=config_manager.get(GEMINI_KEY_PROPERTY))
    
  def prompt_pr(self, pr_prompt_ctx: PrPrompt):
    prompt = f"""
      I'll give you a json containing some Pull request data,
      I'll then ask you something and your answer must be a JSON 
      changing only the data that I gave you, do not answer anything other than a JSON
      do not add new properties.
      
      
      JSON: {json.dumps(pr_prompt_ctx.pr_data)} 
      
      
      Instructions: {pr_prompt_ctx.instructions}
    """
    ai_response = self.gemini_client.models.generate_content(
      model="gemini-2.0-flash", contents=prompt
    )
    
    print(ai_response.text)
