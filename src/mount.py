import os
import subprocess

def setup_mounts():
    subprocess.run(["mount", "-t", "proc", "proc", "/proc"], check=True)
