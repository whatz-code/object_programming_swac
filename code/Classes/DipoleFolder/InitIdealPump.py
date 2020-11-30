#l'initialisation de la classe : 
def __init__(self,flowRate = None) : 
   self.__flowRate = flowRate

@property 
def flowRate(self): 
    return self.__flowRate

@flowRate.setter 
def flowRate(self,flowRate): 
    self.__flowRate = flowRate

