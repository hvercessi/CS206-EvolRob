
import os
import time as t
import subprocess
from hillclimber import HILLCLIMBER
import os

hc = HILLCLIMBER()
hc.Evolve()

# com = ["python generate.py", "python simulate.py"]
# for i in range(2):
#     for c in com:
#         subprocess.call(c)