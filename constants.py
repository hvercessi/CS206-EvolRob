
import numpy

numSensorNeurons = 9
numMotorNeurons = 8

initialNeuronValue = numpy.pi/4.0

backLegAmplitude = (numpy.pi/4.0)
backLegFrequency = 10
backLegPhaseOffset = 0

frontLegAmplitude = -(numpy.pi/4.0)
frontLegFrequency = 10
frontLegPhaseOffset = (numpy.pi/4.0)


simRange = 800
sleepTime = 0.01

xValsMin = 0
xValsMax = 2*(numpy.pi)

# Size values
length = 1.0
width = 1.0
height = 1.0

# Position Values
x_body = 0.0
y_body = 0.0
z_body = 0.5

x_world = -3.0
y_world = 3.0
z_world = 0.5

numberOfGenerations = 10
populationSize = 10