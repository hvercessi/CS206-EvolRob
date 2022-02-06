import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy", allow_pickle=False, encoding="bytes")
print(backLegSensorValues)
