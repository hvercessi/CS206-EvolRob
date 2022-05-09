import pybullet as p
import pyrosim.pyrosim as pyrosim
from solution import SOLUTION
import numpy as np
import constants as c
import copy 
import os
import random as rand


class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        
        while os.path.exists("fitness*.txt"):
            os.system("del fitness*.txt")
        
        while os.path.exists("brain*.nndf"):
            os.system("del brain*.nndf")
        
        self.nextAvailableID = 0
        self.currGen=0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID,self.currGen)
            self.nextAvailableID = self.nextAvailableID+1

        
        
    def Spawn(self):
        self.children = {}
        for key in self.parents:
            
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].gen = self.parents[key].gen + 1
        
            self.children[key].Set_ID(self.nextAvailableID)
        
            self.nextAvailableID = self.nextAvailableID + 1


    def Mutate(self):
        
        for key in self.children:
            if self.children[key].myID % 2 == 0:
                self.children[key].Mutate()
                
            self.children[key].Mutate()
                
    def Select(self):
        for key in self.parents:
            if (self.parents[key].fitness < self.children[key].fitness):
                self.parents[key] = self.children[key]
                #self.parents[key].gen = self.currGen
                self.parents[key].Save_Values()
        
            
    def Print(self):
        pass
        # for key in self.parents:
        #     print("\n*********************************************\n")
        #     print("Parent fitness:", self.parents[key].fitnessX, self.parents[key].fitnessZ)
        #     print("Child fitness:", self.children[key].fitnessX, self.children[key].fitnessZ)
        #     print("\n*********************************************\n")
        
    def Show_Best(self):
        best = -100000000.0
        
        keyBest = 0
        for key in self.parents:
            if ((self.parents[key].fitness > best)):
                keyBest = key
                best = self.parents[key].fitness
                
        print("\n*********************************************\n")
        print("\n             Best Fitness: "+ str(best))
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
        
        self.Mutate()


        self.Evaluate(self.children)
        
        #self.Print()

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
            self.currGen = currentGeneration
            print("\n        Generation: " + str(currentGeneration+1)+"\n")
            self.Evolve_For_One_Generation()
             
        

    

