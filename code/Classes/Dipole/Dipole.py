#creation de la classe Dipole
from math import log
from math import pi 
from math import log10
from math import cos
from math import sin
from math import tan
import matplotlib.pyplot as plt
import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid")
from Calculus import Resolve
from HydraulicThermicCalculus import HydraulicThermicCalculus
from Fluid import Fluid
eau = Fluid()

class Dipole :

     
    #l'initialisation de la classe : 
    def __init__(self,name = 'Dipole',hydraulicDiameter = None,crossSectionalArea = None) : 
        self.__name = name
        self.__hydraulicDiameter = hydraulicDiameter
        self.__crossSectionalArea = crossSectionalArea

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



    def correlation(self, reynolds) :
        return "Don't defined"

    def caracteristic(self, flow, fluid) :
        return "Don't defined"

    def calorificIntake(self, flow, fluid) :
        return "Don't defined"


class Pipe(Dipole):
    
    #l'initialisation de la classe : 

    def __init__(self,name = 'Pipe',hydraulicDiameter = 0.348, rugosity = 0.0005, length = 50) : 
        Dipole.__init__(self, name, hydraulicDiameter, hydraulicDiameter**2*pi/4)
        self.__rugosity = rugosity
        self.__length = length
    
    @property 
    def rugosity(self): 
        return self.__rugosity

    @rugosity.setter 
    def rugosity(self,rugosity): 
        self.__rugosity = rugosity

    @property 
    def length(self): 
        return self.__length

    @length.setter 
    def length(self,length): 
        self.__length = length
    
    def correlation(self, reynoldsNumber, length = None, hydraulicDiameter = None, rugosity = None):

        if length == None :
            length = self.length
        if hydraulicDiameter == None :
            hydraulicDiameter = self.hydraulicDiameter
        if rugosity == None :
            rugosity = self.rugosity

        def laminar(reynoldsNumber):
            if reynoldsNumber > 0 :
                return 64 / reynoldsNumber
        
        def turbulent(reynoldsNumber, rugosity, hydraulicDiameter):
            Inconnue0 = 100 #le point fixe de la fonction g définit sur la ligne suivante correspond à 1/sqrt(coefficient de perte de charge)
            def g(Inconnue):
                return -2 * log10(2.51 / reynoldsNumber * Inconnue + rugosity / (3.7 * hydraulicDiameter))
            Inconnue = Resolve.fixePointResolution(g, Inconnue0) 
            headLossCoefficient = 1 / Inconnue ** 2
            return headLossCoefficient
        
        if reynoldsNumber < 2000 :
            return laminar(reynoldsNumber) * length / hydraulicDiameter
        if reynoldsNumber >= 2000 and reynoldsNumber <=4000 :
            coefficient = (reynoldsNumber - 2000)/2000
            return (1-coefficient) * laminar(reynoldsNumber) * length / hydraulicDiameter + coefficient * turbulent(reynoldsNumber,rugosity,hydraulicDiameter) * length / hydraulicDiameter
        else :
            return turbulent(reynoldsNumber,rugosity,hydraulicDiameter) * length / hydraulicDiameter

    def caracteristic(self, flow, fluid = eau, flowRateUnity = "m3/s", pressureUnity = "Pa"):
        return HydraulicThermicCalculus.caracteristic(self, flow, fluid, flowRateUnity, pressureUnity)
    


                      
class PlateHeatExchangerSide(Dipole):
    def __init__(self,name = 'Plate Heat-exchanger side',hydraulicDiameter = None, crossSectionalArea = None, angle = None, length = None, Npasse = 1) : 
        Dipole.__init__(self, name, hydraulicDiameter, crossSectionalArea)
        self.__angle = angle
        self.__length = length
    
    @property 
    def angle(self): 
        return self.__angle

    @angle.setter 
    def angle(self,angle): 
        self.__angle = angle

    @property 
    def length(self): 
        return self.__length

    @length.setter 
    def length(self,length): 
        self.__length = length
    
    @property 
    def Npasse(self): 
        return self.__Npasse

    @Npasse.setter 
    def Npasse(self,Npasse): 
        self.__Npasse = Npasse
    
    def correlation(self, reynoldsNumber, length = None, angle = None, Npasse = None): #correspond à la correlation de Martin
        if length == None:
            length = self.length
        if angle == None:
            angle = self.angle
        if Npasse == None:
            Npasse = self.Npasse
        angle = angle * Pi / 180
        
        def laminar(reynoldsNumber, angle):
            if reynoldsNumber > 0 :
                f0 = 16 / reynoldsNumber
                f1 = 149.25 / reynoldsNumber + 0.9625
                etape = etapeCalcul(angle, f0, f1)
                return 1 / etape ** 2
            else : 
                raise ValueError('reynoldsNumber should be superior to 0')

        def turbulent(reynoldsNumber, angle):
            f0 = (1.56 * log(reynoldsNumber) - 3) ** (-2)
            f1 = 9.75 / reynoldsNumber ** 0.289
            etape = etapeCalcul(angle, f0, f1)
            return 1 / etape ** 2

        def etapeCalcul(angle, f0, f1):
            return cos(angle) / (0.045 * tan(angle) + 0.09 * sin(angle) + f0 / cos(angle)) ** (1/2) + (1 - cos(angle)) / (3.8 * f1) ** (1/2)

        if reynoldsNumber < 2000 :
            return laminar(reynoldsNumber) * length / hydraulicDiameter * Npasse
        if reynoldsNumber >= 2000 and reynoldsNumber <=4000 :
            coefficient = (reynoldsNumber - 2000)/2000
            return (1-coefficient) * laminar(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse + coefficient * turbulent(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse
        else :
            return turbulent(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse

    def caracteristic(self, flow, fluid = eau, flowRateUnity = "m3/s", pressureUnity = "Pa"):
            return HydraulicThermicCalculus.caracteristic(self, flow, fluid, flowRateUnity, pressureUnity)
        
        



#tests
eau = Fluid()
dipole = Dipole()
pipe = Pipe()
def calorificIntake():
    return None
pipe.calorificIntake = calorificIntake
print(pipe.rugosity)
print(pipe.hydraulicDiameter)
print(pipe.correlation(5000))
print(pipe.caracteristic(500, eau, "m3/h", "mCE"))
print(dipole.correlation(2))
print(pipe.calorificIntake())

# print(pipe.methodCaracteristic(500, eau, "m3/h", "mCE"))

# flowRate = [i/10 for i in range(1,20000)]
# headLoss = [pipe.methodCaracteristic(q, eau, "m3/h", "mCE") for q in flowRate]

# plt.plot(flowRate, headLoss)
# plt.show()
