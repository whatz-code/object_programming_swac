#l'initialisation de la classe : 
def __init__(self,name = 'Dipole',hydraulicDiameter = None,crossSectionalArea = None,correlation = False) : 
   self.__name = name
   self.__hydraulicDiameter = hydraulicDiameter
   self.__crossSectionalArea = crossSectionalArea
   self.__correlation = correlation

@property 
def name(self): 
    return self.__name

@name.setter 
def name(self,name): 
    self.__name = name

@property 
def hydraulicDiameter(self): 
    return self.__hydraulicDiameter

@hydraulicDiameter.setter 
def hydraulicDiameter(self,hydraulicDiameter): 
    self.__hydraulicDiameter = hydraulicDiameter

@property 
def crossSectionalArea(self): 
    return self.__crossSectionalArea

@crossSectionalArea.setter 
def crossSectionalArea(self,crossSectionalArea): 
    self.__crossSectionalArea = crossSectionalArea

@property 
def correlation(self): 
    return self.__correlation

@correlation.setter 
def correlation(self,correlation): 
    self.__correlation = correlation

