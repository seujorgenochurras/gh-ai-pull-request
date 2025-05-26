from typing import Any


class GhDryRunParser:
  """
  GhDryRunParser is a utility class for parsing GH CLI dry run outputs into a dictionary.
  """
  
  def __init__(self, dry_run_output : str):
    self.dry_run_output = dry_run_output
  
  def parse_output(self):
    output_lines = self.dry_run_output.strip().replace("\t", "").splitlines()

    last_key = ""
    output_dict: dict[str, Any] = {}
    
    for line in output_lines:
      key = line.split(":")[0]

      if not line_represents_array(line):
        last_key = key
        value = line.split(":")[1]
        
      else:
        if isinstance(output_dict[last_key], str):
          output_dict[last_key] = []
        value = output_dict[last_key] + [line]

      output_dict[last_key] = value

    return output_dict

def line_represents_array(line : str):
  return line.startswith("-")