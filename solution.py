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
      
      pyrosim.Send_Cube(name="Torso", pos=[0.0,0.0,1.0] , size=[c.length,c.width,c.height])
      
      pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso", child = "BackLeg", type = "revolute", position = [0.0,-0.5,1.0], jointAxis = "1 0 0")
      pyrosim.Send_Cube(name="BackLeg", pos=[0.0,-0.5,0.0] , size=[0.2,1,0.2])
      
      pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.0,0.5,1.0], jointAxis = "1 0 0")
      pyrosim.Send_Cube(name="FrontLeg", pos=[0.0,0.5,0.0] , size=[0.2,1,0.2])
      
      pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0.0,1.0], jointAxis = "1 0 0")
      pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0.0,0.0] , size=[1.0,0.2,0.2])
      
      pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0.0,1.0], jointAxis = "1 0 0")
      pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0.0,0.0] , size=[1.0,0.2,0.2])
      
      # Lower Legs
      pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0.0,1.0,0.0], jointAxis = "1 0 0")
      pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1.0])
      
      pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0.0,-1.0,0.0], jointAxis = "1 0 0")
      pyrosim.Send_Cube(name="BackLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1.0])
      
      
      # while not os.path.exists("body.urdf"):
      #     time.sleep(0.01)
         
      pyrosim.End()
      
    def Generate_Brain(self):
      pyrosim.Start_NeuralNetwork("brain" + str(self.myID) +".nndf")
    
      
      pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
      pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
      pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
      pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
      pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
      pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "BackLowerLeg")
      pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "FrontLowerLeg")
      
      pyrosim.Send_Motor_Neuron(name = 7 , jointName = "Torso_BackLeg")
      pyrosim.Send_Motor_Neuron(name = 8 , jointName = "Torso_FrontLeg")
      pyrosim.Send_Motor_Neuron(name = 9 , jointName = "Torso_LeftLeg")
      pyrosim.Send_Motor_Neuron(name = 10 , jointName = "Torso_RightLeg")
      pyrosim.Send_Motor_Neuron(name = 11 , jointName = "BackLeg_BackLowerLeg")
      pyrosim.Send_Motor_Neuron(name = 12 , jointName = "FrontLeg_FrontLowerLeg")
      
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
            self.fitness = float(fitnessFile.readline())
        
        # print("\n****************************\n")
        # print("Fitness " + str(self.myID) + ": " + str(self.fitness))
        # print("\n****************************\n")
            
        os.system("del " + fitnessFileName)
        
    
      