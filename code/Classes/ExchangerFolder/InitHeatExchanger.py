#l'initialisation de la classe : 
def __init__(self,materialConductivity = 21.9,exchangeSurface = 600,HydraulicDipole1 = 'class dipole',HydraulicDipole2 = 'class dipole') : 
   self.__materialConductivity = materialConductivity
   self.__exchangeSurface = exchangeSurface
   self.__HydraulicDipole1 = HydraulicDipole1
   self.__HydraulicDipole2 = HydraulicDipole2

@property 
def materialConductivity(self): 
    return self.__materialConductivity

@materialConductivity.setter 
def materialConductivity(self,materialConductivity): 
    self.__materialConductivity = materialConductivity

@property 
def exchangeSurface(self): 
    return self.__exchangeSurface

@exchangeSurface.setter 
def exchangeSurface(self,exchangeSurface): 
    self.__exchangeSurface = exchangeSurface

@property 
def HydraulicDipole1(self): 
    return self.__HydraulicDipole1

@HydraulicDipole1.setter 
def HydraulicDipole1(self,HydraulicDipole1): 
    self.__HydraulicDipole1 = HydraulicDipole1

@property 
def HydraulicDipole2(self): 
    return self.__HydraulicDipole2

@HydraulicDipole2.setter 
def HydraulicDipole2(self,HydraulicDipole2): 
    self.__HydraulicDipole2 = HydraulicDipole2

