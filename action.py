import argparse
import subprocess
import sys


def main(requirements_file: str) -> None:
    # read the contents of the requirements file
    with open(requirements_file, "r") as fp:
        requirements = fp.readlines()

    # for each line
    for line in requirements:
        # remove leading and trailing whitespaces
        line = line.strip()
        # remove all whitespaces
        line.replace(" ", "")
        # remove comments
        if line.startswith("#"):
            continue

        # pipx install it
        print(f"::group::Installing {line}", flush=True)

        proc = subprocess.run(["pipx", "install", line])

        # catch errors
        if proc.returncode != 0:
            print(f"::error::{proc.stderr}")

        print("::endgroup::", flush=True)

        # if there was an error, exit
        if proc.returncode != 0:
            sys.exit(proc.returncode)

    # ensure that packages that were cached still are accessible
    subprocess.run(["pipx", "ensurepath"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("requirements_file", type=str)
    args = parser.parse_args()

    main(args.requirements_file)
