import pybullet as p
import pyrosim.pyrosim as pyrosim
from solution import SOLUTION
import numpy as np
import constants as c
import copy 
import os

class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        
        self.nextAvailableID = 0
        
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID+1

        
        
    def Spawn(self):
        self.children = {}
        for key in self.parents:
            
            self.children[key] = copy.deepcopy(self.parents[key])
        
            self.children[key].Set_ID(self.nextAvailableID)
        
            self.nextAvailableID = self.nextAvailableID + 1


    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()


    def Select(self):
        for key in self.parents:
            if (self.parents[key].fitnessX < self.children[key].fitnessX) and (self.parents[key].fitnessZ < self.children[key].fitnessZ):
                self.parents[key] = self.children[key]
            
    def Print(self):
        pass
        # for key in self.parents:
        #     print("\n*********************************************\n")
        #     print("Parent fitness:", self.parents[key].fitnessX, self.parents[key].fitnessZ)
        #     print("Child fitness:", self.children[key].fitnessX, self.children[key].fitnessZ)
        #     print("\n*********************************************\n")
        
    def Show_Best(self):
        bestX = -100000000.0
        bestZ = -100000000.0
        keyBest = 0
        for key in self.parents:
            if ((self.parents[key].fitnessX > bestX) and (self.parents[key].fitnessZ > bestZ)):
                keyBest = key
                bestX = self.parents[key].fitnessX
                bestZ = self.parents[key].fitnessZ
        print("\n*********************************************\n")
        print("\n             Best Fitness: "+ str(bestX)+" "+str(bestZ))
        print("\n*********************************************\n")
        self.parents[keyBest].Start_Simulation("GUI")
        
    
    def Evaluate(self, solutions):
        for key in solutions:
            (solutions[key]).Start_Simulation("DIRECT")
            
        for key in solutions:
            (solutions[key]).Wait_For_Simulation_To_End()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)
        
        self.Print()

        self.Select()
        
        
        
    def Evolve(self):

        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
        
        # for key in self.parents:
        #     (self.parents[key]).Start_Simulation("DIRECT")
            
        # for key in self.parents:
        #     (self.parents[key]).Wait_For_Simulation_To_End()
            
        self.Evaluate(self.parents)
        
        for currentGeneration in range(c.numberOfGenerations):
            print("\n        Generation: " + str(currentGeneration)+"\n")
            self.Evolve_For_One_Generation()
             
        

    

