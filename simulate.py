# CS206 Evolutionary Robotics Assignment 1
# Halina Vercessi

# Use pybullet to simulate the world


from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)

# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)

# backLegSensorValues = numpy.zeros(c.simRange)
# frontLegSensorValues = numpy.zeros(c.simRange)

# targetAnglesBackLeg = c.backLegAmplitude*numpy.sin(c.backLegFrequency*numpy.linspace(c.xValsMin, c.xValsMax, c.simRange) + c.backLegPhaseOffset)
# targetAnglesFrontLeg = c.frontLegAmplitude*numpy.sin(c.frontLegFrequency*numpy.linspace(c.xValsMin, c.xValsMax, c.simRange) + c.frontLegPhaseOffset)

# with open('data/Position_Values_Back.npy', 'wb') as f3:
#   numpy.save(f3, targetAnglesBackLeg)
# with open('data/Position_Values_Front.npy', 'wb') as f4:
#   numpy.save(f4, targetAnglesFrontLeg)
# #exit()


# for i in range(c.simRange):
#   p.stepSimulation()
#   backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#   frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

#   pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBackLeg[i], maxForce = 500)
#   pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFrontLeg[i], maxForce = 500)
  
#   t.sleep(c.sleepTime)
# print(backLegSensorValues)
# print(frontLegSensorValues)
# with open('data/BackLegSensorValues.npy', 'wb') as f1:
#   numpy.save(f1, backLegSensorValues)
# with open('data/FrontLegSensorValues.npy', 'wb') as f2:
#   numpy.save(f2, frontLegSensorValues)
# p.disconnect()

