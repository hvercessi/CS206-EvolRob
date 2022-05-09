import numpy
import matplotlib.pyplot as plt
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

generationsB = np.array(generationsB)
fitValuesB = np.array(fitValuesB)

generationsA = np.array(generationsA)
fitValuesA = np.array(fitValuesA)

# mA, bA = np.polyfit(generationsA, fitValuesA, 1)

# mB, bB = np.polyfit(generationsB, fitValuesB, 1)

fig, ax = plt.subplots()

# scatterA, = ax.plot(generationsA, fitValuesA, 'o', label = "A")
# lineA, = ax.plot(generationsA, mA*generationsA + bA, label = "Fit Line A")

# scatterB, = ax.plot(generationsB, fitValuesB, 'x', label = "B")
# lineB, = ax.plot(generationsB, mB*generationsB + bB, label = "Fit Line B")

# first_legend = ax.legend(handles=[lineA], loc='upper right')
# sec_legend = ax.legend(handles=[lineB], loc='upper left')
# third_legend = ax.legend([(scatterA, scatterB)])

# ax.legend([scatterA, scatterB, lineA, lineB], ["A", "B", "Fit Line A", "Fit Line B"])
data = [fitValuesA, fitValuesB]
ax.boxplot(data)

ax.set_xticklabels(["A", "B"])
plt.xlabel("Test Group")
plt.ylabel("Fitness")
plt.title("Fitness after 15 Generations")
plt.show()

