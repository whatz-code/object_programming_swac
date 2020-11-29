import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole") 
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid")
from Dipole import PlateHeatExchangerSide
from Dipole import Dipole
from math import pi
from HydraulicThermicCalculus import HydraulicThermicCalculus
from Fluid import Fluid
from math import exp
from math import log
from Dipole import Pole
from Calculus import Resolve
from Flow import Flow
class HeatExchanger:
    def __init__(self,materialConductivity = 21.9,exchangeSurface = 600,hydraulicDipole1 = None,hydraulicDipole2 = None, globalThermicCoefficient = 5000, downstreamPole1 = Pole('downstreamPole1'), upstreamPole1 = Pole('upstreamPole1'), downstreamPole2 = Pole('downstreamPole2'), upstreamPole2 = Pole('upstreamPole2')) : 

        if hydraulicDipole1 == None:
            hydraulicDipole1 = Dipole('hydraulc dipole 1', upstreamPole=upstreamPole1,downstreamPole=downstreamPole1)
        if hydraulicDipole2 == None: 
            hydraulicDipole2 = Dipole('hydraulic dipole 2', upstreamPole = upstreamPole2, downstreamPole=downstreamPole2)
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
        if flow1 == None:
            flow1 = self.hydraulicDipole1.flow
        if flow2 == None:
            flow2 = self.hydraulicDipole2.flow

        hydraulicCapacity1 = flow1.flowRate * flow1.fluid.thermicCapacity * flow1.fluid.volumetricMass
        hydraulicCapacity2 = flow2.flowRate * flow2.fluid.thermicCapacity * flow2.fluid.volumetricMass

        hydraulicCapacity = min(hydraulicCapacity1, hydraulicCapacity2)

        return globalThermicCoefficient * exchangeSurface / hydraulicCapacity
    
    def DTLM(self, outletColdTemperature, outletWarmTemperature, entryColdTemperature = None, entryWarmTemperature = None):
        if entryColdTemperature == None or entryWarmTemperature == None:
            temperatureEntry1 = self.hydraulicDipole1.flow.entryTemperature 
            temperatureEntry2 = self.hydraulicDipole2.flow.entryTemperature

            if temperatureEntry1 >= temperatureEntry2:
                entryColdTemperature = temperatureEntry2
                entryWarmTemperature = temperatureEntry1
            else :
                entryColdTemperature = temperatureEntry1
                entryWarmTemperature = temperatureEntry2
        
        temperatureDifference1 = entryWarmTemperature - outletColdTemperature
        temperatureDifference2 = outletWarmTemperature - entryColdTemperature

        DTLM = (temperatureDifference1 - temperatureDifference2) / log(temperatureDifference1 / temperatureDifference2)
        return DTLM

    
    def outletTemperatureCalcul(self, flow1 = None, flow2 = None, estimationOutletTemperature1 = None, estimationOutletTemperature2 = None, averagePressure1 = None, averagePressure2 = None):
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

        #On considère  ici que les caractéristiques des fluides sont constantes 
        caracteristicLength1 = self.hydraulicDipole1.hydraulicDiameter
        caracteristicLength2 = self.hydraulicDipole2.hydraulicDiameter
        caracteristicVelocity1 = flow1.flowRate / self.hydraulicDipole1.crossSectionalArea
        caracteristicVelocity2 = flow2.flowRate / self.hydraulicDipole2.crossSectionalArea
        volumetricMass1 = flow1.fluid.volumetricMass
        volumetricMass2 = flow2.fluid.volumetricMass
        dynamicViscosity1 = flow1.fluid.dynamicViscosity
        dynamicViscosity2 = flow2.fluid.dynamicViscosity
        thermicCapacity1 = flow1.fluid.thermicCapacity
        thermicCapacity2 = flow2.fluid.thermicCapacity
        thermicConductivity1 = flow1.fluid.thermicConductivity
        thermicConductivity2 = flow2.fluid.thermicConductivity
        
        entryTemperature1 = flow1.entryTemperature
        entryTemperature2 = flow2.entryTemperature

        hydraulicCapacity1 = flow1.flowRate * flow1.fluid.thermicCapacity * flow1.fluid.volumetricMass
        hydraulicCapacity2 = flow2.flowRate * flow2.fluid.thermicCapacity * flow2.fluid.volumetricMass 
        hydraulicCapacity = min(hydraulicCapacity1, hydraulicCapacity2)
        fluid1 = self.hydraulicDipole1.flow.fluid
        fluid2 = self.hydraulicDipole2.flow.fluid
        def g(T): #T = [T1s, T2s]
            outletTemperature1 = T[0]
            outletTemperature2 = T[1]
            averageTemperature1 = entryTemperature1 + outletTemperature1
            averageTemperature2 = entryTemperature2 + outletTemperature2
            flow1.fluid.volumetricMassEvolution(averageTemperature1, averagePressure1)
            flow2.fluid.volumetricMassEvolution(averageTemperature2, averagePressure2)
            flow1.fluid.dynamicViscosityEvolution(averageTemperature1, averagePressure1)
            flow2.fluid.dynamicViscosityEvolution(averageTemperature2, averagePressure2)
            flow1.fluid.thermicCapacityEvolution(averageTemperature1, averagePressure1)
            flow2.fluid.thermicCapacityEvolution(averageTemperature2, averagePressure2)
            flow1.fluid.thermicConductivityEvolution(averageTemperature1, averagePressure1)
            flow2.fluid.thermicConductivityEvolution(averageTemperature2, averagePressure2)
            caracteristicLength1 = self.hydraulicDipole1.hydraulicDiameter
            caracteristicLength2 = self.hydraulicDipole2.hydraulicDiameter
            caracteristicVelocity1 = flow1.flowRate / self.hydraulicDipole1.crossSectionalArea
            caracteristicVelocity2 = flow2.flowRate / self.hydraulicDipole2.crossSectionalArea
            volumetricMass1 = flow1.fluid.volumetricMass
            volumetricMass2 = flow2.fluid.volumetricMass
            dynamicViscosity1 = flow1.fluid.dynamicViscosity
            dynamicViscosity2 = flow2.fluid.dynamicViscosity
            thermicCapacity1 = flow1.fluid.thermicCapacity
            thermicCapacity2 = flow2.fluid.thermicCapacity
            thermicConductivity1 = flow1.fluid.thermicConductivity
            thermicConductivity2 = flow2.fluid.thermicConductivity



            reynoldsNumber1 = HydraulicThermicCalculus.reynolds(caracteristicLength1,caracteristicVelocity1,volumetricMass1, dynamicViscosity1)
            reynoldsNumber2 = HydraulicThermicCalculus.reynolds(caracteristicLength2,caracteristicVelocity2,volumetricMass2,dynamicViscosity2)
            prandtlNumber1 = HydraulicThermicCalculus.prandtl(dynamicViscosity1,thermicCapacity1, thermicConductivity1)
            prandtlNumber2 = HydraulicThermicCalculus.prandtl(dynamicViscosity2,thermicCapacity2,thermicConductivity2)
            K = self.thermicTransfertCoefficient(reynoldsNumber1, prandtlNumber1, reynoldsNumber2, prandtlNumber2, fluid1, fluid2)
            NUT = self.NUT(K)
            efficacity = self.efficacity(NUT)
            thermicPower = efficacity * hydraulicCapacity * abs(entryTemperature1 - entryTemperature2)
            if entryTemperature1 >= entryTemperature2 :
                outletTemperature1 = - thermicPower / hydraulicCapacity1 + entryTemperature1
                outletTemperature2 = thermicPower / hydraulicCapacity2 + entryTemperature2
            else :
                outletTemperature1 = thermicPower / hydraulicCapacity1 + entryTemperature1
                outletTemperature2 = - thermicPower / hydraulicCapacity2 + entryTemperature2

            T = [outletTemperature1, outletTemperature2]
            return T
            
            
        T = Resolve.fixePointResolution(g, [estimationOutletTemperature1, estimationOutletTemperature2], seuil = 0.0001)
        return T



