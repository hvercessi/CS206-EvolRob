import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/BackLegSensorValues.npy", allow_pickle=False, encoding="bytes")
#print(backLegSensorValues)
frontLegSensorValues = numpy.load("data/FrontLegSensorValues.npy", allow_pickle=False, encoding="bytes")
#print(frontLegSensorValues)
positionValues = numpy.load("data/Position_Values.npy", allow_pickle=False, encoding="bytes")

#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=5)
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", linewidth=2)

matplotlib.pyplot.plot(numpy.linspace(0, 2*(numpy.pi), 1000), positionValues, label="Position Values")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
