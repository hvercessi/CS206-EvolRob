import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
import simulation as s
import numpy

class MOTOR:
    def __init__(self, name, offset, freq, amp):
        
        self.jointName = name
        self.motorValues = []
        #self.Prepare_To_Act()
        self.offset = offset
        self.frequency = freq
        self.amplitude = amp
        
    # def Prepare_To_Act(self):
    #     self.amplitude = (numpy.pi/4.0)
    #     if self.jointName == "Torso_BackLeg":
    #         self.frequency = 5
    #     else:
    #         self.frequency = 10
    #     self.offset = 0
    #     self.motorValues = []
    #     self.angleValues = self.amplitude*numpy.sin(\
    #                                self.frequency*numpy.linspace(\
    #                                c.xValsMin, c.xValsMax, c.simRange) + self.offset)
        
    def Set_Value(self, robot, desiredAngle):
        self.angleValue = self.amplitude*numpy.sin(self.frequency*desiredAngle + self.offset) 
        self.motorValues.append( \
                           pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robotId, \
                                                       jointName = self.jointName, \
                                                       controlMode = p.POSITION_CONTROL, \
                                                       targetPosition = self.angleValue, \
                                                       maxForce = 300) )
    def Get_Value(self):
        pass
    def Save_Values(self):
        with open('data/MotorValues.npy', 'wb') as f:
            numpy.save(f, self.motorValues)
       