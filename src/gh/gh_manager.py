from common import run_shell_command
from gh import gh_dry_run_parser
from gh.pull_request import PullRequest


def create_dry_pr(base: str = "main"):
  command_output = run_shell_command(f"gh pr create --dry-run --base \"{base}\" -f").split("\n", 1)[1]
  return gh_dry_run_parser.parse_output(command_output)


def create_pr(pull_request: PullRequest):
  command = f"""gh pr create --title "{pull_request.title}" --head "{pull_request.head}" --base "{pull_request.base}" --body \"{"\n".join(pull_request.body)}\""""
  command_output = run_shell_command(command)

  return command_output


