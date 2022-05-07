import numpy
import matplotlib.pyplot
import os
import constants as c
from matplotlib.colors import ListedColormap

# backLegSensorValues = numpy.load("data/BackLegSensorValues.npy", allow_pickle=False, encoding="bytes")

# frontLegSensorValues = numpy.load("data/FrontLegSensorValues.npy", allow_pickle=False, encoding="bytes")

#positionValuesFront = numpy.load("data/Position_Values_Front.npy", allow_pickle=False, encoding="bytes")
i = 0

fitValues = []
#zValues = []
generations = []  
#colors = ListedColormap(['red', 'blue', 'purple','green', 'yellow', 'orange', 'pink']) 
with open("data/RobotFitness.txt", 'r') as f:
    line = f.readline()
    while line != "":
        
        fitnessValue = line.rstrip().split("|")
        #print(fitnessValue)
        generations.append(int(fitnessValue[0]))
        fitValues.append(float(fitnessValue[1]))
        
        line = f.readline()
#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=5)
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", linewidth=2)

#scatter = matplotlib.pyplot.scatter(fitValues, generations, label="Fitness Values")
#matplotlib.pyplot.plot(positionValuesFront, label="Front Leg Target Angles", linewidth=1)

matplotlib.pyplot.plot(generations, fitValues, label="Fitness Values")
matplotlib.pyplot.show()

