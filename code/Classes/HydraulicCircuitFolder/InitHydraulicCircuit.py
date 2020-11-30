#l'initialisation de la classe : 
def __init__(self,name = ''Hydraulic circuit’',dipoles = None,poles = None,definedby = ''edges’') : 
   self.__name = name
   self.__dipoles = dipoles
   self.__poles = poles
   self.__definedby = definedby

@property 
def name(self): 
    return self.__name

@name.setter 
def name(self,name): 
    self.__name = name

@property 
def dipoles(self): 
    return self.__dipoles

@dipoles.setter 
def dipoles(self,dipoles): 
    self.__dipoles = dipoles

@property 
def poles(self): 
    return self.__poles

@poles.setter 
def poles(self,poles): 
    self.__poles = poles

@property 
def definedby(self): 
    return self.__definedby

@definedby.setter 
def definedby(self,definedby): 
    self.__definedby = definedby

