# CS206 Evolutionary Robotics 
# Halina Vercessi
# Specifies what is in the world

import pyrosim.pyrosim as pyrosim

# Size values
length = 1
width = 1
height = 1

# Position Values
x = 1
y = 2
z = 3


pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
pyrosim.End()