class PlateExchanger(HeatExchanger):
    def __init__(self, materialConductivity = 21.9,exchangeSurface = 600,hydraulicDipole1 = None,hydraulicDipole2 = None, length = 2.5,width = 1.0,plateNumber = 385.0,passeNumber = 1,plateThickness = 0.5,plateGap = 3.0,angle = 45.0,streakWaveLength = None, globalThermicCoefficient = 5000.0,downstreamPole1 = Pole('downstreamPole1'), upstreamPole1 = Pole('upstreamPole1'), downstreamPole2 = Pole('downstreamPole2'), upstreamPole2 = Pole('upstreamPole2'), flow1 = Flow(), flow2 = Flow()) : 
        # Calcul du diamètre hydraulique :
        x = 2 * pi * plateGap / streakWaveLength
        phi = 1 / 6 * (1 + (1 + x ** 2) ** (1/2) + 4 * (1 + x ** 2/2) ** (1/2))
        hydraulicDiameter = 4 * plateGap / phi

        # Calcul de la surface transversale pour des deux côtés de l'échangeur :
        crossSectionArea = (plateNumber - 1) * plateGap * 10 ** (-3) * width / 2 

        # Création des instances de classes dipole :

        hydraulicDipole1 = PlateHeatExchangerSide('Plate Heat exchanger side 1', hydraulicDiameter, crossSectionArea, angle, length, passeNumber, downstreamPole = downstreamPole1, upstreamPole = upstreamPole1, flow=flow1)
        hydraulicDipole2 = PlateHeatExchangerSide('Plate Heat exchanger side 2', hydraulicDiameter, crossSectionArea, angle, length, passeNumber, downstreamPole = downstreamPole2, upstreamPole = upstreamPole2,flow=flow2)

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
        if rapport == None:
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


