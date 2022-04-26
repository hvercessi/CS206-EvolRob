import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import numpy

class ROBOT:
    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        
    def __init__(self, solutionID):
        self.motors = {}
        self.sensors = {}
        self.robotId = p.loadURDF("body.urdf")
        self.solutionID = solutionID
        
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")
        os.system("del " + "brain" + str(self.solutionID) + ".nndf")
    
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

            
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
            
    def Sense(self, i):
        for name in self.sensors:
            self.sensors[name].Get_Value(i)
            
    def Act(self, i):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                
                angle = self.nn.Get_Value_Of(neuronName)
                desiredAngle = angle* c.motorJointRange
                
                # if jointName == "LeftLeg_LeftLowerLeg" and self.nn.Get_Value_Of(5) != None and self.nn.Get_Value_Of(7) != None:
                    
                #     if (self.nn.Get_Value_Of(7) > self.nn.Get_Value_Of(5)):
                #         angle = self.nn.Get_Value_Of(5)
                #         desiredAngle = angle* c.motorJointRange
                #         self.motors[jointName].Set_Value(self, (desiredAngle))
                        
                # elif jointName == "RightLeg_RightLowerLeg" and self.nn.Get_Value_Of(6) != None and self.nn.Get_Value_Of(8) != None:
                #     if (self.nn.Get_Value_Of(8) > self.nn.Get_Value_Of(6)):
                #         angle = self.nn.Get_Value_Of(6)
                #         desiredAngle = angle* c.motorJointRange
                #         self.motors[jointName].Set_Value(self, (desiredAngle))
                # else:     
                self.motors[jointName].Set_Value(self, desiredAngle)
                #print(neuronName + ", " + jointName + ", ", end="")
                #print(desiredAngle)
        
            
    def Think(self):
        self.nn.Update()
        self.nn.Print()
        
    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)

        basePosition = basePositionAndOrientation[0]

        self.xPosition = basePosition[0]
        self.zPosition = basePosition[2]
        self.fitnessList =[self.solutionID, self.xPosition, self.zPosition]
        # print("\n*******************************\n")
        # print(xPosition)
        # print(zPosition)
        # print("\n*******************************\n")
   
        fitnessFileName = "fitness" + str(self.solutionID) + ".txt"
        tmpFile = "tmp" + str(self.solutionID) + ".txt"
        
        with open(tmpFile, 'w') as f:
            #print("writing to file")
            f.write(str(self.xPosition)+" "+str(self.zPosition))
            #print("done writing to file")
            
        os.system("rename " + tmpFile + " " + fitnessFileName)
        
        
    def Save_Values(self):
        with open('data/RobotFitness.npy', 'wb') as f:
            numpy.save(f, self.fitnessList)
        