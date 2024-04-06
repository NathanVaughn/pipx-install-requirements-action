import os

import pipx.paths

pip_cache = os.path.join(os.path.expanduser("~"), ".cache", "pipx_pip")

with open(os.environ["GITHUB_OUTPUT"], "w") as fp:
    fp.write(f"pipx={pipx.paths.ctx.venvs}")
    fp.write(f"pip={pip_cache}")
