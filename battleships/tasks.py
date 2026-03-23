import sys
from invoke import task

def run_cmd(c, command):
    """Helper to handle Windows pty issues."""
    c.run(command, pty=sys.platform != "win32")

@task
def start(c):
    run_cmd(c, "python src/index.py")