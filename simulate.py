# CS206 Evolutionary Robotics Assignment 1
# Halina Vercessi

# Use pybullet to simulate the world

import pybullet as p
import time as t
import math
import random as rand
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

amplitude = numpy.pi/4.0
frequency = 1
phaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

targetAngles = numpy.sin(numpy.linspace(0, 2*(numpy.pi), 1000))
#targetAngles = ((targetAngles+1)/2)*((math.pi)/4.0 - (-(math.pi)/4.0)) + (-(math.pi)/4.0)
targetAngles = amplitude * numpy.sin(frequency * targetAngles + phaseOffset)
with open('data/Position_Values.npy', 'wb') as f3:
  numpy.save(f3, targetAngles)
exit()


for i in range(1000):
  p.stepSimulation()
  backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
  #targetPos1 = rand.random()
  #targetPos1 = targetPos1*((math.pi)/2.0 - (-(math.pi)/2.0)) + (-(math.pi)/2.0)
  #targetPos2 = rand.random()
  #targetPos2 = targetPos2*((math.pi)/2.0 - (-(math.pi)/2.0)) + (-(math.pi)/2.0)
  
  pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAngles[i], maxForce = 500)
  pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAngles[i], maxForce = 500)
  
  t.sleep(1/70)
print(backLegSensorValues)
print(frontLegSensorValues)
with open('data/BackLegSensorValues.npy', 'wb') as f1:
  numpy.save(f1, backLegSensorValues)
with open('data/FrontLegSensorValues.npy', 'wb') as f2:
  numpy.save(f2, frontLegSensorValues)
p.disconnect()

