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

x2 = 1.0
y2 = 0.0
z2 = 1.5

def Create_World():
  pyrosim.Start_SDF("world.sdf")

  for h in range(5):
    for j in range(5):
      for i in range(10):
        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        z+=1
        length = length-(length*0.1)
        width = width-(width*0.1)
        height = height-(height*0.1)
      # Set size back to 1x1x1
      length = 1
      width = 1
      height = 1
      # Set position to next row over
      x+=1
      z = 0.5
    x = -2.0
    y+=1.0

  pyrosim.End()
  
Create_World()
