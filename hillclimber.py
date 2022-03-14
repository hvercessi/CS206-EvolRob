import pybullet as p
import pyrosim.pyrosim as pyrosim
from solution import SOLUTION
import numpy as np


class HILLCLIMBER:
    
    def __init__(self):
        self.parent = SOLUTION()
    
        
    def Evolve(self):
        self.parent.Evaluate()

