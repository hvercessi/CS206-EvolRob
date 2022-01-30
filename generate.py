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
  
  
def Create_Robot():
  pyrosim.Start_URDF("body.urdf")
  
  pyrosim.Send_Cube(name="Link0", pos=[x_body,y_body,z_body] , size=[length,width,height])
  pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0.5,0.0,1.0])
  pyrosim.Send_Cube(name="Link1", pos=[0.5,0.0,0.5] , size=[length,width,height])
  
  pyrosim.End()
  
Create_World()
Create_Robot()
