
import numpy

numSensorNeurons = 3
numMotorNeurons = 15

motorJointRange = 1.0

initialNeuronValue = numpy.pi/4.0

leftLegAmplitude = -(numpy.pi)/2
leftLegFrequency = 1
leftLegPhaseOffset = 0

rightLegAmplitude = (numpy.pi)/2
rightLegFrequency = 1
rightLegPhaseOffset = 0

lowerLegAmp = numpy.pi

defaultAmp = numpy.pi/2
defaultFreq = 1
defaultOffset = 0


simRange = 900
sleepTime = 1/90

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