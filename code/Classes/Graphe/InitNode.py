#l'initialisation de la classe : 
def __init__(self,successors = nan) : 
   self.__successors = successors

@property 
def successors(self): 
    return self.__successors

@successors.setter 
def successors(self,successors): 
    self.__successors = successors

