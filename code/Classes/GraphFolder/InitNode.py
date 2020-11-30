#l'initialisation de la classe : 
def __init__(self,name = None,successors = None) : 
   self.__name = name
   self.__successors = successors

@property 
def name(self): 
    return self.__name

@name.setter 
def name(self,name): 
    self.__name = name

@property 
def successors(self): 
    return self.__successors

@successors.setter 
def successors(self,successors): 
    self.__successors = successors

