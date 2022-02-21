import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
import simulation as s
import numpy

class MOTOR:
    def __init__(self, name):
        
        self.jointName = name
        self.Prepare_To_Act()
        
    def Prepare_To_Act(self):
        self.amplitude = (numpy.pi/4.0)
        self.frequency = 10
        self.offset = 0
        self.motorValues = []
        self.angleValues = self.amplitude*numpy.sin(\
                                   self.frequency*numpy.linspace(\
                                   c.xValsMin, c.xValsMax, c.simRange) + self.offset)
        
    def Set_Value(self, robot, i):
        self.motorValues.append( \
                           pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robotId, \
                                                       jointName = self.jointName, \
                                                       controlMode = p.POSITION_CONTROL, \
                                                       targetPosition = self.angleValues[i], \
                                                       maxForce = 500) )
       