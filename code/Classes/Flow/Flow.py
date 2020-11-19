#l'initialisation de la classe : 
def __init__(self,flowRate = None,pressure = None,temperature = None) : 
   self.__flowRate = flowRate
   self.__pressure = pressure
   self.__temperature = temperature

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

