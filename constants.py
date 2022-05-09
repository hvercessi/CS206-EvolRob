
import numpy

numSensorNeurons = 3
numMotorNeurons = 10

motorJointRange = 0.7

initialNeuronValue = numpy.pi/4.0

leftLegAmplitude = -(numpy.pi)/2
leftLegFrequency = 4
leftLegPhaseOffset = 0

rightLegAmplitude = (numpy.pi)/2
rightLegFrequency = 4
rightLegPhaseOffset = (numpy.pi)/4

lowerLegAmp = numpy.pi

defaultAmp = numpy.pi/2
defaultFreq = 1
defaultOffset = 0


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

numberOfGenerations = 8
populationSize = 12