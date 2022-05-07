# CS206 Evolutionary Robotics Assignment 1
# Halina Vercessi

# Use pybullet to simulate the world


from simulation import SIMULATION
import pybullet as p
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
gen = sys.argv[3]

simulation = SIMULATION(directOrGUI, solutionID, gen)
simulation.Run()
simulation.Get_Fitness()

