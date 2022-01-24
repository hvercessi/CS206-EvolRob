# CS206 Evolutionary Robotics Assignment 1
# Halina Vercessi

# Use pybullet to simulate the world

import pybullet as p
import time as t

physicsClient = p.connect(p.GUI)
p.setGravity(0,0,-9.8)

p.loadSDF("box.sdf")
for i in range(1000):
  p.stepSimulation()
  t.sleep(1/100)
  print(i)

p.disconnect()
