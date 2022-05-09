
import os
import time as t
import subprocess
#from hillclimber import HILLCLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os

#subprocess.call("python generate.py")
#subprocess.call("python simulate.py GUI")

# hc = HILLCLIMBER()
# hc.Evolve()
# hc.Show_Best()

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
os.system("python analyze.py")
os.system("del fitness*.txt")
#os.system("del SolutionFitnessA.txt")

