import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code")
from ExceptionsAndErrors import typeErrorAtEntering
class Fluid:
    #l'initialisation de la classe : 
    def __init__(self,name = 'eau',volumetricMass = float(1000),dynamicViscosity = 0.001,thermicCapacity = float(4150),thermicConductivity = 0.6) : 
        self.__name = name
        
        typeErrorAtEntering( volumetricMass, message= "the volumetric mass must be a float number")
        if volumetricMass < 0:
            raise ValueError('volumetric mass must be positive')
        self.__volumetricMass = volumetricMass

        typeErrorAtEntering(dynamicViscosity, message = "the dynamic viscosity must be a float number")
        if dynamicViscosity < 0:
            raise ValueError('dynamic viscosity must be positive')
        self.__dynamicViscosity = dynamicViscosity
        
        typeErrorAtEntering( thermicCapacity, message = "the thermic capacity must be a float number")
        if thermicCapacity < 0:
            raise ValueError('thermic capacity must be positive')
        self.__thermicCapacity = thermicCapacity

        typeErrorAtEntering( thermicConductivity, message = "the thermic conductivity must be a float number")
        if thermicConductivity < 0:
            raise ValueError('thermic conductivity must be positive')
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
        typeErrorAtEntering( volumetricMass, message= "the volumetric mass must be a float number")
        if volumetricMass < 0:
            raise ValueError('volumetric mass must be positive')
        self.__volumetricMass = volumetricMass

    @property 
    def dynamicViscosity(self): 
        return self.__dynamicViscosity

    @dynamicViscosity.setter 
    def dynamicViscosity(self,dynamicViscosity): 
        typeErrorAtEntering(dynamicViscosity, message = "the dynamic viscosity must be a float number")
        if dynamicViscosity < 0:
            raise ValueError('dynamic viscosity must be positive')
        self.__dynamicViscosity = dynamicViscosity

    @property 
    def thermicCapacity(self): 
        return self.__thermicCapacity

    @thermicCapacity.setter 
    def thermicCapacity(self,thermicCapacity): 
        typeErrorAtEntering( thermicCapacity, message = "the thermic capacity must be a float number")
        if thermicCapacity < 0:
            raise ValueError('thermic capacity must be positive')
        self.__thermicCapacity = thermicCapacity

    @property 
    def thermicConductivity(self): 
        return self.__thermicConductivity

    @thermicConductivity.setter 
    def thermicConductivity(self,thermicConductivity): 
        typeErrorAtEntering( thermicConductivity, message = "the thermic conductivity must be a float number")
        if thermicConductivity < 0:
            raise ValueError('thermic conductivity must be positive')
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
            self.volumetricMassEvolution = volumetricMassEvolutionDefinition
    
    def dynamicViscosityEvolutionDefinition(self, dependancy):
        def a():
            pass
        if type(dependancy) is not type(a) :
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
            self.dynamicViscosityEvolution = dynamicViscosityEvolutionDefinition

    def thermicCapacityEvolutionDefinition(self, dependancy):
        def a():
            pass
        if type(dependancy) is not type(a) :
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
            self.thermicCapacityEvolution = thermicCapacityEvolutionDefinition

    def thermicConductivityEvolutionDefinition(self, dependancy):
        def a():
            pass
        if type(dependancy) is not type(a) :
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
            self.thermicConductivityEvolution = thermicConductivityEvolutionDefinition

    def volumetricMassEvolution(temperature, pressure, modify = True):
        return None

    def dynamicViscosityEvolution(temperature, pressure, modify = True):
        return None

    def thermicCapacityEvolution(temperature, pressure, modify = True):
        return None

    def thermicConductivityEvolution(temperature, pressure, modify = True):
        return None

    

