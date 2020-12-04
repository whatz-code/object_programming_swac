"""The module Fluid allows the user to creat fluid obects and SeaWater objects"""
import sys
sys.path.append(".")
from ExceptionsAndErrors import typeErrorAtEntering

class Fluid:
    """The Fluid class represents the caracteristic of a fluid which
    circulate in any dipole of the circuit

    Attributes:
        name (any): this parameters will be the private attribute name of the function
                        it's here to help the user to define his instances. By default
                        it's water.
        volumetricMass (type:float or :obj:np.float):
            unity : kg/m³
        dynamicViscosity (type:float or :obj:np.float):
            unity : kg/m/s
        thermicCapacity (type:float or :obj:np.float): 
            unity : J/K
        thermicConductivity (type:float or :obj:np.float): This parameter indicates the private attribut thermicConductivity of the 
                                object created from the classe Fluid.
                                unity : W/m/K
        variables(type:list of booleans):
            this parameter gives the knowledge of what variables can be variables with temperature, pressure,
            (and salinity for sea water):
            - variables[0] = True if volumetricMass is variable, else it's false
            - variables[1] = True if dynamicViscosity is variable, else it's false
            - variables[2] = True if thermicCapacity is variable, else it's false
            - variables[3] = True if thermicConductivity is variable, else it's false
    

        """
    #l'initialisation de la classe : 
    def __init__(self, name = 'water', volumetricMass = float(1000), dynamicViscosity = 0.001,
                 thermicCapacity = float(4150), thermicConductivity = 0.6, variables = [False, False, False, False]) : 
        """Class Fluid __init__ method : This allows the user to enter all the attributes of the class. 
                                        the default calues correspond to the state of the water with no
                                        salinity, at the atmospheric pressure and at the temperature of 
                                        20°C.

        Args:
            name (any): this parameters will be the private attribute name of the function
                        it's here to help the user to define his instances. By default
                        it's water.
            volumetricMass (type:float or :obj:np.float): This parameter indicates the private attribute volumetricMass volumetric mass of the 
                                    object created from the classe Fluid. 
                                    unity : kg/m³
            dynamicViscosity (type:float or :obj:np.float): This parameter indicates the private attribute dynamicViscosity of the 
                                    object created from the classe Fluid.
                                    unity : kg/m/s
            thermicCapacity (type:float or :obj:np.float): This parameter indicates the private attribute thermicCapacity of the 
                                    object created from the classe Fluid.
                                    unity : J/K
            thermicConductivity (type:float or :obj:np.float): This parameter indicates the private attribut thermicConductivity of the 
                                    object created from the classe Fluid.
                                    unity : W/m/K
            variables(type:list of booleans):
                                this parameter gives the knowledge of what variables can be variables with temperature, pressure,
                                (and salinity for sea water):
                                - variables[0] = True if volumetricMass is variable, else it's false
                                - variables[1] = True if dynamicViscosity is variable, else it's false
                                - variables[2] = True if thermicCapacity is variable, else it's false
                                - variables[3] = True if thermicConductivity is variable, else it's false
                        
        Raises : 
            TypeError : it's raised by the function typeErrorAtEntering.
            ValueError : it's raises if the variables given haven't any physic reality.

        """
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

        typeErrorAtEntering( variables, Types = [list], Classes = [], message = 'variables must be a list of 4 booleans')
        if len(variables) != 4:
            raise TypeError('variables must be a list of 4 booleans')
        for variable in variables:
            typeErrorAtEntering( variables, Types = [bool], Classes=[], message = 'variables must be a list of 4 booleans')
        self.__thermicConductivity = thermicConductivity

    @property 
    def name(self): 
        """ get method and set method to access the private variable name """
        return self.__name

    @name.setter 
    def name(self,name): 
        self.__name = name   

    @property 
    def volumetricMass(self): 
        """ get method and set method to access the private variable volumetricMass """
        return self.__volumetricMass

    @volumetricMass.setter 
    def volumetricMass(self,volumetricMass):
        typeErrorAtEntering( volumetricMass, message= "the volumetric mass must be a float number")
        if volumetricMass < 0:
            raise ValueError('volumetric mass must be positive')
        self.__volumetricMass = volumetricMass

    @property 
    def dynamicViscosity(self): 
        """ get method and set method to access the private variable dynamicViscosity """
        return self.__dynamicViscosity

    @dynamicViscosity.setter 
    def dynamicViscosity(self,dynamicViscosity): 
        typeErrorAtEntering(dynamicViscosity, message = "the dynamic viscosity must be a float number")
        if dynamicViscosity < 0:
            raise ValueError('dynamic viscosity must be positive')
        self.__dynamicViscosity = dynamicViscosity

    @property 
    def thermicCapacity(self): 
        """ get method and set method to access the private variable thermicCapacity """
        return self.__thermicCapacity

    @thermicCapacity.setter 
    def thermicCapacity(self,thermicCapacity): 
        typeErrorAtEntering( thermicCapacity, message = "the thermic capacity must be a float number")
        if thermicCapacity < 0:
            raise ValueError('thermic capacity must be positive')
        self.__thermicCapacity = thermicCapacity

    @property 
    def thermicConductivity(self): 
        """ get method and set method to access the private variable thermicConductivity """
        return self.__thermicConductivity

    @thermicConductivity.setter 
    def thermicConductivity(self,thermicConductivity): 
        typeErrorAtEntering( thermicConductivity, message = "the thermic conductivity must be a float number")
        if thermicConductivity < 0:
            raise ValueError('thermic conductivity must be positive')
        self.__thermicConductivity = thermicConductivity
    
    @property 
    def variables(self): 
        """ get method and set method to access the private variable variables """
        return self.__variables

    @variables.setter 
    def variables(self,variables): 
        typeErrorAtEntering( variables, Types = [list], Classes = [], message = 'variables must be a list of 4 booleans')
        if len(variables) != 4:
            raise TypeError('variables must be a list of 4 booleans')
        for variable in variable:
            typeErrorAtEntering( variables, Types = [bool], Classes=[], message = 'variables must be a list of 4 booleans')
        self.__variables = variables

    def volumetricMassEvolutionDefinition(self, dependancy):
        """ the method volumetricMassEvolutionDefinition 

        Note: 
                This method allows the class to overload the method volumetricMassEvolution by the 
                function dependancy into argument

        Args:
            dependancy(function): This parameter is a function which has to take into argument the paramaters :
                                temperature(type:float or :obj:np.float) and pressure(type:float or :obj:np.float). 

                        
        Raises: 
            TypeError : If dependancy is not a function.
            TypeError : If the function doesn't take temperature and pressure into argument.


        """
        #verifiying if the dependancy is a function of temperature and pressure
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
                #verifying if the temperature and the pressure are float numbers 
                typeErrorAtEntering( temperature, message= "the temperature must be a float number" )
                typeErrorAtEntering( pressure, message= "the pressure must be a float number" )
                if modify :
                    self.volumetricMass = dependancy(temperature, pressure)
                return dependancy(temperature, pressure)
            self.volumetricMassEvolution = volumetricMassEvolutionDefinition
            self.variables[0] = True
    
    def dynamicViscosityEvolutionDefinition(self, dependancy):
        """ the method dynamicViscosityEvolutionDefinition 

        Note: 
                This method allows the class to overload the method dynamicViscosityEvolution by the 
                function dependancy into argument

        Args:
            dependancy (function): This parameter is a function which has to take into argument the paramaters :
                                temperature and pressure. 

                        
        Raises: 
            TypeError : If dependancy is not a function.
            TypeError : If the function doesn't take temperature and pressure into argument.


        """
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
                typeErrorAtEntering( temperature, message= "the temperature must be a float number" )
                typeErrorAtEntering( pressure, message= "the pressure must be a float number" )
                if modify :
                    self.dynamicViscosity = dependancy(temperature, pressure)
                return dependancy(temperature, pressure)
            self.dynamicViscosityEvolution = dynamicViscosityEvolutionDefinition
            self.variables[1] = True

    def thermicCapacityEvolutionDefinition(self, dependancy):
        """ the method thermicCapacityEvolutionDefinition 

        Note: 
                This method allows the class to overload the method thermicCapacityEvolution by the 
                function dependancy into argument

        Args:
            dependancy (function): This parameter is a function which has to take into argument the paramaters :
                                temperature and pressure. 

                        
        Raises: 
            TypeError : If dependancy is not a function.
            TypeError : If the function doesn't take temperature and pressure into argument.


        """
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
                typeErrorAtEntering( temperature, message= "the temperature must be a float number" )
                typeErrorAtEntering( pressure, message= "the pressure must be a float number" )
                if modify :
                    self.thermicCapacity = dependancy(temperature, pressure)
                return dependancy(temperature, pressure)
            self.thermicCapacityEvolution = thermicCapacityEvolutionDefinition
            self.variables[2] = True

    def thermicConductivityEvolutionDefinition(self, dependancy):
        """ the method thermicConductivityEvolutionDefinition 

        Note: 
                This method allows the class to overload the method thermicConductivityEvolution by the 
                function dependancy into argument

        Args:
            dependancy (function): This parameter is a function which has to take into argument the paramaters :
                                temperature and pressure. 

                        
        Raises: 
            TypeError : If dependancy is not a function.
            TypeError : If the function doesn't take temperature and pressure into argument.


        """
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
                typeErrorAtEntering( temperature, message= "the temperature must be a float number" )
                typeErrorAtEntering( pressure, message= "the pressure must be a float number" )
                if modify :
                    self.thermicConductivity = dependancy(temperature, pressure)
                return dependancy(temperature, pressure)
            self.thermicConductivityEvolution = thermicConductivityEvolutionDefinition
            self.variables[3] = True

    def volumetricMassEvolution(self, temperature, pressure, modify = True):
        """ the method volumericMassEvolution 

        Note: 
            This method gives the volumetricMassEvolution at a given temperature and pressure.
            It can modify the volumetricMass attribute if the argument modify is True.

        Args:
            modify (boolean): Allows the method to modify the volumetricMass attribute
            temperature (float): Argument to calcul the volumetricMass.
                                unity : °C
            pressure(float): Argument to calcul the volumetricMass.
                                unity : Pascal
        
        Returns:
            If the methods has been overloaded : volumetricMass in kg/m³ 
            If not, the method is undefined : return None by convention
                        
        Raises: 
            TypeError : If the parameters or not in the type accepted by the method


        """
        return self.volumetricMass

    def dynamicViscosityEvolution(self, temperature, pressure, modify = True):
        """ the method dynamicViscosityEvolution 

        Note: 
            This method gives the dynamicViscosityEvolution at a given temperature and pressure.
            It can modify the dynamicViscosity attribute if the argument modify is True.

        Args:
            modify (boolean): Allows the method to modify the dynamicViscosity attribute
            temperature (float): Argument to calcul the dynamicViscosity.
                                unity : °C
            pressure(float): Argument to calcul the dynamicViscosity.
                                unity : Pascal
        
        Returns:
            If the methods has been overloaded : dynamicViscosity in kg/m/s
            If not, the method is undefined : return None by convention
                        
        Raises: 
            TypeError : If the parameters or not in the type accepted by the method


        """
        return self.dynamicViscosity

    def thermicCapacityEvolution(self, temperature, pressure, modify = True):
        """ the method thermicCapacityEvolution 

        Note: 
            This method gives the thermicCapacityEvolution at a given temperature and pressure.
            It can modify the thermicCapacity attribute if the argument modify is True.

        Args:
            modify (boolean): Allows the method to modify the thermicCapacity attribute
            temperature (float): Argument to calcul the thermicCapacity.
                                unity : °C
            pressure(float): Argument to calcul the thermicCapacity.
                                unity : Pascal
        
        Returns:
            If the methods has been overloaded : thermicCapacity in J/KS
            If not, the method is undefined : return None by convention
                        
        Raises: 
            TypeError : If the parameters or not in the type accepted by the method


        """
        return self.thermicCapacity

    def thermicConductivityEvolution(self, temperature, pressure, modify = True):
        """ the method thermicConductivityEvolution 

        Note: 
            This method gives the thermicConductivityEvolution at a given temperature and pressure.
            It can modify the thermicConductivity attribute if the argument modify is True.

        Args:
            modify (boolean): Allows the method to modify the thermicConductivity attribute
            temperature (float): Argument to calcul the thermicConductivity.
                                unity : °C
            pressure(float): Argument to calcul the thermicConductivity.
                                unity : Pascal
        
        Returns:
            If the methods has been overloaded : thermicConductivity in W/m/K
            If not, the method is undefined : return None by convention
                        
        Raises: 
            TypeError : If the parameters or not in the type accepted by the method


        """
        return self.thermicConductivity

