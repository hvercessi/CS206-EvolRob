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
        
        self.backLegSensorValues = numpy.zeros(c.simRange)
        self.frontLegSensorValues = numpy.zeros(c.simRange)

        self.targetAnglesBackLeg = c.backLegAmplitude*numpy.sin(c.backLegFrequency*numpy.linspace(c.xValsMin, c.xValsMax, c.simRange) + c.backLegPhaseOffset)
        self.targetAnglesFrontLeg = c.frontLegAmplitude*numpy.sin(c.frontLegFrequency*numpy.linspace(c.xValsMin, c.xValsMax, c.simRange) + c.frontLegPhaseOffset)

        
    def Run(self):
        for i in range(c.simRange):
            p.stepSimulation()
            self.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            self.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        
            pyrosim.Set_Motor_For_Joint(bodyIndex = (self.robot).robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = self.targetAnglesBackLeg[i], maxForce = 500)
            pyrosim.Set_Motor_For_Joint(bodyIndex = (self.robot).robotId, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = self.targetAnglesFrontLeg[i], maxForce = 500)
            print(i)
            t.sleep(c.sleepTime)
          