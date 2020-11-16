#creation de la classe Dipole
from math import pi 
from math import log10
import matplotlib.pyplot as plt
import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes")
from Calculus import Resolve
class Dipole :
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



class Pipe(Dipole):
        #l'initialisation de la classe : 
    def __init__(self,name = 'Pipe',hydraulicDiameter = 0.348, rugosity = 0.0005, length = 50,correlation = True) : 
        Dipole.__init__(self,name, hydraulicDiameter, hydraulicDiameter**2*pi/4,correlation)
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
    
    def headLossCorrelation(self, reynoldsNumber, length = None, hydraulicDiameter = None, rugosity = None):

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
                      



#tests
dipole = Dipole()
pipe = Pipe()
print(pipe.rugosity)
print(pipe.hydraulicDiameter)
print(pipe.headLossCorrelation(5000))

reynolds = [i for i in range(1,100000)]
headLossCoefficient = [pipe.headLossCorrelation(i) for i in reynolds]

plt.plot(reynolds,headLossCoefficient)
plt.show()
