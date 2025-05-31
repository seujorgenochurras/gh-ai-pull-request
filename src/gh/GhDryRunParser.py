from typing import Any


def parse_output(raw_output: str):
  output_lines = raw_output.strip().replace("\t", "").splitlines()

  last_key = ""
  output_dict: dict[str, Any] = {}

  for line in output_lines:
    key = line.split(":")[0]

    if not _line_represents_array(line):
      last_key = key
      value = line.split(":")[1]

    else:
      if isinstance(output_dict[last_key], str):
        output_dict[last_key] = []
      value = output_dict[last_key] + [line]

    output_dict[last_key] = value

  return output_dict


def _line_represents_array(line: str):
  return line.startswith("-")
