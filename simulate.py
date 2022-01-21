# CS206 Evolutionary Robotics Assignment 1
# Halina Vercessi
# due 01/24/2022

# Use pybullet to simulate the world

import pybullet as p

physicsClient = p.connect(p.GUI)

for i in range(1000):
  p.stepSimulation()

p.disconnect()
