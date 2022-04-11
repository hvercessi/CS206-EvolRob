import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import random as rand
import numpy as np
import subprocess
import os
import time
import constants as c

class SOLUTION:
    
    def __init__(self):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        
        #print(self.weights)
        self.weights = self.weights*2 - 1
        #print(self.weights)
    
    def __init__(self, iD):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        
        self.weights = self.weights*2 - 1
        #print(self.weights)
        self.myID = iD

    def Set_ID(self, iD):
        self.myID = iD
    
    def Create_World(self):
          
      pyrosim.Start_SDF("world.sdf")
     
      pyrosim.Send_Cube(name="Box", pos=[c.x_world,c.y_world,c.z_world] , size=[c.length,c.width,c.height])
      
      # while not os.path.exists("world.sdf"):
      #     time.sleep(0.01)
          
      pyrosim.End()

    def Generate_Body(self):
    
      pyrosim.Start_URDF("body.urdf")
      
      pyrosim.Send_Cube(name="Torso", pos=[0.0,0.0,3.25] , size=[c.length,c.width,c.height])
      
      # Upper Legs
      pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [0.0,0.3,2.2], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name="LeftLeg", pos=[0.0,0.0,0.0] , size=[0.4,0.3,1.75])
           
      pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso", child = "RightLeg", type = "revolute", position = [0.0,-0.3,2.2], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name="RightLeg", pos=[0.0,0.0,0.0] , size=[0.4,0.3,1.75]) 
      
      # Lower Legs
      pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [0.0,0.0,-0.79], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.4,0.3,1.25])
      
      pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [0.0,0.0,-0.79], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name="RightLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.4,0.3,1.25])
      
      # Feet
      pyrosim.Send_Joint( name = "LeftLowerLeg_LeftFoot" , parent= "LeftLowerLeg" , child = "LeftFoot" , type = "revolute", position = [0.1,0.0,-0.6], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name="LeftFoot", pos=[0.1,0.0,-0.6] , size=[0.85,0.45,0.15])
      
      pyrosim.Send_Joint( name = "RightLowerLeg_RightFoot" , parent= "RightLowerLeg" , child = "RightFoot" , type = "revolute", position = [0.1,0.0,-0.6], jointAxis = "0 1 0")
      pyrosim.Send_Cube(name="RightFoot", pos=[0.1,0.0,-0.6] , size=[0.85,0.45,0.15])
      
      
      # pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0.0,1.0], jointAxis = "0 1 0") # 0 1 0 
      # pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0.0,0.0] , size=[1.0,0.2,0.2])
      
      # pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0.0,1.0], jointAxis = "0 1 0") # 0 1 0 
      # pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0.0,0.0] , size=[1.0,0.2,0.2])
      
      # # Lower Legs
      # pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0.0,1.0,0.0], jointAxis = "1 0 0")
      # pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1.0])
      
      # pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0.0,-1.0,0.0], jointAxis = "1 0 0")
      # pyrosim.Send_Cube(name="BackLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1.0])
      
      # pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1.0,0.0,0.0], jointAxis = "0 1 0")
      # pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1.0])
      
      # pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1.0,0.0,0.0], jointAxis = "0 1 0")
      # pyrosim.Send_Cube(name="RightLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1.0])
      
         
      pyrosim.End()
      
    def Generate_Brain(self):
      pyrosim.Start_NeuralNetwork("brain" + str(self.myID) +".nndf")
    
      
      pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
      pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LeftFoot")
      pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "RightFoot")
     
      
      # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
      # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
      
      
      # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLowerLeg")
      # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
      # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg")
      # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg")
      
      pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_LeftLeg")
      pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_RightLeg")
      
      pyrosim.Send_Motor_Neuron(name = 5 , jointName = "LeftLeg_LeftLowerLeg")
      pyrosim.Send_Motor_Neuron(name = 6 , jointName = "RightLeg_RightLowerLeg")
      
      pyrosim.Send_Motor_Neuron(name = 7 , jointName = "LeftLowerLeg_LeftFoot")
      pyrosim.Send_Motor_Neuron(name = 8 , jointName = "RightLowerLeg_RightFoot")
      
      # pyrosim.Send_Motor_Neuron(name = 6 , jointName = "Torso_LeftLeg")
      # pyrosim.Send_Motor_Neuron(name = 7 , jointName = "Torso_RightLeg")
      
      # pyrosim.Send_Motor_Neuron(name = 8 , jointName = "FrontLeg_FrontLowerLeg")
      # pyrosim.Send_Motor_Neuron(name = 9 , jointName = "BackLeg_BackLowerLeg")
      # pyrosim.Send_Motor_Neuron(name = 10, jointName = "LeftLeg_LeftLowerLeg")
      # pyrosim.Send_Motor_Neuron(name = 11 , jointName = "RightLeg_RightLowerLeg")
      
      for currentRow in range(c.numSensorNeurons):
          for currentColumn in range(c.numMotorNeurons):
              pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, \
                                   weight = self.weights[currentRow][currentColumn])
             
      # while not os.path.exists("brain.nndf"):
      #     time.sleep(0.01)
          
      pyrosim.End()
      
    def Mutate(self):
        randomRow = rand.randint(0, c.numSensorNeurons-1)
        randomColumn = rand.randint(0, c.numMotorNeurons-1)

        self.weights[randomRow, randomColumn] = rand.random() * 2 - 1
        
      
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID) )
    
    def Wait_For_Simulation_To_End(self):
        fitnessFileName = fitnessFileName = "fitness" + str(self.myID) + ".txt"
        
        while not os.path.exists(fitnessFileName):
          time.sleep(0.01)
          
        with open(fitnessFileName) as fitnessFile:
            fitnessList = fitnessFile.readline().split(" ")
            self.fitnessX = float(fitnessList[0])
            self.fitnessZ = float(fitnessList[1])
        
        # print("\n****************************\n")
        # print("Fitness " + str(self.myID) + ": " + str(self.fitness))
        # print("\n****************************\n")
            
        os.system("del " + fitnessFileName)
        
    
      