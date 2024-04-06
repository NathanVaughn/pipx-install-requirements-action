import os

pip_cache = os.path.join(os.environ["GITHUB_RUNNER_TEMP"], "pipx_pip")
pipx_cache = os.path.join(os.environ["GITHUB_RUNNER_TEMP"], "pipx_venvs")

with open(os.environ["GITHUB_OUTPUT"], "w") as fp:
    fp.write(f"pipx={pip_cache}\n")
    fp.write(f"pip={pip_cache}\n")
