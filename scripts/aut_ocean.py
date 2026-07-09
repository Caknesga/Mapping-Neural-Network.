import subprocess
import os


env = os.environ.copy()

subprocess.run(
    ["./scripts/run_ocean.sh"],
    env=env,
    check=True
)