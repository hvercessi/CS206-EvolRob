import numpy
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, name):
        self.linkName = name
        self.values = []
        
    
    def Get_Value(self, i):
        #self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
       
        self.values.append(pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName))
        if i == c.simRange-1:
            print(self.values)
        