from dataclasses import dataclass
from typing import List


@dataclass
class PullRequest:
  title: str
  draft: str
  base: str
  head: str
  maintainerCanModify: str
  body: List[str]
