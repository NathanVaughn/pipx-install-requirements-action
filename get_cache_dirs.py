import os

import pipx.paths

with open(os.environ["GITHUB_OUTPUT"], "w") as fp:
    fp.write(f"pipx={pipx.paths.ctx.venvs}")
    fp.write(f"pip={os.path.join(os.path.expanduser("~"), ".cache", "pipx_pip")}")
