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
import numpy as np
from FlowFolder.Flow import Flow
from GraphFolder.Graphe import Edge, Node
from Calculus import Resolve
from HydraulicThermicCalculus import HydraulicThermicCalculus
from FluidFolder.Fluid import Fluid
from Calculus import DataAnalysis
eau = Fluid()

class Pole(Node):
    def __init__(self,name = None, pressure = None, temperature = None, successors = []) : 
        Node.__init__(self, name = name, successors = successors)
        if (type(temperature) is not float or type(pressure) is not float) and (type(temperature) is not type(None) or type(pressure) is not type(None)):
            raise TypeError("the temperature and the pressure must be float numbers")
        self.__pressure = pressure
        self.__temperature = temperature

    @property 
    def pressure(self): 
        return self.__pressure

    @pressure.setter 
    def pressure(self,pressure): 
        if type(pressure) is not float :
            raise  TypeError("the pressure must be a float number")
        self.__pressure = pressure
    
    @property 
    def temperature(self): 
        return self.__temperature

    @temperature.setter 
    def temperature(self,temperature): 
        if type(temperature) is not float :
            raise  TypeError("the temperature must be a float number")
        self.__temperature = temperature

class Dipole(Edge):
    #l'initialisation de la classe : 
    def __init__(self,name = 'Dipole',hydraulicDiameter = None,crossSectionalArea = None, downstreamPole = Pole('downstream pole'), upstreamPole = Pole('upstream Pole'), flow = Flow(), variables = [False, False, False]) : 
        if type(downstreamPole) is not Pole or type(upstreamPole) is not Pole:
            raise TypeError("downstreamPole and upstreamPole must be a pole")
        Edge.__init__(self, name, [downstreamPole, upstreamPole])
        if not(isinstance(flow,Flow)) and type(flow) is not type(None):
            raise TypeError('flow must be Flow Type')
        if type(hydraulicDiameter) is not float and type(hydraulicDiameter) is not type(None):
            raise TypeError('The hydraulic diameter must be a float')
        if type(hydraulicDiameter) is not type(None):
            if hydraulicDiameter <= 0:
                raise ValueError('hydraulic diameter must be strictly positive')
        if type(crossSectionalArea) is not float and type(crossSectionalArea) is not type(None):
            raise TypeError('The cross sectionnal area must be a float')
        if type(crossSectionalArea) is not type(None):
            if crossSectionalArea <= 0:
                raise ValueError('cross sectionnal area must be strictly positive')
        if type(variables) is not list:
            raise TypeError("the variables should be a list of 3 booleans")
        if len(variables) != 3:
            raise TypeError("the variables should be a list of 3 booleans")
        for variable in variables :
            if type(variable) is not bool: 
                raise TypeError("the variables should be a list of 3 booleans")
        self.__name = name
        self.__hydraulicDiameter = hydraulicDiameter
        self.__crossSectionalArea = crossSectionalArea
        self.__flow = flow
        self.__variables = variables
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
        if type(hydraulicDiameter) is not float:
            raise TypeError("The hydraulic diameter must be a float") 
        if type(hydraulicDiameter) is not type(None):
            if hydraulicDiameter <= 0:
                raise ValueError('hydraulic diameter must be strictly positive')
     
        self.__hydraulicDiameter = hydraulicDiameter

    @property 
    def crossSectionalArea(self): 
        return self.__crossSectionalArea

    @crossSectionalArea.setter 
    def crossSectionalArea(self,crossSectionalArea): 
        if type(crossSectionalArea) is not float:
            raise TypeError('The cross sectionnal area must be a float')
        if type(crossSectionalArea) is not type(None):
            if crossSectionalArea <= 0:
                raise ValueError('cross sectionnal area must be strictly positive')

        self.__crossSectionalArea = crossSectionalArea
    
    @property 
    def flow(self): 
        return self.__flow

    @flow.setter 
    def flow(self,flow): 
        if not(isinstance(flow,Flow)):
            raise TypeError('the flow must be a flow type')
        self.__flow = flow

    @property 
    def flow(self): 
        return self.__flow

    @flow.setter 
    def flow(self,flow): 
        if type(flow) is not Flow:
            raise TypeError('the flow must be a flow type')
        self.__flow = flow

    @property 
    def downstreamPole(self): 
        return self.nodes[0]

    @downstreamPole.setter 
    def downstreamPole(self,downstreamPole): 
        if type(downstreamPole) is not Pole:
            raise TypeError('the downstreamPole must be a Pole type')
        self.nodes[0] = downstreamPole
    
    @property 
    def upstreamPole(self): 
        return self.nodes[1]

    @upstreamPole.setter 
    def upstreamPole(self,upstreamPole): 
        if type(upstreamPole) is not Pole:
            raise TypeError('the upstreamPole must be a Pole type')
        self.nodes[1] = upstreamPole

    @property 
    def variables(self): 
        return self.__variables

    @variables.setter 
    def variables(self,variables): 
        if type(variables) is not list:
            raise TypeError("the variables should be a list of 3 booleans")
        if len(variables) != 3:
            raise TypeError("the variables should be a list of 3 booleans")
        for variable in variables :
            if type(variable) is not bool: 
                raise TypeError("the variables should be a list of 3 booleans")
        self.__variables = variables
    

    def hydraulicCorrelation(self, reynoldsNumber) :
        if type(reynoldsNumber) is float:
            raise type("reynolds number must be a float")
        return None

    def caracteristic(self, flowRate = None, fluid = None) :
        if flowRate == None:
            flowRate = self.flow.flowRate
        if fluid == None:
            fluid = self.flow.fluid
        if type(flowRate) is not float or type(fluid) is not Fluid:
            raise TypeError("flowRate must be float type and fluid must be fluid type")
        return None

    def thermicCorrelation(self, reynoldsNumber, prandtlNumber):
        if type(reynoldsNumber) is not float or type(prandtlNumber) is not float:
            raise TypeError("reynolds number and prandtl number must be float type")
        return None


