import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import random as rand
import numpy as np
import subprocess
import os
import time

class SOLUTION:
    
    def __init__(self):
        self.weights = np.random.rand(3,2)
        
        #print(self.weights)
        self.weights = self.weights*2 - 1
        #print(self.weights)
    
    def __init__(self, iD):
        self.weights = np.random.rand(3,2)
    
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
      
      pyrosim.Send_Cube(name="Torso", pos=[1.5,0.0,1.5] , size=[c.length,c.width,c.height])
      
      pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso", child = "BackLeg", type = "revolute", position = [1.0,0.0,1.0])
      pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0.0,-0.5] , size=[c.length,c.width,c.height])
      
      pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2.0,0.0,1.0])
      pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0.0,-0.5] , size=[c.length,c.width,c.height])
      
      # while not os.path.exists("body.urdf"):
      #     time.sleep(0.01)
          
      pyrosim.End()
      
    def Generate_Brain(self):
      pyrosim.Start_NeuralNetwork("brain" + str(self.myID) +".nndf")
    
      
      pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
      pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
      pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
      
      pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
      pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")
      
      # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )
      # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -1.0 )
      # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )
      # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.0 )

      for currentRow in [0,1,2]:
          for currentColumn in [0,1]:
              #w = rand.uniform(-1,1)
              pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, \
                                   weight = self.weights[currentRow][currentColumn])
              
      # while not os.path.exists("brain.nndf"):
      #     time.sleep(0.01)
          
      pyrosim.End()
      
    def Mutate(self):
        randomRow = rand.randint(0, 2)
        randomColumn = rand.randint(0, 1)

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
            print("\n****************************\n")
            print("Fitness " + str(self.myID) + ": " + str(self.fitness))
            print("\n****************************\n")
      
        os.system("del " + fitnessFileName)
        
    def Evaluate(self, directOrGUI):
      self.Create_World()
      self.Generate_Body()
      self.Generate_Brain()
      fitnessFileName = fitnessFileName = "fitness" + str(self.myID) + ".txt"
      
      #subprocess.call("python simulate.py " + directOrGUI + " &")
      #os.system("python generate.py")
      os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID) )
      while not os.path.exists(fitnessFileName):
          time.sleep(0.01)
          
      with open(fitnessFileName) as fitnessFile:
          self.fitness = float(fitnessFile.readline())
          print("\n****************************\n")
          print("Fitness " + str(self.myID) + ": " + str(self.fitness))
          print("\n****************************\n")
      
      