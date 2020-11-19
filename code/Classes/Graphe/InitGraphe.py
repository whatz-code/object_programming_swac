#l'initialisation de la classe : 
def __init__(self,nodes = None) : 
   self.__nodes = nodes

@property 
def nodes(self): 
    return self.__nodes

@nodes.setter 
def nodes(self,nodes): 
    self.__nodes = nodes

