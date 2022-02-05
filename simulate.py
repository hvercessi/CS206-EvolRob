# CS206 Evolutionary Robotics Assignment 1
# Halina Vercessi

# Use pybullet to simulate the world

import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
p.loadSDF("world.sdf")

for i in range(1000):
  p.stepSimulation()
  backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  t.sleep(1/70)
  #print(i)
  print(backLegTouch)

p.disconnect()
print(backLegSensorValues)
