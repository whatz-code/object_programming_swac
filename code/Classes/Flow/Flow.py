import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid")
from Fluid.Fluid import Fluid

class Flow:
    def __init__(self,flowRate = None, pressureDifference = None, inputTemperature = None, averageTemperature = None, outletTemperature = None, fluid = Fluid(), temperatureDifference = None) : 
        
        if type(flowRate) is float or type(flowRate) is type(None):
            self.__flowRate = flowRate
        else :
            raise TypeError("the flow rate must be a float or a none type")

        if type(pressureDifference) is float or type(pressureDifference) is type(None):
            self.__pressureDifference = pressureDifference
        else :
            raise TypeError("the pressure difference must be a float or a none type")

        if type(inputTemperature) is float or type(inputTemperature) is type(None):
            self.__inputTemperature = inputTemperature
        else :
            raise TypeError("the input temperature must be a float or a none type")

        if type(averageTemperature) is float or type(averageTemperature) is type(None):
            self.__averageTemperature = averageTemperature
        else :
            raise TypeError("the average temperature must be a float or a none type")

        if type(outletTemperature) is float or type(outletTemperature) is type(None):
            self.__outletTemperature = outletTemperature
        else :
            raise TypeError("the outlet temperature must be a float or a none type")
        
        if type(temperatureDifference) is float or type(temperatureDifference) is type(None):
            self.__temperatureDifference = temperatureDifference
        else :
            raise TypeError("the temperature difference must be a float or a none type")





        eau = Fluid()
        if isinstance(fluid,Fluid):
            self.__fluid = fluid
        else :
            raise TypeError("the fluid must be a fluid object")

    @property 
    def flowRate(self): 
        return self.__flowRate

    @flowRate.setter 
    def flowRate(self,flowRate): 
        if type(flowRate) is float or type(flowRate) is type(None):
            self.__flowRate = flowRate
        else :
            raise TypeError("the flow rate must be a float or a none type")

    @property 
    def pressureDifference(self): 
        return self.__pressureDifference

    @pressureDifference.setter 
    def pressureDifference(self,pressureDifference): 
        if type(pressureDifference) is float or type(pressureDifference) is type(None):
            self.__pressureDifference = pressureDifference
        else :
            raise TypeError("the pressure difference must be a float or a none type")

    @property 
    def inputTemperature(self): 
        return self.__inputTemperature

    @inputTemperature.setter 
    def inputTemperature(self,inputTemperature): 
        if type(inputTemperature) is float or type(inputTemperature) is type(None):
            self.__inputTemperature = inputTemperature
        else :
            raise TypeError("the input temperature must be a float or a none type")

    @property 
    def averageTemperature(self): 
        return self.__averageTemperature

    @averageTemperature.setter 
    def averageTemperature(self,averageTemperature): 
        if type(averageTemperature) is float or type(averageTemperature) is type(None):
            self.__averageTemperature = averageTemperature
        else :
            raise TypeError("the average temperature must be a float or a none type")

    @property 
    def outletTemperature(self): 
        return self.__outletTemperature

    @outletTemperature.setter 
    def outletTemperature(self,outletTemperature): 
        if type(outletTemperature) is float or type(outletTemperature) is type(None):
            self.__outletTemperature = outletTemperature
        else :
            raise TypeError("the outlet temperature must be a float or a none type")

    @property 
    def temperatureDifference(self): 
        return self.__temperatureDifference

    @temperatureDifference.setter 
    def temperatureDifference(self,temperatureDifference): 
        if type(temperatureDifference) is float or type(temperatureDifference) is type(None):
            self.__temperatureDifference = temperatureDifference
        else :
            raise TypeError("the temperature difference must be a float or a none type")

    @property 
    def fluid(self): 
        return self.__fluid

    @fluid.setter 
    def fluid(self,fluid): 
        eau = Fluid()
        if isinstance(fluid,Fluid):
            self.__fluid = fluid
        else :
            raise TypeError("the fluid must be a fluid object")

    def averageVelocity(self, dipole, flowRate = None):
        return flowRate / dipole.crossSectionnalArea


    
    
