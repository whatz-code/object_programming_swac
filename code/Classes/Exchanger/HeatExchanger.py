import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole") 
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid")
from Dipole import PlateHeatExchangerSide
from math import pi
from HydraulicThermicCalculus import HydraulicThermicCalculus
from Fluid import Fluid
from math import exp
class HeatExchanger:
    def __init__(self,materialConductivity = 21.9,exchangeSurface = 600,hydraulicDipole1 = 'class dipole',hydraulicDipole2 = 'class dipole', globalThermicCoefficient = 5000) : 
        self.__materialConductivity = materialConductivity
        self.__exchangeSurface = exchangeSurface
        self.__hydraulicDipole1 = hydraulicDipole1
        self.__hydraulicDipole2 = hydraulicDipole2
        self.__globalThermicCoefficient = globalThermicCoefficient

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
    def hydraulicDipole1(self): 
        return self.__hydraulicDipole1

    @hydraulicDipole1.setter 
    def hydraulicDipole1(self,hydraulicDipole1): 
        self.__hydraulicDipole1 = hydraulicDipole1

    @property 
    def hydraulicDipole2(self): 
        return self.__hydraulicDipole2

    @hydraulicDipole2.setter 
    def hydraulicDipole2(self,hydraulicDipole2): 
        self.__hydraulicDipole2 = hydraulicDipole2

    @property 
    def globalThermicCoefficient(self): 
        return self.__globalThermicCoefficient

    @globalThermicCoefficient.setter 
    def globalThermicCoefficient(self,hydraulicDipole2): 
        self.__globalThermicCoefficient = globalThermicCoefficient

    def NUT(self, globalThermicCoefficient = None, exchangeSurface = None, flow1 = None, flow2 = None):
        if globalThermicCoefficient == None:
            globalThermicCoefficient = self.globalThermicCoefficient
        if exchangeSurface == None:
            exchangeSurface = self.exchangeSurface
        if flow1 = None:
            flow1 = self.hydraulicDipole1.flow
        if flow2 = None:
            flow2 = self.hydraulicDipole2.flow

        hydraulicCapacity1 = flow1.flowRate * flow1.fluid.thermicCapacity * flow1.fluid.volumetricMass
        hydraulicCapacity2 = flow2.flowRate * flow2.fluid.thermicCapacity * flow2.fluid.volumetricMass

        hydraulicCapacity = min(hydraulicCapacity1, hydraulicCapacity2)

        return globalThermicCoefficient * exchangeSurface / hydraulicCapacity
    
    def outletTemperatureCalcul(self, flow1 = None, flow2 = None, estimationOutletTemperature1 = None, estimationOutletTemperature2 = None):
        if flow1 == None:
            flow1 = self.hydraulicDipole1.flow
        if flow2 == None:
            flow2 = self.hydraulicDipole2.flow
        if estimationOutletTemperature1 == None:
            estimationOutletTemperature1 = flow1.outletTemperature
        if estimationOutletTemperature2 == None:
            estimationOutletTemperature2 = flow2.outletTemperature

        outletTemperature10 = estimationOutletTemperature1
        outletTemperature20 = estimationOutletTemperature2
        outletTemperature1N = outletTemperature10
        outletTemperature2N = outletTemperature20
        
        caracteristicLength1 = self.hydraulicDipole1.hydraulicDiameter
        caracteristicLength2 = self.hydraulicDipole2.hydraulicDiameter
        caracteristicVelocity1 = flow1.flowRate / self.hydraulicDipole1.crossSectionArea
        caracteristicVelocity2 = flow2.flowRate / self.hydraulicDipole2.crossSectionArea
        volumetricMass1 = flow1.fluid.volumetricMass1
        volumetricMass2 = flow2.fluid.volumetricMass2
        dynamicViscosity1 = flow1.fluid.dynamicViscosity
        dynamicViscosity2 = flow2.fluid.dynamicViscosity
        thermicCapacity1 = flow1.fluid.thermicCapacity
        thermicCapacity2 = flow2.fluid.thermicCapacity
        thermicConductivity1 = flow1.fluid.thermicConductivity
        thermicConductivity2 = flow2.fluid.thermicConductivity


        def g(T): #T = [T1s, T2s]
            reynoldsNumber1 = HydraulicThermicCalculus.reynolds(caracteristicLength1,caracteristicLength2,volumetricMass1, dynamicViscosity1)
            reynoldsNumber2 = HydraulicThermicCalculus.reynolds(caracteristicLength2,caracteristicVelocity2,volumetricMass2,dynamicViscosity2, reynoldsNumber2)
            prandtlNumber1 = HydraulicThermicCalculus.prandtl(dynamicViscosity1,thermicCapacity1, thermicConductivity1)
            prandtlNumber2 = HydraulicThermicCalculus.prandtl(dynamicViscosity2,thermicCapacity2,thermicConductivity2)
            K = self.globalThermicCoefficient(reynoldsNumber1, prandtlNumber1, reynoldsNumber2, prandtlNumber2, fluid1, fluid2)
            
        efficacity = self.efficacity()
        puissanceThermic = efficacity * 


