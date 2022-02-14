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

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

position_seq_vect = numpy.linspace(0, 2*(numpy.pi), 1000)
translated_pos_vals = numpy.sin(position_seq_vect)

for i in range(1000):
  p.stepSimulation()
  backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
  targetPos1 = rand.random()
  targetPos1 = targetPos1*((math.pi)/2.0 - (-(math.pi)/2.0)) + (-(math.pi)/2.0)
  targetPos2 = rand.random()
  targetPos2 = targetPos2*((math.pi)/2.0 - (-(math.pi)/2.0)) + (-(math.pi)/2.0)
  
  pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetPos1, maxForce = 500)
  pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetPos2, maxForce = 500)
  
  t.sleep(1/70)
print(backLegSensorValues)
print(frontLegSensorValues)
with open('data/BackLegSensorValues.npy', 'wb') as f1:
  numpy.save(f1, backLegSensorValues)
with open('data/FrontLegSensorValues.npy', 'wb') as f2:
  numpy.save(f2, frontLegSensorValues)
with open('data/Position_Values.npy', 'wb') as f3:
  numpy.save(f3,  translated_pos_vals)
p.disconnect()

