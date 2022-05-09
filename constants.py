
import numpy

numSensorNeurons = 3
numMotorNeurons = 6

motorJointRange = 0.3

initialNeuronValue = numpy.pi/4.0

leftLegAmplitude = -(numpy.pi)/4
leftLegFrequency = 6
leftLegPhaseOffset = 0

rightLegAmplitude = (numpy.pi)/4
rightLegFrequency = 6
rightLegPhaseOffset = (numpy.pi)

lowerLegAmp = numpy.pi

defaultAmp = numpy.pi/4
defaultFreq = 6
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

numberOfGenerations = 25
populationSize = 10