from world import WORLD
from robot import ROBOT
import pybullet as p
import time as t
import random as rand
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet_data
import numpy
import os

class SIMULATION:

    def __init__(self):
        
        self.physicsClient = p.connect(p.GUI)
        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate((self.robot).robotId)
        (self.robot).Prepare_To_Sense()
        (self.robot).Prepare_To_Act()
        
    def __init__(self, directOrGUI, solutionID):
        
        if directOrGUI == "DIRECT":
            self.directOrGUI = "DIRECT"
            self.physicsClient = p.connect(p.DIRECT)
        elif directOrGUI == "GUI":
            self.directOrGUI = "GUI"
            self.physicsClient = p.connect(p.GUI)
        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        pyrosim.Prepare_To_Simulate((self.robot).robotId)
        (self.robot).Prepare_To_Sense()
        (self.robot).Prepare_To_Act()
        
    def Run(self):
        for i in range(c.simRange):
            p.stepSimulation()
            (self.robot).Sense(i)
            
            self.robot.Think()
            
            (self.robot).Act(i)
            
            if self.directOrGUI == "GUI":
                t.sleep(c.sleepTime)
            
    def Get_Fitness(self):
        self.robot.Get_Fitness()
            
    
    def __del__(self):
        # for s in self.robot.sensors:
        #      self.robot.sensors[s].Save_Values()
        #      for m in self.robot.motors:
        #          self.robot.motors[m].Save_Values()
        self.robot.SaveValues()
        os.system("del fitness*.txt")
        p.disconnect()  