import pybullet as p
import pyrosim.pyrosim as pyrosim
from solution import SOLUTION
import numpy as np
import constants as c
import copy 


class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        self.parent = SOLUTION()
        
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child
            
    def Print(self):
        print("\n*********************************************\n")
        print("Parent fitness:", self.parent.fitness, "Child fitness:", self.child.fitness)
        print("\n*********************************************\n")
        
    def Show_Best(self):
        self.parent.Evaluate("GUI")
    
    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate("DIRECT")
        
        self.Print()

        self.Select()
        
    def Evolve(self):
        self.parent.Evaluate("DIRECT")
        
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    