class PlateExchanger(HeatExchanger):
    def __init__(self, materialConductivity = 21.9,exchangeSurface = 600,hydraulicDipole1 = None,hydraulicDipole2 = None, length = 2.5,width = 1.0,plateNumber = 385.0,passeNumber = 1.0,plateThickness = 0.5,plateGap = 3.0,angle = 45.0,streakWaveLength = None, globalThermicCoefficient = 5000) : 
        # Calcul du diamètre hydraulique :
        x = 2 * pi * plateGap / streakWaveLength
        phi = 1 / 6 * (1 + (1 + x ** 2) ** (1/2) + 4 * (1 + x ** 2/2) ** (1/2))
        hydraulicDiameter = 4 * plateGap / phi

        # Calcul de la surface transversale pour des deux côtés de l'échangeur :
        crossSectionArea = (plateNumber - 1) * plateGap / 2 

        # Création des instances de classes dipole :

        hydraulicDipole1 = PlateHeatExchangerSide('Plate Heat exchanger side 1', hydraulicDiameter, crossSectionArea, angle, length, passeNumber)
        hydraulicDipole2 = PlateHeatExchangerSide('Plate Heat exchanger side 2', hydraulicDiameter, crossSectionArea, angle, length, passeNumber)

        # Initialisation : 
        HeatExchanger.__init__(self, materialConductivity, exchangeSurface, hydraulicDipole1, hydraulicDipole2, globalThermicCoefficient)
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
        self.hydraulicDipole1.length(length)
        self.hydraulicDipole2.length(length)

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
        self.hydraulicDipole1.passeNumber(passeNumber)
        self.hydraulicDipole2.passeNumber(passeNumber)
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
        self.hydraulicDipole1.angle(angle)
        self.hydraulicDipole2.angle(angle)

    @property 
    def streakWaveLength(self): 
        return self.__streakWaveLength

    @streakWaveLength.setter 
    def streakWaveLength(self,streakWaveLength): 
        self.__streakWaveLength = streakWaveLength
    
    def thermicTransfertCoefficient(self, reynoldsNumber1, prandtlNumber1, reynoldsNumber2, prandtlNumber2, fluid1, fluid2, hydraulicDipole1 = None, hydraulicDipole2 = None, materialConductivity = None, plateThickness = None, parameterA = 3.8, parameterB = 0.045, parameterC = 0.09):
        # determination du Nusselt du premier cotes
        if hydraulicDipole1 == None :
            hydraulicDipole1 = self.hydraulicDipole1
        nusseltNumber1 = hydraulicDipole1.thermicCorrelation(reynoldsNumber1, prandtlNumber1, parameterA = parameterA, parameterB = parameterB, parameterC = parameterC)
        thermicConvectiveCoefficient1 = HydraulicThermicCalculus.nusselt(hydraulicDipole1.hydraulicDiameter, fluid1.thermicConductivity, nusseltNumber1)

        # determination du Nusselt du deuxieme cotes
        if hydraulicDipole2 == None :
            hydraulicDipole2 = self.hydraulicDipole2
        nusseltNumber2 = hydraulicDipole2.thermicCorrelation(reynoldsNumber2, prandtlNumber2, parameterA = parameterA, parameterB = parameterB, parameterC = parameterC)
        thermicConvectiveCoefficient2 = HydraulicThermicCalculus.nusselt(hydraulicDipole2.hydraulicDiameter, fluid2.thermicConductivity, nusseltNumber2)
        
        if materialConductivity == None :
            materialConductivity = self.materialConductivity
        if plateThickness == None :
            plateThickness = self.plateThickness * 10 ** (-3)

        return 1 / (1 / thermicConvectiveCoefficient1 + 1 / thermicConvectiveCoefficient2 + plateThickness/materialConductivity)
    
    def efficacity(self, NUT = None, rapport = None):
        if NUT == None:
            NUT = self.NUT()
        if rapport = None:
            flow1 = self.hydraulicDipole1.flow
            flow2 = self.hydraulicDipole2.flow
            hydraulicCapacity1 = flow1.flowRate * flow1.fluid.thermicCapacity * flow1.fluid.volumetricMass
            hydraulicCapacity2 = flow2.flowRate * flow2.fluid.thermicCapacity * flow2.fluid.volumetricMass 
            rapport = min(hydraulicCapacity1 / hydraulicCapacity2, hydraulicCapacity2 / hydraulicCapacity1)
        if rapport != 1.0:
            efficacity = (1 - exp(- NUT * (1 - rapport))) / (1 - rapport * (- NUT * (1 - rapport))) 
        else :
            efficacity = NUT / (1 + NUT)
        return efficacity



#Debug
heatExchanger1 = PlateExchanger(22,700,None,None,2.8,2,388,2,0.8,4,56,1.5)
heatExchanger2 = PlateExchanger(streakWaveLength=2)