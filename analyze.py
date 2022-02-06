import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy", allow_pickle=False, encoding="bytes")
#print(backLegSensorValues)
frontLegSensorValues = numpy.load("data/FrontLegSensorValues.npy", allow_pickle=False, encoding="bytes")
#print(frontLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()

matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.show()
