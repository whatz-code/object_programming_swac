import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code")
from ExceptionsAndErrors import typeErrorAtEntering
class Fluid:
    #l'initialisation de la classe : 
    def __init__(self,name = 'eau',volumetricMass = float(1000),dynamicViscosity = 0.001,thermicCapacity = float(4150),thermicConductivity = 0.6) : 
        self.__name = name

        self.__volumetricMass = None
        typeErrorAtEntering(self.__volumetricMass, volumetricMass, float, "the volumetric mass must be a float number")
        self.__volumetricMass = volumetricMass

        self.__dynamicViscosity = None
        typeErrorAtEntering(self.__dynamicViscosity, dynamicViscosity, float, "the dynamic viscosity must be a float number")
        self.__dynamicViscosity = dynamicViscosity

        self.__thermicCapacity = None
        typeErrorAtEntering(self.__thermicCapacity, thermicCapacity, float, "the thermic capacity must be a float number")
        self.__thermicCapacity = thermicCapacity

        self.__thermicConductivity = None
        typeErrorAtEntering(self.__thermicConductivity, thermicConductivity, float, "the thermic conductivity must be a float number")
        self.__thermicConductivity = thermicConductivity

    @property 
    def name(self): 
        return self.__name

    @name.setter 
    def name(self,name): 
        self.__name = name

    @property 
    def volumetricMass(self): 
        return self.__volumetricMass

    @volumetricMass.setter 
    def volumetricMass(self,volumetricMass):
        typeErrorAtEntering(self.__volumetricMass, volumetricMass, float, "the volumetric mass must be a float number")
        self.__volumetricMass = volumetricMass

    @property 
    def dynamicViscosity(self): 
        return self.__dynamicViscosity

    @dynamicViscosity.setter 
    def dynamicViscosity(self,dynamicViscosity): 
        typeErrorAtEntering(self.__dynamicViscosity, dynamicViscosity, float, "the volumetric mass must be a float number")
        self.__dynamicViscosity = dynamicViscosity

    @property 
    def thermicCapacity(self): 
        return self.__thermicCapacity

    @thermicCapacity.setter 
    def thermicCapacity(self,thermicCapacity): 
        typeErrorAtEntering(self.__thermicCapacity, thermicCapacity, float, "the volumetric mass must be a float number")
        self.__thermicCapacity = thermicCapacity

    @property 
    def thermicConductivity(self): 
        return self.__thermicConductivity

    @thermicConductivity.setter 
    def thermicConductivity(self,thermicConductivity): 
        typeErrorAtEntering(self.__thermicConductivity, thermicConductivity, float, "the volumetric mass must be a float number")
        self.__thermicConductivity = thermicConductivity

    def volumetricMassEvolutionDefinition(self, dependancy):
        def a():
            pass
        if type(dependancy) is not type(a) :
            raise TypeError("the fluid dependency must be a function")
        else :
            try :
                a = dependancy(temperature = 20, pressure = 10)
            except TypeError :
                raise TypeError("the fluid dependency must be a function of temperature and pressure")
            def volumetricMassEvolutionDefinition(temperature, pressure, modify = True):
                if modify :
                    self.volumetricMass = dependancy(temperature, pressure)
                return dependancy(temperature, pressure)
    
    def dynamicViscosityEvolutionDefinition(self, dependancy):
        if type(dependancy) is not type(dynamicViscosityEvolution) :
            raise TypeError("the fluid dependency must be a function")
        else :
            try :
                a = dependancy(temperature = 20, pressure = 10)
            except TypeError :
                raise TypeError("the fluid dependency must be a function of temperature and pressure")
            def dynamicViscosityEvolutionDefinition(temperature, pressure, modify = True):
                if modify :
                    self.dynamicViscosity = dependancy(temperature, pressure)
                return dependancy(temperature, pressure)

    def thermicCapacityEvolutionDefinition(self, dependancy):
        if type(dependancy) is not type(thermicCapacityEvolution) :
            raise TypeError("the fluid dependency must be a function")
        else :
            try :
                a = dependancy(temperature = 20, pressure = 10)
            except TypeError :
                raise TypeError("the fluid dependency must be a function of temperature and pressure")
            def thermicCapacityEvolutionDefinition(temperature, pressure, modify = True):
                if modify :
                    self.thermicCapacity = dependancy(temperature, pressure)
                return dependancy(temperature, pressure)

    def thermicConductivityEvolutionDefinition(self, dependancy):
        if type(dependancy) is not type(thermicConductivityEvolution) :
            raise TypeError("the fluid dependency must be a function")
        else :
            try :
                a = dependancy(temperature = 20, pressure = 10)
            except TypeError :
                raise TypeError("the fluid dependency must be a function of temperature and pressure")
            def thermicConductivityEvolutionDefinition(temperature, pressure, modify = True):
                if modify :
                    self.thermicConductivity = dependancy(temperature, pressure)
                return dependancy(temperature, pressure)

    def volumetricMassEvolution(temperature, pressure, modify = True):
        return None

    def dynamicViscosityEvolution(temperature, pressure, modify = True):
        return None

    def thermicCapacityEvolution(temperature, pressure, modify = True):
        return None

    def thermicConductivityEvolution(temperature, pressure, modify = True):
        return None

    


    
    
#micro tests
b = 0
def a(b):
    class Solution:
        pass
    solution = Solution()
    solution.temp = b
    return solution


