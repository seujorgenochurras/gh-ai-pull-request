import subprocess
from gh import GhDryRunParser
from gh.PullRequest import PullRequest


def create_dry_pr():
  command_output = _run_shell_command("gh pr create --dry-run -f").split("\n", 1)[1]
  return GhDryRunParser.parse_output(command_output)


def create_pr(pull_request: PullRequest):
  command = f"""gh pr create --title "{pull_request.title}" --head "{pull_request.head}" --base "{pull_request.base}" --body \"{"\n".join(pull_request.body)}\""""
  command_output = _run_shell_command(command)

  return command_output


def _run_shell_command(command: str):
  command_output = (
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    .stdout.read()  # type: ignore
    .decode()
  )
  return command_output
