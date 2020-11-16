

class Fluid:
    #l'initialisation de la classe : 
    def __init__(self,name = 'eau',voluminalMass = 1000,dynamicViscosity = 0.001,thermicCapacity = 4150,thermicConductivity = 0.6) : 
        self.__name = name
        self.__voluminalMass = voluminalMass
        self.__dynamicViscosity = dynamicViscosity
        self.__thermicCapacity = thermicCapacity
        self.__thermicConductivity = thermicConductivity

    @property 
    def name(self): 
        return self.__name

    @name.setter 
    def name(self,name): 
        self.__name = name

    @property 
    def voluminalMass(self): 
        return self.__voluminalMass

    @voluminalMass.setter 
    def voluminalMass(self,voluminalMass): 
        self.__voluminalMass = voluminalMass

    @property 
    def dynamicViscosity(self): 
        return self.__dynamicViscosity

    @dynamicViscosity.setter 
    def dynamicViscosity(self,dynamicViscosity): 
        self.__dynamicViscosity = dynamicViscosity

    @property 
    def thermicCapacity(self): 
        return self.__thermicCapacity

    @thermicCapacity.setter 
    def thermicCapacity(self,thermicCapacity): 
        self.__thermicCapacity = thermicCapacity

    @property 
    def thermicConductivity(self): 
        return self.__thermicConductivity

    @thermicConductivity.setter 
    def thermicConductivity(self,thermicConductivity): 
        self.__thermicConductivity = thermicConductivity



#test
fluid = Fluid()
print(fluid.thermicCapacity)