class SeaWater(Fluid):
    """The seaWater class represents the caracteristic of a sea Water fluid.

    Attributes:
        salinity (type:float or :obj:np.float64):
            Unity : g/kg
                 
    

        """
    def __init__(self, name = 'water', volumetricMass = float(1000), dynamicViscosity = 0.001, 
                thermicCapacity = float(4150), thermicConductivity = 0.6, salinity = 0.0):
        """Class SeaWater __init__ method :
        
        Note:
            The class SeaWater is a child class of the class Fluid which
            takes also the salinity as an attribute.

            __init__ method : It allows the user to enter all the attributes of the class. 
            the default calues correspond to the state of the water with no
            salinity, at the atmospheric pressure and at the temperature of 
            20°C.

        Args:
            name (any): this parameters will be the private attribute name of the function
                        it's here to help the user to define his instances. By default
                        it's water.
            volumetricMass (type:float or :obj:np.float64): This parameter indicates the private attribute volumetricMass volumetric mass of the 
                                    object created from the classe Fluid. 
                                    unity : kg/m³
            dynamicViscosity (type:float or :obj:np.float64): This parameter indicates the private attribute dynamicViscosity of the 
                                    object created from the classe Fluid.
                                    unity : kg/m/s
            thermicCapacity (type:float or :obj:np.float64): This parameter indicates the private attribute thermicCapacity of the 
                                    object created from the classe Fluid.
                                    unity : J/K
            thermicConductivity (type:float or :obj:np.float64): This parameter indicates the private attribute thermicConductivity of the 
                                    object created from the classe Fluid.
                                    unity : W/m/K
            salinity (type:float or :obj:np.float64): 
                This parameter indicates the private attribute salinity of 
                the object created from the class Fluid.
                Unity : g/kg
                        
        Raises : 
            TypeError : it's raised by the function typeErrorAtEntering.
            ValueError : it's raises if the variables given haven't any physic reality.

        """
        Fluid.__init__(self, name = "eau de mer")
        typeErrorAtEntering( volumetricMass, message= "the salinity must be a float number")
        self.__salinity = salinity

    @property 
    def salinity(self): 
        """ get method and set method to access the private variable dynamicViscosity """
        return self.__salinity

    @salinity.setter 
    def salinity(self,salinity):
        typeErrorAtEntering(self.__salinity, salinity, float, "the salinity must be a float number")
        self.__salinity = salinity

    def volumetricMassEvolutionDefinition(self, dependancy):
        """ overloading of the methode of the class fluid by adding 
            the argument salinity in the function 
        """
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
            self.variables[0] = True

    def dynamicViscosityEvolutionDefinition(self, dependancy):
        """ overloading of the methode of the class fluid by adding 
            the argument salinity in the function 
        """
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
            self.variables[1] = True

    def thermicCapacityEvolutionDefinition(self, dependancy):
        """ overloading of the methode of the class fluid by adding 
            the argument salinity in the function 
        """
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
            self.variables[2] = True

    def thermicConductivityEvolutionDefinition(self, dependancy):
        """ overloading of the methode of the class fluid by adding 
            the argument salinity in the function 
        """
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
            self.variables[3] = True

    def volumetricMassEvolution(self, temperature, pressure, salinity = None, modify = True):
        """ overloading of the methode of the class fluid by adding 
            the argument salinity in the function 
        """
        return self.volumetricMass

    def dynamicViscosityEvolution(self, temperature, pressure, salinity = None, modify = True):
        """ overloading of the methode of the class fluid by adding 
            the argument salinity in the function 
        """
        return self.dynamicViscosity

    def thermicCapacityEvolution(self, temperature, pressure, salinity = None, modify = True):
        """ overloading of the methode of the class fluid by adding 
            the argument salinity in the function 
        """
        return self.thermicCapacity 

    def thermicConductivityEvolution(self, temperature, pressure, salinity = None, modify = True):
        """ overloading of the methode of the class fluid by adding 
            the argument salinity in the function 
        """
        return self.thermicConductivity

    