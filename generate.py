# CS206 Evolutionary Robotics 
# Halina Vercessi
# Specifies what is in the world

import pyrosim.pyrosim as pyrosim

# Size values
length = 1.0
width = 1.0
height = 1.0

# Position Values
x_body = 0.0
y_body = 0.0
z_body = 0.5

x_world = -3.0
y_world = 3.0
z_world = 0.5

def Create_World():

  pyrosim.Start_SDF("world.sdf")
 
  pyrosim.Send_Cube(name="Box", pos=[x_world,y_world,z_world] , size=[length,width,height])
  
  pyrosim.End()

def Generate_Body():
  pyrosim.Start_URDF("body.urdf")
  
  pyrosim.Send_Cube(name="Torso", pos=[1.5,0.0,1.5] , size=[length,width,height])
  
  pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso", child = "BackLeg", type = "revolute", position = [1.0,0.0,1.0])
  pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0.0,-0.5] , size=[length,width,height])
  
  pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2.0,0.0,1.0])
  pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0.0,-0.5] , size=[length,width,height])
  
  pyrosim.End()
  
def Generate_Brain():
  pyrosim.Start_NeuralNetwork("brain.nndf")
  
  pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
  pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
  pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
  
  pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
  pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")
  
  pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1.0 )
  pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )
  pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0 )
  pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -1.0 )

  
  
  pyrosim.End()

  
Create_World()
Generate_Body()
Generate_Brain()
