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
#plt.plot(backLegSensorValues, label="Back Leg", linewidth=5)
#plt.plot(frontLegSensorValues, label="Front Leg", linewidth=2)
generationsA = np.array(generationsA)
fitValuesA = np.array(fitValuesA)
#scatter = plt.scatter(fitValues, generations, label="Fitness Values")
#plt.plot(positionValuesFront, label="Front Leg Target Angles", linewidth=1)
coeffsA = np.polyfit(generationsA, fitValuesA, 4)

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
#plt.plot(backLegSensorValues, label="Back Leg", linewidth=5)
#plt.plot(frontLegSensorValues, label="Front Leg", linewidth=2)
generationsB = np.array(generationsB)
fitValuesB = np.array(fitValuesB)
#scatter = plt.scatter(fitValues, generations, label="Fitness Values")
#plt.plot(positionValuesFront, label="Front Leg Target Angles", linewidth=1)
coeffsB = np.polyfit(generationsB, fitValuesB, 4)

polyB = np.poly1d(coeffsB)
new_xB = np.linspace(np.amin(generationsB), np.amax(generationsB))
new_yB = polyB(new_xB)

polyA = np.poly1d(coeffsA)
new_xA = np.linspace(np.amin(generationsA), np.amax(generationsA))
new_yA = polyA(new_xA)


fig, ax = plt.subplots()

scatterA, = ax.plot(generationsA, fitValuesA, 'o', label = "A")
lineA, = ax.plot(new_xA, new_xB, label = "Fit Line A") #ax.plot(generationsA, mA*generationsA + bA, label = "Fit Line A")

scatterB, = ax.plot(generationsB, fitValuesB, 'x', label = "B")
lineB, = ax.plot(new_xB, new_yB, label = "Fit Line B")  #ax.plot(generationsB, mB*generationsB + bB, label = "Fit Line B")

first_legend = ax.legend(handles=[lineA], loc='upper right')
sec_legend = ax.legend(handles=[lineB], loc='upper left')
third_legend = ax.legend([(scatterA, scatterB)])

ax.legend([scatterA, scatterB, lineA, lineB], ["A (no arms)", "B (arms)", "Fit Line A", "Fit Line B"])

plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Fitness after 20 Generations")
plt.show()