import numpy
import matplotlib.pyplot

# backLegSensorValues = numpy.load("data/BackLegSensorValues.npy", allow_pickle=False, encoding="bytes")

# frontLegSensorValues = numpy.load("data/FrontLegSensorValues.npy", allow_pickle=False, encoding="bytes")

positionValues = numpy.load("data/Position_Values.npy", allow_pickle=False, encoding="bytes")

#matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=5)
#matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg", linewidth=2)

matplotlib.pyplot.plot(positionValues, label="Back Leg Target Angles", linewidth=5)
matplotlib.pyplot.plot(positionValues, label="Front Leg Target Angles", linewidth=1)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
