# pipx-install-requirements-action

This is a GitHub Action to install tools with `pipx` from a `requirements.txt` file.
This will cache the installed tools and downloaded dependencies.

This allows you to have consistent tool versions and leverage dependabot to keep
them up-to-date.

## Usage

```txt
poetry==1.8.2
vscode-task-runner==1.1.0
```

```yml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Install poetry/vscode-task-runner
        uses: NathanVaughn/pipx-install-requirements-action@main
        with:
          requirements_file: requirements.txt
```
