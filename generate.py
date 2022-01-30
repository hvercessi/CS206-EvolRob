# CS206 Evolutionary Robotics 
# Halina Vercessi
# Specifies what is in the world

import pyrosim.pyrosim as pyrosim

# Size values
length = 1.0
width = 1.0
height = 1.0

# Position Values
x = -2.0
y = -2.0
z = 0.5

def Create_World():

  pyrosim.Start_SDF("world.sdf")
 
  pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
  
  pyrosim.End()
  
  
def Create_Robot():
  pyrosim.Start_URDF("body.urdf")
  
  pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length,width,height])
  
  pyrosim.End()
  
Create_World()
Create_Robot()
