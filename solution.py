import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import random as rand
import numpy as np
import subprocess
import os
import time
import constants as c
import numpy

class SOLUTION:
    
    def __init__(self):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        
        #print(self.weights)
        self.weights = self.weights*2 - 1
        #print(self.weights)
    
    def __init__(self, iD,gen):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        
        self.weights = self.weights*2 - 1
        #print(self.weights)
        self.myID = iD
        self.gen=gen

    def Set_ID(self, iD):
        self.myID = iD
    
    def Create_World(self):
          
      pyrosim.Start_SDF("world.sdf")
     
      pyrosim.Send_Cube(name="Box", pos=[c.x_world,c.y_world,c.z_world] , size=[c.length,c.width,c.height])
      
      while not os.path.exists("world.sdf"):
          time.sleep(0.01)
          
      pyrosim.End()

    def Generate_Body(self):
    
      pyrosim.Start_URDF("body.urdf")
      
      
      pyrosim.Send_Cube(name="Hips", pos=[0.0,0.0,4.0] , size=[0.8,1.0,0.5],mass=2.5)
      
      
      # Upper Legs
      pyrosim.Send_Joint( name = "Hips_LeftLeg" , parent= "Hips" , child = "LeftLeg",\
                         type = "revolute", position = [0.0,0.5,4.0], jointAxis = "0 1 0", upperLimit = numpy.pi/4, lowerLimit = -numpy.pi/2)
      pyrosim.Send_Cube(name="LeftLeg", pos=[0.0,0.0,-1.125] , size=[0.45,0.45,2.25], mass=3.5)
           
      pyrosim.Send_Joint( name = "Hips_RightLeg" , parent= "Hips", child = "RightLeg",\
                         type = "revolute", position = [0.0,-0.5,4.0], jointAxis = "0 1 0", upperLimit = numpy.pi/4, lowerLimit = -numpy.pi/2)
      pyrosim.Send_Cube(name="RightLeg", pos=[0.0,0.0,-1.125] , size=[0.45,0.45,2.25],mass=3.5) 
      
      # Lower Legs
      pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg",\
                         type = "revolute", position = [0.0,0.0,-2.25], jointAxis = "0 1 0", upperLimit = numpy.pi/2.0, lowerLimit = 0.0)
      pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0.0,0.0,-0.8125] , size=[0.35,0.35,1.625], mass=2.75)
      
      pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg",\
                         type = "revolute", position = [0.0,0.0,-2.25], jointAxis = "0 1 0", upperLimit = numpy.pi/2.0, lowerLimit = 0.0)
      pyrosim.Send_Cube(name="RightLowerLeg", pos=[0.0,0.0,-0.8125] , size=[0.35,0.35,1.625],mass=2.75)
      
      # Feet
      pyrosim.Send_Joint( name = "LeftLowerLeg_LeftFoot" , parent= "LeftLowerLeg" , child = "LeftFoot",\
                         type = "revolute", position = [0.0,0.0,-1.625], jointAxis = "0 1 0", upperLimit = numpy.pi/12.0, lowerLimit = -numpy.pi/6.0)
      pyrosim.Send_Cube(name="LeftFoot", pos=[0.0,0.0,-0.0625] , size=[0.675,0.675,0.225], mass=1.5)
      
      pyrosim.Send_Joint( name = "RightLowerLeg_RightFoot" , parent= "RightLowerLeg" , child = "RightFoot",\
                         type = "revolute", position = [0.0,0.0,-1.625], jointAxis = "0 1 0", upperLimit = numpy.pi/12.0, lowerLimit = -numpy.pi/6.0)
      pyrosim.Send_Cube(name="RightFoot", pos=[0.0,0.0,-0.0625] , size=[0.675,0.675,0.225],mass=1.5)
      
      
      # Lower Torso
      pyrosim.Send_Joint( name = "Hips_LowerTorso" , parent= "Hips" , child = "LowerTorso",\
                         type = "fixed", position = [0.0,0.0,4.25], jointAxis = "0 1 0", upperLimit = numpy.pi/12.0, lowerLimit = -numpy.pi/12.0)
      pyrosim.Send_Cube(name="LowerTorso", pos=[0.0,0.0,0.125] , size=[0.675,0.875,0.25],mass=1.0)
      
      # Mid Torso
      pyrosim.Send_Joint( name = "LowerTorso_MidTorso" , parent= "LowerTorso" , child = "MidTorso",\
                         type = "fixed", position = [0.0,0.0,0.25], jointAxis = "0 1 0", upperLimit = 0.0, lowerLimit = 0.0)
      pyrosim.Send_Cube(name="MidTorso", pos=[0.0,0.0,0.125] , size=[0.55,0.75,0.25])
      
      # # Upper Torso
      # pyrosim.Send_Joint( name = "MidTorso_UpperTorso" , parent= "MidTorso" , child = "UpperTorso",\
      #                    type = "revolute", position = [0.0,0.0,0.25], jointAxis = "0 1 0", upperLimit = numpy.pi/12.0, lowerLimit = -numpy.pi/12.0)
      # pyrosim.Send_Cube(name="UpperTorso", pos=[0.0,0.0,0.25] , size=[0.65,0.85,0.5])
      
      # # Shoulders
      # pyrosim.Send_Joint( name = "UpperTorso_LeftShoulder" , parent= "UpperTorso" , child = "LeftShoulder",\
      #                    type = "revolute", position = [0.0,0.0,0.625], jointAxis = "0 0 1", upperLimit = 0.0, lowerLimit = 0.0)
      # pyrosim.Send_Cube(name="LeftShoulder", pos=[0.0,-0.5625,0.0] , size=[0.55,1.125,0.25])
      
      # pyrosim.Send_Joint( name = "UpperTorso_RightShoulder" , parent= "UpperTorso" , child = "RightShoulder",\
      #                    type = "revolute", position = [0.0,0.0,0.625], jointAxis = "0 0 1", upperLimit = 0.0, lowerLimit = 0.0)
      # pyrosim.Send_Cube(name="RightShoulder", pos=[0.0,0.5625,0.0] , size=[0.55,1.125,0.25])
      
      # # Left Upper Arm
      # pyrosim.Send_Joint( name = "LeftShoulder_LeftUpperArm" , parent= "LeftShoulder" , child = "LeftUpperArm",\
      #                    type = "revolute", position = [0.0,-1.125,0.0], jointAxis = "1 1 0", upperLimit = numpy.pi/8.0, lowerLimit = -numpy.pi/8.0)
      # pyrosim.Send_Cube(name="LeftUpperArm", pos=[0.0,0.0,-0.5] , size=[0.35,0.35,1.0], mass=2.0)
      
      # # Right Upper Arm
      # pyrosim.Send_Joint( name = "RightShoulder_RightUpperArm" , parent= "RightShoulder" , child = "RightUpperArm",\
      #                    type = "revolute", position = [0.0,1.125,0.0], jointAxis = "1 1 0", upperLimit = numpy.pi/8.0, lowerLimit = -numpy.pi/8.0)
      # pyrosim.Send_Cube(name="RightUpperArm", pos=[0.0,0.0,-0.5] , size=[0.35,0.35,1.0], mass=2.0)
      
      # # Left Lower Arm
      # pyrosim.Send_Joint( name = "LeftUpperArm_LeftLowerArm" , parent= "LeftUpperArm" , child = "LeftLowerArm",\
      #                    type = "revolute", position = [0.0,0.0,-0.875], jointAxis = "0 1 0", upperLimit = 0.0, lowerLimit = -numpy.pi/6.0)
      # pyrosim.Send_Cube(name="LeftLowerArm", pos=[0.0,0.0,-0.475] , size=[0.3,0.3,0.95],mass=1.5)
      
      # # Right Lower Arm
      # pyrosim.Send_Joint( name = "RightUpperArm_RightLowerArm" , parent= "RightUpperArm" , child = "RightLowerArm",\
      #                    type = "revolute", position = [0.0,0.0,-0.875], jointAxis = "0 1 0", upperLimit = 0.0, lowerLimit = -numpy.pi/6.0)
      # pyrosim.Send_Cube(name="RightLowerArm", pos=[0.0,0.0,-0.475] , size=[0.3,0.3,0.95],mass=1.5)
      
      
      
      
      
      while not os.path.exists("body.urdf"):
          time.sleep(0.01)
          
         
      pyrosim.End()
      
    def Generate_Brain(self):
      pyrosim.Start_NeuralNetwork("brain" + str(self.myID) +".nndf")
    
      
      pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Hips")
      pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LeftFoot")
      pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "RightFoot")
     
      
      # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
      # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
      
      
      # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLowerLeg")
      # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
      # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLowerLeg")
      # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLowerLeg")
      
      
      # MOTOR NEURONS
      pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Hips_LowerTorso")
      pyrosim.Send_Motor_Neuron(name = 4 , jointName = "LowerTorso_MidTorso")
      pyrosim.Send_Motor_Neuron(name = 5 , jointName = "MidTorso_UpperTorso")
      
      # pyrosim.Send_Motor_Neuron(name = 6 , jointName = "UpperTorso_LeftShoulder")
      # pyrosim.Send_Motor_Neuron(name = 7 , jointName = "UpperTorso_RightShoulder") 
      
      # pyrosim.Send_Motor_Neuron(name = 8 , jointName = "LeftShoulder_LeftUpperArm")
      # pyrosim.Send_Motor_Neuron(name = 9, jointName = "RightShoulder_RightUpperArm")
      # pyrosim.Send_Motor_Neuron(name = 10, jointName = "LeftUpperArm_LeftLowerArm")
      # pyrosim.Send_Motor_Neuron(name = 11, jointName = "RightUpperArm_RightLowerArm")
      
      pyrosim.Send_Motor_Neuron(name = 6 , jointName = "Hips_LeftLeg")
      pyrosim.Send_Motor_Neuron(name = 7, jointName = "Hips_RightLeg")
      
      pyrosim.Send_Motor_Neuron(name = 8 , jointName = "LeftLeg_LeftLowerLeg")
      pyrosim.Send_Motor_Neuron(name = 9 , jointName = "RightLeg_RightLowerLeg")
      
      pyrosim.Send_Motor_Neuron(name = 10 , jointName = "LeftLowerLeg_LeftFoot")
      pyrosim.Send_Motor_Neuron(name = 11, jointName = "RightLowerLeg_RightFoot")
      
      
      for currentRow in range(c.numSensorNeurons):
          for currentColumn in range(c.numMotorNeurons):
              pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, \
                                   weight = self.weights[currentRow][currentColumn])
             
      while not os.path.exists("brain" + str(self.myID) +".nndf"):
          time.sleep(0.01)
          
      pyrosim.End()
      
    def Mutate(self):
        randomRow = rand.randint(0, c.numSensorNeurons-1)
        randomColumn = rand.randint(0, c.numMotorNeurons-1)

        self.weights[randomRow, randomColumn] = rand.random() * 2 - 1
        #self.weights[randomRow, randomColumn] = rand.random()
        
      
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID)+ " " + str(self.gen ))
    
    
    def Wait_For_Simulation_To_End(self):
        fitnessFileName = fitnessFileName = "fitness" + str(self.myID) + ".txt"
        
        while not os.path.exists(fitnessFileName):
          time.sleep(0.01)
          
        try:
            with open(fitnessFileName, 'r') as fitnessFile:
                self.fitness = float(fitnessFile.readline())
        except PermissionError:
            os.system("chmod +r " + fitnessFileName)
            
        os.system("del " + fitnessFileName)
        
    
    def Save_Values(self):
        #self.fitnessList = [self.gen, self.xPosition, self.zPosition]
        f = open('SolutionFitnessA.txt', 'a')
        f.write(str(self.gen)+"|"+str(self.fitness)+"\n")
        f.close()