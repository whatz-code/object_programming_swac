#l'initialisation de la classe : 
class Flow:
    def __init__(self,flowRate = None,pressure = None,temperature = None, fluid = None) : 
        self.__flowRate = flowRate
        self.__pressure = pressure
        self.__temperature = temperature
        self.__fluid = fluid

    @property 
    def flowRate(self): 
        return self.__flowRate

    @flowRate.setter 
    def flowRate(self,flowRate): 
        self.__flowRate = flowRate

    @property 
    def pressure(self): 
        return self.__pressure

    @pressure.setter 
    def pressure(self,pressure): 
        self.__pressure = pressure

    @property 
    def temperature(self): 
        return self.__temperature

    @temperature.setter 
    def temperature(self,temperature): 
        self.__temperature = temperature

    @property 
    def fluid(self): 
        return self.__fluid

    @fluid.setter 
    def fluid(self,fluid): 
        self.__fluid = fluid

    def averageVelocity(self, dipole, flowRate = None):
        return flowRate / dipole.crossSectionnalArea
    
