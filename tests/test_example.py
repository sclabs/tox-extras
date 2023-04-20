import os
import pathlib
import subprocess
import sys


def test_example():
    # copy the current env
    env = os.environ.copy()

    # delete keys that tox sets
    for key in list(env.keys()):
        if key.startswith("TOX_"):
            del env[key]

    # run tox from the example directory with the copied env
    subprocess.run("tox", cwd="./example", env=env, check=True)
