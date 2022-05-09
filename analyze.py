import numpy
import matplotlib.pyplot
import os
import constants as c
from matplotlib.colors import ListedColormap
import numpy as np

# backLegSensorValues = numpy.load("data/BackLegSensorValues.npy", allow_pickle=False, encoding="bytes")

# frontLegSensorValues = numpy.load("data/FrontLegSensorValues.npy", allow_pickle=False, encoding="bytes")

#positionValuesFront = numpy.load("data/Position_Values_Front.npy", allow_pickle=False, encoding="bytes")
i = 0

fitValuesA = []
#zValues = []
generationsA = []  
#colors = ListedColormap(['red', 'blue', 'purple','green', 'yellow', 'orange', 'pink']) 
with open("SolutionFitnessA.txt", 'r') as f:
    line = f.readline()
    while line != "":
        
        fitnessValueA = line.rstrip().split("|")
        #print(fitnessValue)
        generationsA.append(int(fitnessValueA[0]))
        fitValuesA.append(float(fitnessValueA[1]))
        
        line = f.readline()
#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=5)
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", linewidth=2)
generationsA = np.array(generationsA)
fitValuesA = np.array(fitValuesA)
#scatter = matplotlib.pyplot.scatter(fitValues, generations, label="Fitness Values")
#matplotlib.pyplot.plot(positionValuesFront, label="Front Leg Target Angles", linewidth=1)
mA, bA = np.polyfit(generationsA, fitValuesA, 1)

fitValuesB = []
#zValues = []
generationsB = []  
#colors = ListedColormap(['red', 'blue', 'purple','green', 'yellow', 'orange', 'pink']) 
with open("SolutionFitnessB.txt", 'r') as f:
    line = f.readline()
    while line != "":
        
        fitnessValueB = line.rstrip().split("|")
        #print(fitnessValue)
        generationsB.append(int(fitnessValueB[0]))
        fitValuesB.append(float(fitnessValueB[1]))
        
        line = f.readline()
#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=5)
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", linewidth=2)
generationsB = np.array(generationsB)
fitValuesB = np.array(fitValuesB)
#scatter = matplotlib.pyplot.scatter(fitValues, generations, label="Fitness Values")
#matplotlib.pyplot.plot(positionValuesFront, label="Front Leg Target Angles", linewidth=1)
mB, bB = np.polyfit(generationsB, fitValuesB, 1)

matplotlib.pyplot.plot(generationsA, fitValuesA, 'o')
matplotlib.pyplot.plot(generationsA, mA*generationsA + bA)
matplotlib.pyplot.plot(generationsB, fitValuesB, 'x')
matplotlib.pyplot.plot(generationsB, mB*generationsB + bB)
matplotlib.pyplot.xlabel("Generation")
matplotlib.pyplot.ylabel("Fitness")
matplotlib.pyplot.title("Fitness after 15 Generations")
matplotlib.pyplot.show()

