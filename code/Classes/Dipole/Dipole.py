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
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Flow")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Graphe")
from Flow import Flow
from Graphe import Edge, Node
from Calculus import Resolve
from HydraulicThermicCalculus import HydraulicThermicCalculus
from Fluid import Fluid
eau = Fluid()

class Dipole(Edge):
    #l'initialisation de la classe : 
    def __init__(self,name = 'Dipole',hydraulicDiameter = None,crossSectionalArea = None, downstreamPole = None, upstreamPole = None, flow = Flow(fixedVariables=[])) : 
        Edge.__init__(self, name, [downstreamPole, upstreamPole])
        self.__hydraulicDiameter = hydraulicDiameter
        self.__crossSectionalArea = crossSectionalArea
        self.__flow = flow
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
    def flow(self): 
        return self.__flow

    @flow.setter 
    def flow(self,flow): 
        self.__flow = flow

    def hydraulicCorrelation(self, reynolds) :
        return "Don't defined"

    def caracteristic(self, flow, fluid) :
        return "Don't defined"

    def thermicCorrelation(self, flow, fluid) :
        return "Don't defined"


class Pipe(Dipole):
    
    #l'initialisation de la classe : 

    def __init__(self,name = 'Pipe',hydraulicDiameter = 0.348, rugosity = 0.0005, length = 50, downstreamPole = None, upstreamPole = None, flow = Flow(fixedVariables=[])) : 
        Dipole.__init__(self, name, hydraulicDiameter, hydraulicDiameter**2*pi/4, downstreamPole, upstreamPole, flow)
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
    
    def hydraulicCorrelation(self, reynoldsNumber, length = None, hydraulicDiameter = None, rugosity = None):

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
    def __init__(self,name = 'Plate Heat-exchanger side',hydraulicDiameter = None, crossSectionalArea = None, angle = None, length = None, Npasse = 1, hydraulicCorrectingFactor = 1, thermicCorrectingFactor = 1, downstreamPole = None, upstreamPole = None, flow = Flow(fixedVariables=[])) : 
        Dipole.__init__(self, name, hydraulicDiameter, crossSectionalArea, downstreamPole, upstreamPole, flow)
        self.__angle = angle
        self.__length = length
        self.__Npasse = Npasse
        self.__hydraulicCorrectingFactor = hydraulicCorrectingFactor
        self.__thermicCorrectingFactor = thermicCorrectingFactor
    
    @property      
    def downstreamPole(self): 
        return self.__downstreamPole

    @downstreamPole.setter 
    def downstreamPole(self,downstreamPole): 
        self.__downstreamPole = downstreamPole
    
    @property 
    def upstreamPole(self): 
        return self.__upstreamPole

    @upstreamPole.setter 
    def upstreamPole(self,upstreamPole): 
        self.__upstreamPole = upstreamPole

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

    @property 
    def hydraulicCorrectingFactor(self): 
        return self.__hydraulicCorrectingFactor

    @Npasse.setter 
    def hydraulicCorrectingFactor(self,Npasse): 
        self.__hydraulicCorrectingFactor = hydraulicCorrectingFactor

    @property 
    def thermicCorrectingFactor(self): 
        return self.__thermicCorrectingFactor
    @property 
    def downstreamPole(self): 
        return self.__downstreamPole

    @downstreamPole.setter 
    def downstreamPole(self,downstreamPole): 
        self.__downstreamPole = downstreamPole
    
    @property 
    def upstreamPole(self): 
        return self.__upstreamPole

    @upstreamPole.setter 
    def upstreamPole(self,upstreamPole): 
        self.__upstreamPole = upstreamPole
    
    def hydraulicCorrelation(self, reynoldsNumber, length = None, angle = None, Npasse = None, hydraulicDiameter = None, parameterA = 3.8, parameterB = 0.045, parameterC = 0.09): #correspond à la hydraulicCorrelation de Martin
        if length == None:
            length = self.length
        if angle == None:
            angle = self.angle
        if Npasse == None:
            Npasse = self.Npasse
        if hydraulicDiameter == None:
            hydraulicDiameter = self.hydraulicDiameter

        angle = angle * pi / 180
        
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
            return cos(angle) / (parameterB * tan(angle) + parameterC * sin(angle) + f0 / cos(angle)) ** (1/2) + (1 - cos(angle)) / (parameterA * f1) ** (1/2)

        if reynoldsNumber < 2000 :
            return laminar(reynoldsNumber) * length / hydraulicDiameter * Npasse
        if reynoldsNumber >= 2000 and reynoldsNumber <=4000 :
            coefficient = (reynoldsNumber - 2000)/2000
            return (1-coefficient) * laminar(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse + coefficient * turbulent(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse
        else :
            return turbulent(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse

    def caracteristic(self, flow, fluid = eau, flowRateUnity = "m3/s", pressureUnity = "Pa", hydraulicCorrectingFactor = None):
        if hydraulicCorrectingFactor == None :
            hydraulicCorrectingFactor = self.hydraulicCorrectingFactor

        return HydraulicThermicCalculus.caracteristic(self, flow, fluid, flowRateUnity, pressureUnity) * hydraulicCorrectingFactor

    def thermicCorrelation(self, reynoldsNumber, prandtlNumber, length = None, angle = None, Npasse = None, hydraulicDiameter = None, parameterA = 3.8, parameterB = 0.045, parameterC = 0.09, thermicCorrectingFactor = None):
        if angle == None:
            angle = self.angle 
        if length == None:
            length = self.length
        if angle == None:
            angle = self.angle
        if Npasse == None:
            Npasse = self.Npasse
        if thermicCorrectingFactor == None:
            thermicCorrectingFactor = self.thermicCorrectingFactor
        if hydraulicDiameter == None:
            hydraulicDiameter = self.hydraulicDiameter

        headLossCoefficient = self.hydraulicCorrelation(reynoldsNumber, parameterA = 3.8, parameterB = 0.045, parameterC = 0.09) / Npasse / length * hydraulicDiameter
        angle *= pi / 180
        nusseltNumber = 0.122 * prandtlNumber ** (1/3) * (headLossCoefficient * reynoldsNumber ** 2 * sin(2 * angle) ) ** 0.374

        return nusseltNumber * thermicCorrectingFactor

        
class IdealPump(Dipole):
    #l'initialisation de la classe : 
    def __init__(self,name = None, hydraulicDiameter = None,crossSectionalArea = None ,flowRate = None, downstreamPole = None, upstreamPole = None) : 
        Dipole.__init__(self, name, hydraulicDiameter, crossSectionalArea, downstreamPole, upstreamPole, flow = Flow(flowRate = flowRate, fixedVariables=["flowRate"]))



class Pole(Node):
    def __init__(self,name = None, pressure = None, temperature = None, fluid = None, successors = None) : 
        Node.__init__(self, name = name, successors = successors)
        self.__pressure = pressure
        self.__temperature = temperature
        self.__fluid = fluid

    @property 
    def pressure(self): 
        return self.__pressure

    @pressure.setter 
    def pressure(self,pressure): 
        self.__pressure = pressure
    
    @property 
    def temperature(self): 
        return self.__temperature

    @temperature.setter 
    def temperature(self,temperature): 
        self.__temperature = temperature

    @property 
    def fluid(self): 
        return self.__fluid

    @fluid.setter 
    def fluid(self,fluid): 
        self.__fluid = fluid

#tests
eau = Fluid()
dipole = Dipole()
pipe = Pipe()
plateHeatExchangerSide = PlateHeatExchangerSide(hydraulicDiameter=0.2, crossSectionalArea=0.5, angle = 45, length=1)
headLossCoefficient = plateHeatExchangerSide.hydraulicCorrelation(5000)
nusseltNumber = plateHeatExchangerSide.thermicCorrelation(5000,1)


# print(pipe.methodCaracteristic(500, eau, "m3/h", "mCE"))

# flowRate = [i/10 for i in range(1,20000)]
# headLoss = [pipe.methodCaracteristic(q, eau, "m3/h", "mCE") for q in flowRate]

# plt.plot(flowRate, headLoss)
# plt.show()
