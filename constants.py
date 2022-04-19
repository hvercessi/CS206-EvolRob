
import numpy

numSensorNeurons = 5
numMotorNeurons = 6

motorJointRange = 2.0

initialNeuronValue = numpy.pi/4.0

backLegAmplitude = (numpy.pi/4.0)
backLegFrequency = 10
backLegPhaseOffset = 0

frontLegAmplitude = -(numpy.pi/4.0)
frontLegFrequency = 10
frontLegPhaseOffset = (numpy.pi/4.0)


simRange = 1000
sleepTime = 1/100

xValsMin = 0
xValsMax = 2*(numpy.pi)

# Size values
length = 0.5
width = 1.0
height = 0.5

# Position Values
x_body = 0.0
y_body = 0.0
z_body = 0.5

x_world = -3.0
y_world = 3.0
z_world = 0.5

numberOfGenerations = 10
populationSize = 10