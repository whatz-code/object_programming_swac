import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole") 
from Dipole import PlateHeatExchangerSide
from math import pi

class HeatExchanger :
    def __init__(self,materialConductivity = 21.9,exchangeSurface = 600,hydraulicDipole1 = 'class dipole',hydraulicDipole2 = 'class dipole') : 
        self.__materialConductivity = materialConductivity
        self.__exchangeSurface = exchangeSurface
        self.__HydraulicDipole1 = hydraulicDipole1
        self.__HydraulicDipole2 = hydraulicDipole2

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

class PlateExchanger(HeatExchanger):
    def __init__(self, materialConductivity = 21.9,exchangeSurface = 600,hydraulicDipole1 = 'class dipole',hydraulicDipole2 = 'class dipole', length = 2.5,width = 1.0,plateNumber = 385.0,passeNumber = 1.0,plateThickness = 0.5,plateGap = 3.0,angle = 45.0,streakWaveLength = None) : 
        # Calcul du diamètre hydraulique :
        x = 2 * pi * plateGap / streakWaveLength
        phi = 1 / 6 * (1 + (1 + x ** 2) ** (1/2) + 4 * (1 + x ** 2/2) ** (1/2))
        hydraulicDiameter = 4 * plateGap / phi

        # Calcul de la surface transversale pour des deux côtés de l'échangeur :
        crossSectionArea = (plateNumber - 1) * plateGap / 2 

        # Création des instances de classes dipole :

        hydraulicDipole1 = PlateExchangerSide('Plate Heat exchanger side 1', hydraulicDiameter, crossSectionArea, angle, length, passeNumber)
        hydraulicDipole2 = PlateExchangerSide('Plate Heat exchanger side 2', hydraulicDiameter, crossSectionArea, angle, length, passeNumber)

        # Initialisation : 
        
        HeatExchanger.__init__(materialConductivity, exchangeSurface, hydraulicDipole1, hydraulicDipole2)
        self.__length = length
        self.__width = width
        self.__plateNumber = plateNumber
        self.__passeNumber = passeNumber
        self.__plateThickness = plateThickness
        self.__plateGap = plateGap
        self.__angle = angle
        self.__streakWaveLength = streakWaveLength

    @property 
    def length(self): 
        return self.__length

    @length.setter 
    def length(self,length): 
        self.__length = length

    @property 
    def width(self): 
        return self.__width

    @width.setter 
    def width(self,width): 
        self.__width = width

    @property 
    def plateNumber(self): 
        return self.__plateNumber

    @plateNumber.setter 
    def plateNumber(self,plateNumber): 
        self.__plateNumber = plateNumber

    @property 
    def passeNumber(self): 
        return self.__passeNumber

    @passeNumber.setter 
    def passeNumber(self,passeNumber): 
        self.__passeNumber = passeNumber

    @property 
    def plateThickness(self): 
        return self.__plateThickness

    @plateThickness.setter 
    def plateThickness(self,plateThickness): 
        self.__plateThickness = plateThickness

    @property 
    def plateGap(self): 
        return self.__plateGap

    @plateGap.setter 
    def plateGap(self,plateGap): 
        self.__plateGap = plateGap

    @property 
    def angle(self): 
        return self.__angle

    @angle.setter 
    def angle(self,angle): 
        self.__angle = angle

    @property 
    def streakWaveLength(self): 
        return self.__streakWaveLength

    @streakWaveLength.setter 
    def streakWaveLength(self,streakWaveLength): 
        self.__streakWaveLength = streakWaveLength