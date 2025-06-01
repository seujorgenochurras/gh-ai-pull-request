from typing import List

from pydantic import BaseModel


class PullRequest(BaseModel):
  title: str
  draft: str
  base: str
  head: str
  maintainerCanModify: str
  body: List[str]