class Pipe(Dipole):
    
    #l'initialisation de la classe : 

    def __init__(self,name = 'Pipe',hydraulicDiameter = 0.348, rugosity = 0.0005, length = 50.0, downstreamPole = Pole('downstream pole'), upstreamPole = Pole('upstream Pole'), flow = Flow()) : 
        Dipole.__init__(self, name, hydraulicDiameter, hydraulicDiameter**2*pi/4, downstreamPole, upstreamPole, flow, variables=[True, True, False])
        if type(rugosity) is not float :
            raise TypeError('rugosity has to be a float number')
        if rugosity < 0:
            raise ValueError('rugosity must be positive')
        if type(length) is not float:
            raise TypeError('length must be a float number')
        if length < 0:
            raise ValueError('length must be positive')
        self.__rugosity = rugosity
        self.__length = length
        self.flow.temperatureDifference = 0.0
    
    @property 
    def rugosity(self): 
        return self.__rugosity

    @rugosity.setter 
    def rugosity(self,rugosity): 
        if type(rugosity) is not float :
            raise TypeError('rugosity has to be a float number')
        if rugosity < 0:
            raise ValueError('rugosity must be positive')
      
        self.__rugosity = rugosity

    @property 
    def length(self): 
        return self.__length

    @length.setter 
    def length(self,length): 
        if type(length) is not float:
            raise TypeError('length must be a float number')
        if length < 0:
            raise ValueError('length must be positive')

        self.__length = length
    

    def hydraulicCorrelation(self, reynoldsNumber, length = None, hydraulicDiameter = None, rugosity = None):
        if length == None :
            length = self.length
        if hydraulicDiameter == None :
            hydraulicDiameter = self.hydraulicDiameter
        if rugosity == None :
            rugosity = self.rugosity
        if type(reynoldsNumber) is not float:
            raise TypeError('the reynolds number must be a strictly positive float')
        if reynoldsNumber <= 0:
            raise ValueError('the reynolds number must be a strictly positive float')
        if type(rugosity) is not float :
            raise TypeError('rugosity has to be a float number')
        if rugosity < 0:
            raise ValueError('rugosity must be positive')
        if type(length) is not float:
            raise TypeError('length must be a float number')
        if length < 0:
            raise ValueError('length must be positive')
        if type(hydraulicDiameter) is not float:
            raise TypeError('hydraulic diameter must be a float number')
        if length <=0 :
            raise ValueError('hydraulic diameter must be a strictyly positive float number')

        def laminar(reynoldsNumber):
            if reynoldsNumber > 0 :
                return 64 / reynoldsNumber
            else :
                raise ValueError("the reynolds number must be strictly positive")
        
        def turbulent(reynoldsNumber, rugosity, hydraulicDiameter):
            Inconnue0 = 1 #le point fixe de la fonction g définit sur la ligne suivante correspond à 1/sqrt(coefficient de perte de charge)
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
        if reynoldsNumber > 4000:
            return turbulent(reynoldsNumber,rugosity,hydraulicDiameter) * length / hydraulicDiameter

    def caracteristic(self, flowRate = None, fluid = None, flowRateUnity = "m3/s", pressureUnity = "Pa"):
        if flowRate == None:
            flowRate = self.flow.flowRate
        if fluid == None:
            fluid = self.flow.fluid

        if type(flowRate) is not float and not(isinstance(flowRate,np.float64)):
            raise TypeError('the flow rate must be a float number')
        if not(isinstance(fluid,Fluid)):
            raise TypeError('fluid must be a Fluid')
        return - HydraulicThermicCalculus.caracteristic(self, flowRate, fluid, flowRateUnity, pressureUnity)
    


                      
