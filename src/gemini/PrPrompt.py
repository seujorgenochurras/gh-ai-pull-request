from dataclasses import dataclass
from typing import Any



@dataclass()
class PrPrompt:
  pr_data: dict[str, Any]
  instruction: str
