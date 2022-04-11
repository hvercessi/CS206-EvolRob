
import numpy

numSensorNeurons = 5
numMotorNeurons = 6

motorJointRange = 1.0 #0.2

initialNeuronValue = numpy.pi/4.0

backLegAmplitude = (numpy.pi/4.0)
backLegFrequency = 10
backLegPhaseOffset = 0

frontLegAmplitude = -(numpy.pi/4.0)
frontLegFrequency = 10
frontLegPhaseOffset = (numpy.pi/4.0)


simRange = 900
sleepTime = 0.01

xValsMin = 0
xValsMax = 2*(numpy.pi)

# Size values
length = 0.55
width = 0.85
height = 0.55

# Position Values
x_body = 0.0
y_body = 0.0
z_body = 0.5

x_world = -3.0
y_world = 3.0
z_world = 0.5

numberOfGenerations = 8
populationSize = 8