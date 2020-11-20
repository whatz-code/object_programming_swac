#l'initialisation de la classe : 
class Flow:
    def __init__(self,flowRate = None, pressureDifference = None, inputTemperature = None, averageTemperature = None, outletTemperature = None, fixedVariables = []) : 
        self.__flowRate = flowRate
        self.__pressureDifference = pressureDifference
        self.__inputTemperature = inputTemperature
        self.__averageTemperature = averageTemperature
        self.__outletTemperature = outletTemperature
        self.__fluid = fluid
        self.__fixedVaribales = fixedVariables
    @property 
    def flowRate(self): 
        return self.__flowRate

    @flowRate.setter 
    def flowRate(self,flowRate): 
        self.__flowRate = flowRate

    @property 
    def pressureDifference(self): 
        return self.__pressureDifference

    @pressureDifference.setter 
    def pressureDifference(self,pressureDifference): 
        self.__pressureDifference = pressureDifference
    
    @property 
    def inputTemperature(self): 
        return self.__inputTemperature

    @inputTemperature.setter 
    def inputTemperature(self,inputTemperature): 
        self.__inputTemperature = inputTemperature

    @property 
    def averageTemperature(self): 
        return self.__averageTemperature

    @averageTemperature.setter 
    def averageTemperature(self,averageTemperature): 
        self.__averageTemperature = averageTemperature

    @property 
    def outletTemperature(self): 
        return self.__outletTemperature

    @outletTemperature.setter 
    def outletTemperature(self,outletTemperature): 
        self.__outletTemperature = outletTemperature

    @property 
    def fluid(self): 
        return self.__fluid

    @fluid.setter 
    def fluid(self,fluid): 
        self.__fluid = fluid
    
    @property 
    def fixedVariables(self): 
        return self.__fixedVariables

    @fixedVariables.setter 
    def fixedVariables(self,fixedVariables): 
        self.__fixedVariables = fixedVariables
    
    def addFixedVariable(self, fixedVariable):
        self.__fixedVariables.append(fixedVariable)

    def averageVelocity(self, dipole, flowRate = None):
        return flowRate / dipole.crossSectionnalArea


    
    
