# CS206 Evolutionary Robotics Assignment 1
# Halina Vercessi

# Use pybullet to simulate the world


from simulation import SIMULATION
import pybullet as p
simulation = SIMULATION()
simulation.Run()
simulation.Get_Fitness()
#simulation.__del__