class PlateHeatExchangerSide(Dipole):
    def __init__(self,name = 'Plate Heat-exchanger side',width = None, plateGap = None, streakWaveLength = None, plateNumber = None, angle = None, length = None, Npasse = 1, hydraulicCorrectingFactor = 1.0, thermicCorrectingFactor = 1.0, downstreamPole = Pole('downstream pole'), upstreamPole = Pole('upstream Pole'), flow = Flow()) : 
        # Calcul du diamètre hydraulique :
        x = 2 * pi * plateGap / streakWaveLength
        phi = 1 / 6 * (1 + (1 + x ** 2) ** (1/2) + 4 * (1 + x ** 2/2) ** (1/2))
        hydraulicDiameter = 4 * plateGap / phi


        # Calcul de la surface transversale pour des deux côtés de l'échangeur :
        crossSectionalArea = (plateNumber - 1) * plateGap * 10 ** (-3) * width / 2 

 

        Dipole.__init__(self, name, hydraulicDiameter, crossSectionalArea, downstreamPole, upstreamPole, flow, variables=[True, True, True])
        if type(angle) is not float:
            raise TypeError("the pattern angle must be a float number")
        if angle <0 or angle >90:
            raise ValueError("the angle must be 0 and 90 degree")
        if type(length) is not float:
            raise TypeError("the length must be a positive float")
        if length < 0 :
            raise   ValueError("the length must be a positive float")
        if type(Npasse) is not int:
            raise TypeError("the number of passe must be a positive integer superior to 1")
        if Npasse < 1:
            raise ValueError("the number of passe must be a positive integer superior to 1")
        if type(hydraulicCorrectingFactor) is not float:
            raise TypeError("the hydraulic correcting factor must be a strictly positive float close to 1")
        if hydraulicCorrectingFactor <= 0 :
            raise TypeError("the hydraulic correcting factor must be a strictly positive float close to 1")
        if type(thermicCorrectingFactor) is not float:
            raise TypeError("the thermic correcting factor must be a strictly positive float close to 1")
        if thermicCorrectingFactor <= 0 :
            raise TypeError("the thermic correcting factor must be a strictly positive float close to 1")


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
        self.__init__(self.name,self.hydraulicDiameter,self.crossSectionalArea,self.angle,self.length,self.Npasse,self.hydraulicCorrectingFactor,self.thermicCorrectingFactor, downstreamPole, self.upstreamPole, self.flow)
    
    @property 
    def upstreamPole(self): 
        return self.__upstreamPole

    @upstreamPole.setter 
    def upstreamPole(self,upstreamPole): 
        self.__init__(self.name,self.hydraulicDiameter,self.crossSectionalArea,self.angle,self.length,self.Npasse,self.hydraulicCorrectingFactor,self.thermicCorrectingFactor, self.downstreamPole, upstreamPole, self.flow)

    @property 
    def angle(self): 
        return self.__angle

    @angle.setter 
    def angle(self,angle): 
        self.__init__(self.name,self.hydraulicDiameter,self.crossSectionalArea,angle,self.length,self.Npasse,self.hydraulicCorrectingFactor,self.thermicCorrectingFactor, self.downstreamPole, self.upstreamPole, self.flow)

    @property 
    def length(self): 
        return self.__length

    @length.setter 
    def length(self,length): 
        self.__init__(self.name,self.hydraulicDiameter,self.crossSectionalArea,self.angle, length,self.Npasse,self.hydraulicCorrectingFactor,self.thermicCorrectingFactor, self.downstreamPole, self.upstreamPole, self.flow)
    
    @property 
    def Npasse(self): 
        return self.__Npasse

    @Npasse.setter 
    def Npasse(self,Npasse): 
        self.__init__(self.name,self.hydraulicDiameter,self.crossSectionalArea,self.angle,self.length,Npasse,self.hydraulicCorrectingFactor,self.thermicCorrectingFactor, self.downstreamPole, self.upstreamPole, self.flow)


    @property 
    def thermicCorrectingFactor(self): 
        return self.__thermicCorrectingFactor

    @thermicCorrectingFactor.setter 
    def thermicCorrectingFactor(self,thermicCorrectingFactor): 
        self.__init__(self.name,self.hydraulicDiameter,self.crossSectionalArea,self.angle,self.length,self.Npasse,self.hydraulicCorrectingFactor,thermicCorrectingFactor, self.downstreamPole, self.upstreamPole, self.flow)

    @property 
    def hydraulicCorrectingFactor(self): 
        return self.__hydraulicCorrectingFactor

    @hydraulicCorrectingFactor.setter 
    def hydraulicCorrectingFactor(self,hydraulicCorrectingFactor): 
        self.__init__(self.name,self.hydraulicDiameter,self.crossSectionalArea,self.angle,self.length,self.Npasse,hydraulicCorrectingFactor,self.thermicCorrectingFactor, self.downstreamPole, self.upstreamPole, self.flow)

    
    def hydraulicCorrelation(self, reynoldsNumber, length = None, angle = None, Npasse = None, hydraulicDiameter = None, parameterA = 3.8, parameterB = 0.045, parameterC = 0.09, hydraulicCorrectingFactor = 1.0): #correspond à la hydraulicCorrelation de Martin
        if length == None:
            length = self.length
        if angle == None:
            angle = self.angle
        if Npasse == None:
            Npasse = self.Npasse
        if hydraulicDiameter == None:
            hydraulicDiameter = self.hydraulicDiameter

        if type(angle) is not float:
            raise TypeError("the pattern angle must be a float number")
        if angle <0 or angle >90:
            raise ValueError("the angle must be 0 and 90 degree")
        if type(length) is not float:
            raise TypeError("the length must be a positive float")
        if length < 0 :
            raise   ValueError("the length must be a positive float")
        if type(Npasse) is not int:
            raise TypeError("the number of passe must be a positive integer superior to 1")
        if Npasse < 1:
            raise ValueError("the number of passe must be a positive integer superior to 1")
        if type(hydraulicCorrectingFactor) is not float:
            raise TypeError("the hydraulic correcting factor must be a strictly positive float close to 1")
        if hydraulicCorrectingFactor <= 0 :
            raise TypeError("the hydraulic correcting factor must be a strictly positive float close to 1")
        if type(reynoldsNumber) is not float:
            raise TypeError("the reynolds number must be a strictly positive float")
        if reynoldsNumber <=0 :
            raise ValueError("the reynolds number must be a strictly positive float")

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
            return laminar(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse
        if reynoldsNumber >= 2000 and reynoldsNumber <=4000 :
            coefficient = (reynoldsNumber - 2000)/2000
            return (1-coefficient) * laminar(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse + coefficient * turbulent(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse
        else :
            return turbulent(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse

    def caracteristic(self, flowRate = None, fluid = None, flowRateUnity = "m3/s", pressureUnity = "Pa", hydraulicCorrectingFactor = None):
        if hydraulicCorrectingFactor == None :
            hydraulicCorrectingFactor = self.hydraulicCorrectingFactor
        if flowRate == None:
            flowRate = self.flow.flowRate
        if fluid == None:
            fluid = self.flow.fluid

        if type(flowRate) is not float:
            raise TypeError('the flow rate must be a float number')
        if not(isinstance(fluid,Fluid)):
            raise TypeError('fluid must be a Fluid')

        return - HydraulicThermicCalculus.caracteristic(self, flowRate, fluid, flowRateUnity, pressureUnity) * hydraulicCorrectingFactor

    def thermicCorrelation(self, reynoldsNumber, prandtlNumber = None, length = None, angle = None, Npasse = None, hydraulicDiameter = None, parameterA = 3.8, parameterB = 0.045, parameterC = 0.09, thermicCorrectingFactor = 1.0):
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
        if prandtlNumber == None:
            prandtlNumber = self.flow.fluid.thermicCapacity * self.flow.fluid.dynamicViscosity / self.flow.fluid.thermicConductivity

        if type(angle) is not float:
            raise TypeError("the pattern angle must be a float number")
        if angle <0 or angle >90:
            raise ValueError("the angle must be 0 and 90 degree")
        if type(length) is not float:
            raise TypeError("the length must be a positive float")
        if length < 0 :
            raise   ValueError("the length must be a positive float")
        if type(Npasse) is not int:
            raise TypeError("the number of passe must be a positive integer superior to 1")
        if Npasse < 1:
            raise ValueError("the number of passe must be a positive integer superior to 1")
        if type(thermicCorrectingFactor) is not float:
            raise TypeError("the thermic correcting factor must be a strictly positive float close to 1")
        if thermicCorrectingFactor <= 0 :
            raise TypeError("the thermic correcting factor must be a strictly positive float close to 1")
        if type(reynoldsNumber) is not float or type(prandtlNumber) is not float:
            raise TypeError("the reynolds number and the prandtl number must be a strictly positive float")
        if reynoldsNumber <=0 or prandtlNumber <= 0:
            raise ValueError("the reynolds number and the prandtl number must be a strictly positive float")



        headLossCoefficient = self.hydraulicCorrelation(reynoldsNumber, parameterA = 3.8, parameterB = 0.045, parameterC = 0.09) / Npasse / length * hydraulicDiameter
        angle *= pi / 180
        nusseltNumber = 0.122 * prandtlNumber ** (1/3) * (headLossCoefficient * reynoldsNumber ** 2 * sin(2 * angle) ) ** 0.374

        return nusseltNumber * thermicCorrectingFactor

        
class IdealPump(Dipole):
    #l'initialisation de la classe : 
    def __init__(self,name = 'Ideal Pump', hydraulicDiameter = None, crossSectionalArea = None ,flowRate = None, fluid = Fluid(), inputTemperature = None, downstreamPole = Pole("downstream pole"), upstreamPole = Pole("upstream Pole")) : 
        Dipole.__init__(self, name, hydraulicDiameter, crossSectionalArea, downstreamPole, upstreamPole, flow = Flow(fluid = fluid, flowRate = flowRate, inputTemperature = inputTemperature), variables=[False,True, False])
        downstreamPole.temperature = inputTemperature
        self.flow.temperatureDifference = 0.0


class Pump(Dipole):
    #l'initialisation de la classe : 
    def __init__(self,name = 'Pump', hydraulicDiameter = None, crossSectionalArea = None ,flowRates = [], overPressures = [], fluid = Fluid(), inputTemperature = None, inputTemperature = None, downstreamPole = Pole("downstream pole"), upstreamPole = Pole("upstream Pole"), temperatureDifference = 0.0) : 
        Dipole.__init__(self, name, hydraulicDiameter, crossSectionalArea, downstreamPole, upstreamPole, flow = Flow(fluid = fluid, flowRate = flowRate, inputTemperature = inputTemperature), variables=[False,True, False])
        if type(flowRates) is not list or type(overPressures) is not list :
            raise TypeError('flowRates and overPressures must be a list of functionnement points')
        downstreamPole.temperature = inputTemperature
        self.flow.temperatureDifference = temperatureDifference
        self.caracteristic = DataAnalysis.interpolation(flowRates,overPressures)


#tests



# print(pipe.methodCaracteristic(500, eau, "m3/h", "mCE"))

# flowRate = [i/10 for i in range(1,20000)]
# headLoss = [pipe.methodCaracteristic(q, eau, "m3/h", "mCE") for q in flowRate]

# plt.plot(flowRate, headLoss)
# plt.show()
