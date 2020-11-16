#creation de la classe Dipole
from math import pi 
from math import log10
import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes")
from Calculus import Resolve
class Dipole :
    #l'initialisation de la classe : 
    def __init__(self,name = 'Dipole',fluid = 'class eau',hydraulicDiameter = None,crossSectionalArea = None,correlation = False) : 
        self.__name = name
        self.__fluid = fluid
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
    def fluid(self): 
        return self.__fluid

    @fluid.setter 
    def fluid(self,fluid): 
        self.__fluid = fluid

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
    
    def headLossCorrelation(reynoldsNumber, length = self.length, hydraulicDiameter = self.hydraulicDiameter, rugosity = self.rugosity):
        def laminar(reynoldsNumber):
            if reynoldsNumber > 0 :
                return 64 / reynoldsNumber
        
        def turbulent(reynoldsNumber, rugosity, hydraulicDiameter):
            headLossCoefficient0 = 100
            def g(headLossCoefficient):
                return -2 * log10(2.51 / reynoldsNumber * headLossCoefficient + rugosity / (3.7 * hydraulicDiameter))
            headLossCoefficient = Resolve.fixePointResolution(g, headLossCoefficient0)
        
        if reynoldsNumber < 2000 :
            return laminar(reynoldsNumber) * length / hydraulicDiameter
        if reynoldsNumber >= 2000 and reynoldsNumber <=4000 :
            coefficient = (reynoldsNumber - 2000)/2000
            return (1-coefficient) * laminar(reynoldsNumber) * length / hydraulicDiameter + coefficient * turbulent(reynoldsNumber,rugosity,hydraulicDiameter) * length / hydraulicDiameter
        else :
            return turbulent(reynoldsNumber,rugosity,hydraulicDiameter) * length / hydraulicDiameter
                      



#tests
dipole = Dipole()
pipe = Pipe(rugosity=0.1)
print(pipe.rugosity)
print(pipe.headLossCorrelation(5000))