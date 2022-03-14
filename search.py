
import os
import time as t
import subprocess
from hillclimber import HILLCLIMBER
import os

subprocess.call("python generate.py")
subprocess.call("python simulate.py GUI")

hc = HILLCLIMBER()
hc.Evolve()
hc.Show_Best()