import subprocess


def run_shell_command(command: str):
  command_output = (
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    .stdout.read()  # type: ignore
    .decode()
  )
  return command_output
