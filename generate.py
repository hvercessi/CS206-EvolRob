# CS206 Evolutionary Robotics 
# Halina Vercessi
# Specifies what is in the world

import pyrosim.pyrosim as pyrosim

# Size values
length = 1
width = 2
height = 3

# Position Values
x = 0
y = 0
z = 0.5


pyrosim.Start_SDF("box.sdf")
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
pyrosim.End()
