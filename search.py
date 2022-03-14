
import os
import time as t

import subprocess

com = ["python generate.py", "python simulate.py"]


for i in range(5):
    for c in com:
        subprocess.call(c)