class SeaWater(Fluid):
    def __init__(self, salinity):
        Fluid.__init__(self, name = "eau de mer")
        if type(salinity) is not float:
                raise TypeError("the salinity must be a float number")
        self.__salinity = salinity

    @property 
    def salinity(self): 
        return self.__salinity

    @salinity.setter 
    def salinity(self,salinity):
        typeErrorAtEntering(self.__salinity, salinity, float, "the salinity must be a float number")
        self.__salinity = salinity

    def volumetricMassEvolutionDefinition(self, dependancy):
        def a():
            pass
        if type(dependancy) is not type(a) :
            raise TypeError("the fluid dependency must be a function")
        else :
            try :
                a = dependancy(temperature = 20, pressure = 10, salinity = 0.2)
            except TypeError :
                raise TypeError("the fluid dependency must be a function of temperature, pressure and salinity")
            def volumetricMassEvolutionDefinition(temperature, pressure, salinity = None, modify = True):
                if salinity == None:
                    salinity = self.salinity
                if modify :
                    self.volumetricMass = dependancy(temperature, pressure, salinity)
                return dependancy(temperature, pressure, salinity)
            self.volumetricMassEvolution = volumetricMassEvolutionDefinition
    
    def dynamicViscosityEvolutionDefinition(self, dependancy):
        def a():
            pass
        if type(dependancy) is not type(a) :
            raise TypeError("the fluid dependency must be a function")
        else :
            try :
                a = dependancy(temperature = 20, pressure = 10, salinity = 0.2)
            except TypeError :
                raise TypeError("the fluid dependency must be a function of temperature, pressure and salinity")
            def dynamicViscosityEvolutionDefinition(temperature, pressure, salinity = None, modify = True):
                if salinity == None:
                    salinity = self.salinity
                if modify :
                    self.dynamicViscosity = dependancy(temperature, pressure, salinity)
                return dependancy(temperature, pressure, salinity)
            self.dynamicViscosityEvolution = dynamicViscosityEvolutionDefinition

    def thermicCapacityEvolutionDefinition(self, dependancy):
        def a():
            pass
        if type(dependancy) is not type(a) :
            raise TypeError("the fluid dependency must be a function")
        else :
            try :
                a = dependancy(temperature = 20, pressure = 10, salinity = 0.2)
            except TypeError :
                raise TypeError("the fluid dependency must be a function of temperature, pressure and salinity")
            def thermicCapacityEvolutionDefinition(temperature, pressure, salinity = None, modify = True):
                if salinity == None:
                    salinity = self.salinity
                if modify :
                    self.thermicCapacity = dependancy(temperature, pressure, salinity)
                return dependancy(temperature, pressure, salinity)
            self.thermicCapacityEvolution = thermicCapacityEvolutionDefinition

    def thermicConductivityEvolutionDefinition(self, dependancy):
        def a():
            pass
        if type(dependancy) is not type(a) :
            raise TypeError("the fluid dependency must be a function")
        else :
            try :
                a = dependancy(temperature = 20, pressure = 10, salinity = 0.2)
            except TypeError :
                raise TypeError("the fluid dependency must be a function of temperature, pressure and salinity")
            def thermicConductivityEvolutionDefinition(temperature, pressure, salinity = None, modify = True):
                if salinity == None:
                    salinity = self.salinity
                if modify :
                    self.thermicConductivity = dependancy(temperature, pressure, salinity)
                return dependancy(temperature, pressure, salinity)
            self.thermicConductivityEvolution = thermicConductivityEvolutionDefinition

    def volumetricMassEvolution(temperature, pressure, salinity = None, modify = True):
        return None

    def dynamicViscosityEvolution(temperature, pressure, salinity = None, modify = True):
        return None

    def thermicCapacityEvolution(temperature, pressure, salinity = None, modify = True):
        return None 

    def thermicConductivityEvolution(temperature, pressure, salinity = None, modify = True):
        return None

    
    
#micro tests
b = 0
def a(b):
    class Solution:
        pass
    solution = Solution()
    solution.temp = b
    return solution


