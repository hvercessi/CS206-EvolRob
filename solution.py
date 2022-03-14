import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import random as rand
import numpy as np
import subprocess

class SOLUTION:
    
    def __init__(self):
        self.weights = np.random.rand(3,2)
        
        #print(self.weights)
        self.weights = self.weights*2 - 1
        #print(self.weights)

    
    def Create_World(self):

      pyrosim.Start_SDF("world.sdf")
     
      pyrosim.Send_Cube(name="Box", pos=[c.x_world,c.y_world,c.z_world] , size=[c.length,c.width,c.height])
      
      pyrosim.End()

    def Generate_Body(self):
      pyrosim.Start_URDF("body.urdf")
      
      pyrosim.Send_Cube(name="Torso", pos=[1.5,0.0,1.5] , size=[c.length,c.width,c.height])
      
      pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso", child = "BackLeg", type = "revolute", position = [1.0,0.0,1.0])
      pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0.0,-0.5] , size=[c.length,c.width,c.height])
      
      pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2.0,0.0,1.0])
      pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0.0,-0.5] , size=[c.length,c.width,c.height])
      
      pyrosim.End()
      
    def Generate_Brain(self):
      pyrosim.Start_NeuralNetwork("brain.nndf")
    
      
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
              
      pyrosim.End()
      
    def Mutate(self):
        randomRow = rand.randint(0, 2)
        randomColumn = rand.randint(0, 1)

        self.weights[randomRow, randomColumn] = rand.random() * 2 - 1
        
      
    def Evaluate(self, directOrGUI):
      self.Create_World()
      self.Generate_Body()
      self.Generate_Brain()
      subprocess.call("python simulate.py "+directOrGUI)
      
      with open("fitness.txt") as fitnessFile:
          self.fitness = float(fitnessFile.readline())
      
      