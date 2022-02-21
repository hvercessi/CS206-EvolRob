from world import WORLD
from robot import ROBOT
import pybullet as p
import time as t
import random as rand
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet_data
import numpy

class SIMULATION:

    def __init__(self):
        
        
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate((self.robot).robotId)
        (self.robot).Prepare_To_Sense()
        (self).robot.Prepare_To_Act()


        
    def Run(self):
        for i in range(c.simRange):
            p.stepSimulation()
            (self.robot).Sense(i)
            (self.robot).Act(i)
            
            
            t.sleep(c.sleepTime)
            
    def Save_Values(self):
        with open('data/SensorValues.npy', 'wb') as f:
            vals = []
            for name in self.sensors:
                vals.append(self.robot.sensors[name].values)
            numpy.save(f, vals)
    
    def __del__(self):
        p.disconnect()  