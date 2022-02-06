import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/BackLegSensorValues.npy", allow_pickle=False, encoding="bytes")
#print(backLegSensorValues)
frontLegSensorValues = numpy.load("data/FrontLegSensorValues.npy", allow_pickle=False, encoding="bytes")
#print(frontLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=5)
matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", linewidth=2)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
