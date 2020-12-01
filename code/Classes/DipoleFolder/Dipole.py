""" Into the module dipole are created the classes : 
        - Pole
        - Dipole
        - Pipe
        - PlateHeatExchangerSide
        - Ideal Pump
        - Pump
 """
from math import log
from math import pi 
from math import log10
from math import cos
from math import sin
from math import tan
import matplotlib.pyplot as plt
import sys
sys.path.append("./Classes")
sys.path.append(".")
import numpy as np
from FlowFolder.Flow import Flow
from GraphFolder.Graphe import Edge, Node
from Calculus import Resolve
from HydraulicThermicCalculus import HydraulicThermicCalculus
from FluidFolder.Fluid import Fluid
from Calculus import DataAnalysis
from ExceptionsAndErrors import typeErrorAtEntering

eau = Fluid()

class Pole(Node):
    def __init__(self,name = None, pressure = None, temperature = None, successors = [], fluid = Fluid()) : 
        """Class Pole __init__ method : 
        
        Note : 
            The Pole class is used to give the ponctual state of the flow between various dipoles.
            It's a child of the Node class and so has a important role to play for the definition
            of the topology of the hydraulic and thermic network. 
            the __init__ method offers the opportunity to give the attributes of the Pole object.

        Args:
            pressure (type:float,Nonetype or :obj:np.float64): This parameter indicates the private attribute pressure of the 
                                    object created from the classe Pole. It represents the pressures between dipoles which are
                                    associated with the pole object as an attribute.
                                    unity : Pascal.
            temperature (type:float,Nonetype or :obj:np.float64): This parameter indicates the private attribute temperature
                                    of the object created from the classe Pole. It represents the pressures between dipoles which are
                                    associated with the pole object as an attribute.
                                    unity : °C
            successors (type:list of :obj:Pole): This parameter indicates the private attribute successors of the 
                                    object created from the parent class Node. It represents the other poles linked
                                    by a dipole where the pole object is the downstream attribute.
            fluid(:obj: Fluid): This parameter indicates the private attribute fluid of the obkect created from the class Flow. It represents
                                the fluid which flows between the dipoles the pole object is associated with as an attribtute.
                                    
                        
        Raises : 
            TypeError : It's raised by the function typeErrorAtEntering when the types and the object
                    don't match with the type and the object defined.

        """
        Node.__init__(self, name = name, successors = successors)

        typeErrorAtEntering(pressure,Types = [float, type(None)], message = "the pressure must be a float or a None type")
        self.__pressure = pressure

        typeErrorAtEntering(temperature,Types = [float, type(None)], message = "the temperature must be a float or a None type")
        self.__temperature = temperature

        typeErrorAtEntering(flowRate,Types = [], Classes = [Fluid], message = "the fluid must be a Fluid object")
        self.__fluid = fluid

    @property 
    def pressure(self): 
        """ get method and set method to access the private variable pressure """
        return self.__pressure

    @pressure.setter 
    def pressure(self,pressure): 
        typeErrorAtEntering(pressure,Types = [float, type(None)], message = "the pressure must be a float or a None type")
        self.__pressure = pressure
    
    @property 
    def temperature(self): 
        """ get method and set method to access the private variable temperature """
        return self.__temperature

    @temperature.setter 
    def temperature(self,temperature): 
        typeErrorAtEntering(temperature,Types = [float, type(None)], message = "the temperature must be a float or a None type")
        self.__temperature = temperature

    @property 
    def fluid(self): 
        """ get method and set method to access the private variable fluid """
        return self.__fluid

    @fluid.setter 
    def fluid(self,fluid): 
        typeErrorAtEntering(flowRate,Types = [], instances = [Fluid], message = "the fluid must be a Fluid object")
        self.__fluid = fluid

class Dipole(Edge):
    #l'initialisation de la classe : 
    def __init__(self, name = 'Dipole', hydraulicDiameter = None, crossSectionalArea = None, downstreamPole = Pole('downstream pole'),
                    upstreamPole = Pole('upstream Pole'), flow = Flow(), variables = [False, False, False, False], 
                    caracteristics = [False, False], exchanger = False) : 
        """Class Dipole __init__ method : 
        
        Note : 
            The Dipole class is used to represent the caracteristic of a region where a flow object 
            flows from one pole where an other pole. It represents for example the geometry of the 
            region, and how the region can affect the flow, for examples :
                - by giving are taking pressure
                - by increasing his temperature or decreasing his temperature (giving thermic power or
                taking thermic power)
                - by fixing the flow rate of the flow
                - ...

            the __init__ method offers the opportunity to give the attributes of the dipole object.

        Args:
            name( type:any ): 
                this parameters indicates the private attribute name. This parameter gives 
                        the user the opportunity to organise his dipole objects.

            hydraulicDiameter (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute hydraulicDiameter of the 
                dipole object created from the class Dipole. 
                It represents the caracteristical length in the dipole to computes the 
                reynolds or other important numbers.
                unity : m

            crossSectionnalArea (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute crossSectionalArea of the object 
                created from the Dipole class. 
                It represents the sectionnal area of the flow, it's an important parameter to compute 
                the average velocity of the fluid into the dipole.
                unity : m²

            downstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[0] of the 
                object created from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid enters into the dipole (or the
                dipole entry). By default all the states attributes of the object downstreamPole 
                are undefined (with the None variable).

            upstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[1] of the 
                object created from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid exits the dipole (or the
                dipole outlet). By default all the states attributes of the object 
                upstreamPole are undefined (with the None variable).

            flow(:obj: Flow): 
                This parameter indicates the private attribute flow of the object created from 
                the class Dipole. 
                It represents the state of the flow of the dipole. By default all the states
                attributes of the object flow are undefined (with the None variable).

            variables(type:list of 4 booleans):
                This parameter indicates the private attribute variables of the object created from 
                the class Dipole.    
                It gives the knowledge of how the variables of the flow can be calculated : 
                    - if variables[0] == False : the flow rate is fixed (so flowRate is a variable of the system)
                    - if variables[1] == False : the difference of pressure is fixed
                    - if variables[2] == False : the input temperature is fixed
                    - if variables[3] == False : the outlet temperature is fixed      

                This attribute is usefull to reduce the unknown variables in the system which has to be 
                resolved to know the functionnement hydraulic and thermic of the networks

            caracteristics(type:list of 2 booleans):
                This parameter indicate the private attribut caracteristics of the object created from
                the class Dipole.
                It gives the knowledge of what caracteristics are defined :
                    - if caracteristics[0] = False : the method hydraulicCaracteristic is not defined (True : is defined)
                    - if caracteristics[1] = False : the method hydraulicCaracteristic is not defined (True : is defined)
            
            exchanger(type:boolean):
                this paramete indicate the private attribute exchanger of the object created from the class
                exchanger.
                It gives the knowledge : 
                    - if the dipole is a part of an exchanger : True, else : False

        Raises : 
            TypeError : 
                It's raised by the function typeErrorAtEntering when the Types and the object
                don't match with the type and the object defined.
            ValueError: 
                If the variables haven't the physical reality, example : hydraulicDiameter < 0

        """
        self.__name = name

        #Edge is initialised with Poles[0] = downstreamPole and Poles[1] = upstreamPole
        typeErrorAtEntering(downstreamPole,Types = [], Classes = [Pole], message = "the downstreamPole must be an instance of the class Pole")
        typeErrorAtEntering(upstreamPole,Types = [], Classes = [Pole], message = "the upstreamPole must be an instance of the class Pole")
        Edge.__init__(self, name, [downstreamPole, upstreamPole])
        
        typeErrorAtEntering(flow,Types = [], Classes = [Flow], message = "the flow must be an instance of the class Flow")
        self.__flow = flow

        typeErrorAtEntering(hydraulicDiameter, message = "the hydraulic diameter must be a float number")
        if type(hydraulicDiameter) is not type(None):
            if hydraulicDiameter <= 0:
                raise ValueError('hydraulic diameter must be strictly positive')
        self.__hydraulicDiameter = hydraulicDiameter

        typeErrorAtEntering(crossSectionalArea, message = "the cross sectionnal area must be a float number")
        if type(crossSectionalArea) is not type(None):
            if crossSectionalArea <= 0:
                raise ValueError('cross sectionnal area must be strictly positive')
        self.__crossSectionalArea = crossSectionalArea

        typeErrorAtEntering(variables, Types = list, message = "the variables must be a list of 4 booleans")
        if len(variables) != 5:
            raise TypeError("the variables must be a list of 5 booleans")
        for variable in variables :
            if type(variable) is not bool: 
                raise TypeError("the variables must be a list of 5 booleans")
        self.__variables = variables

        typeErrorAtEntering(caracteristics, Types = list, message = "the caracteristics must be a list of 2 booleans")
        if len(caracteristics) != 2:
            raise TypeError("the caracteristics must be a list of 2 booleans")
        for variable in caracteristics :
            if type(variable) is not bool: 
                raise TypeError("the caracteristics must be a list of 2 booleans")
        self.__caracteristics = caracteristics

        typeErrorAtEntering(exchanger, Types = bool, message = "the variables must be a boolean")
        self.__echanger = echanger

    @property 
    def name(self): 
        """ get method and set method to access the private variable name """
        return self.__name

    @name.setter 
    def name(self,name): 
        self.__name = name

    @property 
    def hydraulicDiameter(self):
        """ get method and set method to access the private variable flowRate """
        return self.__hydraulicDiameter

    @hydraulicDiameter.setter 
    def hydraulicDiameter(self,hydraulicDiameter):
        typeErrorAtEntering(hydraulicDiameter, message = "the hydraulic diameter must be a float number")
        if type(hydraulicDiameter) is not type(None):
            if hydraulicDiameter <= 0:
                raise ValueError('hydraulic diameter must be strictly positive')
        self.__hydraulicDiameter = hydraulicDiameter

    @property 
    def crossSectionalArea(self): 
        """ get method and set method to access the private variable crossSectionnalArea """
        return self.__crossSectionalArea

    @crossSectionalArea.setter 
    def crossSectionalArea(self,crossSectionalArea): 
        typeErrorAtEntering(crossSectionalArea, message = "the cross sectionnal area must be a float number")
        if type(crossSectionalArea) is not type(None):
            if crossSectionalArea <= 0:
                raise ValueError('cross sectionnal area must be strictly positive')
        self.__crossSectionalArea = crossSectionalArea
    
    @property 
    def flow(self): 
        """ get method and set method to access the private variable flow """
        return self.__flow

    @flow.setter 
    def flow(self,flow): 
        typeErrorAtEntering(flow,Types = [], Classes = [Flow], message = "the flow must be an instance of the class Flow")
        self.__flow = flow

    @property 
    def downstreamPole(self):
        """ get method and set method to access the private variable downstreamPole """ 
        return self.nodes[0]

    @downstreamPole.setter 
    def downstreamPole(self,downstreamPole): 
        typeErrorAtEntering(downstreamPole,Types = [], Classes = [Pole], message = "the downstreamPole must be an instance of the class Pole")
        self.nodes[0] = downstreamPole
    
    @property 
    def upstreamPole(self): 
        """ get method and set method to access the private variable upstreamPole """
        return self.nodes[1]

    @upstreamPole.setter 
    def upstreamPole(self,upstreamPole): 
        typeErrorAtEntering(upstreamPole,Types = [], Classes = [Pole], message = "the upstreamPole must be an instance of the class Pole")
        self.nodes[1] = upstreamPole

    @property 
    def variables(self): 
        """ get method and set method to access the private variable variables """
        return self.__variables

    @variables.setter 
    def variables(self,variables): 
        typeErrorAtEntering(variables, Types = list, message = "the variables must be a list of 5 booleans")
        if len(variables) != 5:
            raise TypeError("the variables must be a list of 5 booleans")
        for variable in variables :
            if type(variable) is not bool: 
                raise TypeError("the variables must be a list of 5 booleans")
        self.__variables = variables
    

    def hydraulicCorrelation(self, reynoldsNumber) :
        """ the method hydraulicCorrelation 

        Note: 
            When this method is defined, it take into account the caracteristics
            of the object created from the class Dipole and the reynolds number of 
            the flow to give head loss coefficient of the formula :
            Delta P = headLossCoefficient * volumetricMass * 1/2 * v ** 2
            with  :
                - Delta P the pressure head loss
                - headLossCoefficient the head loss coefficient
                - volumetricMass the volumetric Mass
                - v the average velocity of the flow
        Args:
            reynoldsNumber(type:float):
                It corresponds to the Reynolds number which combines the
                importants information of the flow and the dipole.

        Returns:
            headLossCoefficient(type:float) when the method is defined 
            None when the method is not defined
                        
        Raises: 
            TypeError : If reynoldsNumber is not a float


        """
        typeErrorAtEntering( reynoldsNumber, message = "the reynolds number must be a float number")
        return None

    def hydraulicCaracteristic(self, flowRate = None, fluid = None) :
        """ the method hydraulicCaracteristic 

        Note: 
            When this method is defined, it take into account the hydraulicCaracteristics
            of the object created from the class Dipole and the flow rate and the 
            fluid to compute the difference of pressure between the outlet and the
            inlet of the dipole. 
            This hydraulicCaracteristic can be deduced from the hydraulic correlation, if it's
            defined.
        Args:
            flowRate(type:float or None type):
                If the flowRate is equal to None, the flowRate use for the calcul
                is the flowRate from the flow object attribute.
                unity:m³/s
            fluid(:obj: Fluid, type:None type):
                If the fluid is equal to None, the fluid taken into account
                is the fluid from the flow object attribute.

        Returns:
            pressureDifference(type:float)
            None when the method is not defined
                        
        Raises: 
            TypeError : If flowRate is not a float 
            TypeError : If fluid is not a Fluid object


        """
        if flowRate == None:
            flowRate = self.flow.flowRate
        if fluid == None:
            fluid = self.flow.fluid

        typeErrorAtEntering( flowRate, message = "the flow rate must be a float number")
        typeErrorAtEntering( fluid, Types = [], Classes = [Fluid],  message = "the fluid must be a fluid object")

        return None

    def thermicCorrelation(self, reynoldsNumber, prandtlNumber):
        """ the method thermicCorrelation 

        Note: 
            When this method is defined, it take into account the caracteristics
            of the object created from the class Dipole, the reynolds number and
            the prandtl number to give the Nusselt number

        Args:
            reynoldsNumber(type:float):
                It corresponds to the Reynolds number which combines the
                importants information of the flow and the dipole.
            prandtlNumber(type:float):
                It corresponds to the prandtl number which is the ratio 
                between the momentum diffusivity and the thermal diffusivity :
                prantlNumber = thermicCapacity * dynamixViscosity / thermicConductivity

        Returns:
            NusseltNumber(type:float) when the method is defined 
            None when the method is not defined
                        
        Raises: 
            TypeError : If reynoldsNumber or prandtl number are not a float


        """
        typeErrorAtEntering( reynoldsNumber, message = "the Reynolds number must be a float number")
        typeErrorAtEntering( prandtlNumber, message = "the Prandtl number must be a float number")
        return None
    
    def thermicCaracteristic(self, flowRate = None, fluid = None):
        """ the method thermicCaracteristic 

        Note: 
            When this method is defined, it take into account the caracteristics
            of the object created from the class Dipole, the flow rate and the 
            fluid to compute the thermal power given to the fluid.
        Args:
            flowRate(type:float or None type):
                If the flowRate is equal to None, the flowRate use for the calcul
                is the flowRate from the flow object attribute.
                unity:m³/s
            fluid(:obj: Fluid, type:None type):
                If the fluid is equal to None, the fluid taken into account
                is the fluid from the flow object attribute.

        Returns:
            thermalPower(type:float)
            None when the method is not defined
                        
        Raises: 
            TypeError : If flowRate is not a float 
            TypeError : If fluid is not a Fluid object


        """
        typeErrorAtEntering( flowRate, message = "the flow rate must be a float number")
        typeErrorAtEntering( fluid, Types = [], Classes = [Fluid], message = "the fluid must be a fluid object")

        return None

class Pipe(Dipole):
    
    def __init__(self,name = 'Pipe', hydraulicDiameter = 0.348, rugosity = 0.0001, length = 50.0,
                    downstreamPole = Pole('downstream pole'), upstreamPole = Pole('upstream Pole'), 
                    flow = Flow(), variables = [True, True, True, True], caracteristics = [True, True], 
                    exchanger = False) : 
        """Class Pipe __init__ method : 
        
        Note : 
            The Pipe class is a child of the Dipole class. It represents pipes in a hydraulic network.
            the __init__ method offers the opportunity to give the attributes of the Pipe object.

        Args:
            name( type:any ): 
                this parameters indicates the private attribute name. This parameter gives 
                        the user the opportunity to organise his dipole objects.

            hydraulicDiameter (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute hydraulicDiameter of the 
                dipole object created from the class Dipole. 
                It represents the caracteristical length in the dipole to computes the 
                reynolds or other important numbers.
                By default the hydraulicDiameter is fixed to 0.348 m because it's an hydraulic
                diameter that exists in reality.
                unity : m
            
            rugosity(type:float): 
                This parameter indicates the private attribute flow of the object created from 
                the class Pipe. 
                It represents the surface roughness of the pipe.
                By default it's fixed to 0.0001 m because it's a good order of magnitude
                unity:m
            
            length(type:float): 
                This parameter indicates the private attribute length of the object created from 
                the class Pipe. 
                It represents the length of the pipe.
                By default it's 50 m but it should be any other length while it's far superior to
                the hydraulicDiameter.
                unity:m

            downstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[0] of the 
                object created from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid enters into the dipole (or the
                dipole entry). By default all the states attributes of the object downstreamPole 
                are undefined (with the None variable).

            upstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[1] of the 
                object created from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid exits the dipole (or the
                dipole outlet). By default all the states attributes of the object 
                upstreamPole are undefined (with the None variable).

            flow(:obj: Flow): 
                This parameter indicates the private attribute flow of the object created from 
                the class Dipole. 
                It represents the state of the flow of the dipole. By default all the states
                attributes of the object flow are undefined (with the None variable).

            variables(type:list of booleans):
                This argument is described in the documentation of the class Dipole.
                By default it's fixed to [True, True, True, True] because all the 
                parameter are variable for the majority of case.
            
            caracteristics(type:list of booleans):
                This argument is described in the documentation of the class Dipole.
                By default it's fixed to [True, True] because the pipe have an
                hydraulic caracteristic and for the majority of cases the pipe
                have also a thermicCaracteristic which corresponds to the elevation
                of temperature of the fluid induced by the friction with the surface 
                roughness of the pipe.
            
            exchanger(type:boolean):
                This argument is described in the documentation of the class Dipole.
                By default it's fixed to False because it could be considered, for
                the majority of case that the wall pipe is adiabatic. 
                But it could also be in a exchanger system. 


            Note:
                - the cross sectionnal area can be calculated from the hydralic diameter of the pipe
                - variables of the Dipole is fixed to [True, True, False, False]

                        
        Raises : 
            TypeError : 
                It's raised by the function typeErrorAtEntering when the Types and the object
                don't match with the type and the object defined.
            ValueError: 
                If the variables haven't the physical reality, example : hydraulicDiameter < 0

        """
        Dipole.__init__(self, name, hydraulicDiameter, hydraulicDiameter**2*pi/4,
                        downstreamPole, upstreamPole, flow, variables = variables, 
                        caracteristics = caracteristics, exchanger = exchanger)

        typeErrorAtEntering(rugosity, message = "the rugosity must be a float number")
        if type(rugosity) is not type(None):
            if rugosity < 0:
                raise ValueError('rugosity must be positive')
        
        typeErrorAtEntering(length, message = "the length must be a float number")
        if type(length) is not type(None):
            if length < 0:
                raise ValueError('length must be positive')

        self.__rugosity = rugosity
        self.__length = length
    
    @property 
    def rugosity(self): 
        """ get and set allows the user to modify the private rugosity attribute """
        return self.__rugosity

    @rugosity.setter 
    def rugosity(self,rugosity): 
        typeErrorAtEntering(rugosity, message = "the rugosity must be a float number")
        if type(rugosity) is not type(None):
            if rugosity < 0:
                raise ValueError('rugosity must be positive')
        self.__rugosity = rugosity

    @property 
    def length(self): 
        """ get and set allows the user to modify the private length attribute """
        return self.__length

    @length.setter 
    def length(self,length): 
        typeErrorAtEntering(length, message = "the length must be a float number")
        if type(length) is not type(None):
            if length < 0:
                raise ValueError('length must be positive')
        self.__length = length

    def hydraulicCorrelation(self, reynoldsNumber, length = None, hydraulicDiameter = None, rugosity = None):
        """ the method hydraulicCorrelation 

        Note: 
            When this method is defined, it take into account the caracteristics
            of the object created from the class Dipole and the reynolds number of 
            the flow to give head loss coefficient of the formula :
            Delta P = headLossCoefficient * volumetricMass * 1/2 * v ** 2
            with  :
                - Delta P the pressure head loss
                - headLossCoefficient the head loss coefficient
                - volumetricMass the volumetric Mass
                - v the average velocity of the flow
        Args:
            reynoldsNumber(type:float):
                It corresponds to the Reynolds number which combines the
                importants information of the flow and the dipole.
            hydraulicDiameter(type:float or None type):
                If the hydraulicDiameter is equal to None, then the hydraulicDiameter
                taken into account is taken from the dipole object.
                unity: m
            rugosity(type:float or None type):
                If the rugosity is equal to None, then the rugosity
                taken into account is taken from the dipole object.
                unity: m

        Returns:
            headLossCoefficient(type:float)
                        
        Raises: 
            TypeError : If reynoldsNumber is not a float


        """
        #takes the intern paramaters if there are not defined in the arguments
        if length == None :
            length = self.length
        if hydraulicDiameter == None :
            hydraulicDiameter = self.hydraulicDiameter
        if rugosity == None :
            rugosity = self.rugosity
        
        #tests to raise exceptions
        typeErrorAtEntering(reynoldsNumber, message = "the reynoldsNumber must be a float number")
        if reynoldsNumber <= 0:
            raise ValueError('the reynolds number must be a strictly positive float')

        typeErrorAtEntering(rugosity, message = "the rugosity must be a float number")
        if rugosity < 0:
            raise ValueError('rugosity must be positive')

        typeErrorAtEntering(length, message = "the length must be a float number")
        if length < 0:
            raise ValueError('length must be positive')

        typeErrorAtEntering(hydraulicDiameter, message = "the hydraulic diameter must be a float number")
        if length <=0 :
            raise ValueError('hydraulic diameter must be a strictyly positive float number')

        def laminar(reynoldsNumber):
            """ calcul of the regular head loss coefficient if the flow is laminar """
            if reynoldsNumber > 0 :
                return 64 / reynoldsNumber
            else :
                raise ValueError("the reynolds number must be strictly positive")
        
        def turbulent(reynoldsNumber, rugosity, hydraulicDiameter):
            """ calcul of the regular head loss coefficient if the flow is turbulent """

            Inconnue0 = 100 
            def g(Inconnue):
                """ 
                definition of the fixed point function : x = g(x) with x = 1 / sqrt(lambda)
                with lambda the regular head loss coefficient 
                """
                return -2 * log10(2.51 / reynoldsNumber * Inconnue + rugosity / (3.7 * hydraulicDiameter))
            
            #resolution of the equation by using the static function of the class Resolve from the module Calculus
            Inconnue = Resolve.fixePointResolution(g, Inconnue0) 
            #calcul of the coefficient 
            headLossCoefficient = 1 / Inconnue ** 2
            return headLossCoefficient
        
        #it's considered that the flow is laminar if the reynolds number is higher than 2000 and
        #turbulent if the reynolds number is higher than 4000, between the 2 limits it's the 
        #average balanced by the distance of the limits 
        if reynoldsNumber < 2000 :
            return laminar(reynoldsNumber) * length / hydraulicDiameter

        if reynoldsNumber >= 2000 and reynoldsNumber <=4000 :
            coefficient = (reynoldsNumber - 2000)/2000
            return (1-coefficient) * laminar(reynoldsNumber) * length / hydraulicDiameter + coefficient * turbulent(reynoldsNumber,rugosity,hydraulicDiameter) * length / hydraulicDiameter

        if reynoldsNumber > 4000:
            return turbulent(reynoldsNumber,rugosity,hydraulicDiameter) * length / hydraulicDiameter

    def hydraulicCaracteristic(self, flowRate = None, fluid = None, flowRateUnity = "m3/s", pressureUnity = "Pa"):
        """ the method hydraulicCaracteristic 

        Note: 
            When this method is defined, it take into account the hydraulicCaracteristics
            of the object created from the class Dipole and the flow rate and the 
            fluid to compute the difference of pressure between the outlet and the
            inlet of the dipole. 
            This hydraulicCaracteristic can be deduced from the hydraulic correlation, if it's
            defined.
        Args:
            flowRate(type:float or None type):
                If the flowRate is equal to None, the flowRate use for the calcul
                is the flowRate from the flow object attribute.
                unity: defined by flowRateUnity
            fluid(:obj: Fluid, type:None type):
                If the fluid is equal to None, the fluid taken into account
                is the fluid from the flow object attribute.
            flowRateUnity(type:str):
                flowRateUnity can be equal to "m3/s" or "m3/h"
                pressureUnity can be equal to "Pa", "bar", "mCE"

        Returns:
            pressureDifference(type:float)
                unity:defined by pressureUnity
            None when the method is not defined
                        
        Raises: 
            TypeError : If flowRate is not a float 
            TypeError : If fluid is not a Fluid object


        """
        #takes the intern variables if undefined
        if flowRate == None:
            flowRate = self.flow.flowRate
        if fluid == None:
            fluid = self.flow.fluid

        typeErrorAtEntering( flowRate, message = "the flow rate must be a float number")
        typeErrorAtEntering( flowRate, Types = [], Classes = [Fluid], message = "the fluid must be a fluid object")

        return - HydraulicThermicCalculus.caracteristic(self, flowRate, fluid, flowRateUnity, pressureUnity)
    
    def thermicCaracteristic(self, flowRate = None, fluid = None):
        """ the method thermicCaracteristic 

        Note: 
            When this method is defined, it take into account the caracteristics
            of the object created from the class Dipole, the flow rate and the 
            fluid to compute the thermal power given to the fluid.
        Args:
            flowRate(type:float or None type):
                If the flowRate is equal to None, the flowRate use for the calcul
                is the flowRate from the flow object attribute.
                unity:m³/s
            fluid(:obj: Fluid, type:None type):
                If the fluid is equal to None, the fluid taken into account
                is the fluid from the flow object attribute.

        Returns:
            thermalPower(type:float)
            None when the method is not defined
                        
        Raises: 
            TypeError : If flowRate is not a float 
            TypeError : If fluid is not a Fluid object


        """
        #takes the intern variables if undefined
        if flowRate == None:
            flowRate = self.flow.flowRate
        if fluid == None:
            fluid = self.flow.fluid
        
        typeErrorAtEntering( flowRate, message = "the flow rate must be a float number")
        typeErrorAtEntering( fluid, Types = [], Classes = [Fluid], message = "the fluid must be a fluid object")
        thermalPower =  - flowRate * self.hydraulicCaracteristic(flowRate = flowRate, fluid = fluid)

        return thermalPower

                      
class PlateHeatExchangerSide(Dipole):
    def __init__(self, name = 'Plate Heat-exchanger side',width = None, plateGap = None, streakWaveLength = None,
                 plateNumber = None, angle = None, length = None, Npasse = 1, hydraulicCorrectingFactor = 1.0, 
                 thermicCorrectingFactor = 1.0, downstreamPole = Pole('downstream pole'), upstreamPole = Pole('upstream Pole'), 
                 flow = Flow(), variables = [True, True, False, False]) : 
        """Class PlateHeatExchangerSide __init__ method : 
        
        Note : 
            The PlateHeatExchangerSide class is a child of the Dipole class. It represents one
            of the 2 sides of an hydraulic diameter.
            the __init__ method offers the opportunity to give the attributes of the Pipe object.

        Args:
            name( type:any ): 
                this parameters indicates the private attribute name. This parameter gives 
                        the user the opportunity to organise his dipole objects.

            width (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute width of the 
                plateHeatExchangerSide object created from the class PlateHeatExchangerSide. 
                It represents the caracteristical width of the exchanger.
                unity : m
            
            plateGap(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute plateGape of the object created from 
                the class PlateHeatExchangerSide. 
                unity:mm
            
            streakWaveLength(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute streakWaveLength of the object created from 
                the class PlateHeatExchangerSide. 
                It represents the Wave length of the relief of the heat echanger plates
                unIy:mm
            
            plateNumber(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute plateNumber of the object created from 
                the class PlateHeatExchangerSide. 
                It represents the number of plates of the heat exchanger
            
            angle(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute angle of the object created from 
                the class PlateHeatExchangerSide. 
                It represents the angle of the relief on the surface of the plates.
                unity:m

            length(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute length of the object created from 
                the class PlateHeatExchangerSide. 
                It represents the length of the plates of the heat exchanger.
                unity:m
            
            Npasse(type:int, Nonetype or :obj:np.int64): 
                This parameter indicates the private attribute Npasses of the object created from 
                the class PlateHeatExchangerSide. 
                It represents the number of pass of the heat exchanger.
            
            hydraulicCorrectingFactor(type:float or :obj:np.float64): 
                This parameter indicates the private attribute hydraulicCorrectingFactor of the object created from 
                the class PlateHeatExchangerSide. 
                It's a parameter to minimize the error between the manufacturer and the hydraulic computation.
            
            thermicCorrectingFactor(type:float or :obj:np.float64): 
                This parameter indicates the private attribute thermicCorrectingFactor of the object created from 
                the class PlateHeatExchangerSide. 
                It's a parameter to minimize the error between the manufacturer and the thermic computation.

            downstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[0] of the 
                object created from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid enters into the dipole (or the
                dipole entry). By default all the states attributes of the object downstreamPole 
                are undefined (with the None variable).

            upstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[1] of the 
                object created from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid exits the dipole (or the
                dipole outlet). By default all the states attributes of the object 
                upstreamPole are undefined (with the None variable).

            flow(:obj: Flow): 
                This parameter indicates the private attribute flow of the object created from 
                the class Dipole. 
                It represents the state of the flow of the dipole. By default all the states
                attributes of the object flow are undefined (with the None variable).

            variables(type:list of booleans):
                This argument is described in the documentation of the class Dipole.
                By default it's fixed to [True, True, True, True] because all the 
                parameter are variable for the majority of case.
            
            caracteristics(type:list of booleans):
                This argument is described in the documentation of the class Dipole.
                By default it's fixed to [True, True] because the pipe have an
                hydraulic caracteristic and for the majority of cases the pipe
                have also a thermicCaracteristic which corresponds to the elevation
                of temperature of the fluid induced by the friction with the surface 
                roughness of the pipe.
            
            exchanger(type:boolean):
                This argument is described in the documentation of the class Dipole.
                By default it's fixed to False because it could be considered, for
                the majority of case that the wall pipe is adiabatic. 
                But it could also be in a exchanger system. 


            Note:
                - the cross sectionnal area can be calculated from the hydralic diameter of the pipe
                - variables of the Dipole is fixed to [True, True, False, False]

                        
        Raises : 
            TypeError : 
                It's raised by the function typeErrorAtEntering when the Types and the object
                don't match with the type and the object defined.
            ValueError: 
                If the variables haven't the physical reality, example : hydraulicDiameter < 0

        """

        # calcul of the hydraulic diameter
        x = 2 * pi * plateGap / streakWaveLength
        phi = 1 / 6 * (1 + (1 + x ** 2) ** (1/2) + 4 * (1 + x ** 2/2) ** (1/2))
        hydraulicDiameter = 4 * plateGap / phi


        # calcul of the cross sectionnal area 
        crossSectionalArea = (plateNumber - 1) * plateGap * 10 ** (-3) * width / 2 

 
        # the caracteristics are fixed to [True, False] because it only have an hydraulic caracteristic,
        # indeed, the thermic caracteristic depends on the other part of the heat exchanger. So exchanger = True.
        Dipole.__init__(self, name, hydraulicDiameter, crossSectionalArea, downstreamPole,
                        upstreamPole, flow, variables, caracteristics = [True, False], exchanger=True)
        
        typeErrorAtEntering( angle, message = "the angle must be a float number")
        if angle <0 or angle >90:
            raise ValueError("the angle must be 0 and 90 degree")

        typeErrorAtEntering( length, message = "the length must be a float number")
        if length < 0 :
            raise   ValueError("the length must be a positive float")

        typeErrorAtEntering( Npasse, Types = [int], Classes = [np.int64], message = "the Npasse must be a integer number")
        if Npasse < 1:
            raise ValueError("the number of passe must be a positive integer superior to 1")

        typeErrorAtEntering( plateNumber, Types = [int], Classes = [np.int64], message = "the plateNumber must be a integer number")
        if Npasse < 1:
            raise ValueError("the number of passe must be a positive integer superior to 1")

        typeErrorAtEntering( hydraulicCorrectingFactor, message = "the hydraulicCorrectingFactor must be a float number")
        if hydraulicCorrectingFactor <= 0 :
            raise TypeError("the hydraulic correcting factor must be a strictly positive float close to 1")

        typeErrorAtEntering( thermicCorrectingFactor, message = "the thermicCorrectingFactor must be a float number")
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

    def hydraulicCaracteristic(self, flowRate = None, fluid = None, flowRateUnity = "m3/s", pressureUnity = "Pa", hydraulicCorrectingFactor = None):
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
        Dipole.__init__(self, name, hydraulicDiameter, crossSectionalArea, downstreamPole, upstreamPole, flow = Flow(fluid = fluid, flowRate = flowRate, inputTemperature = inputTemperature), variables=[False,True, True, False])
        downstreamPole.temperature = inputTemperature
        self.flow.inputTemperature = inputTemperature
        self.flow.temperatureDifference = 0.0


class Pump(Dipole):
    #l'initialisation de la classe : 
    def __init__(self,name = 'Pump', hydraulicDiameter = None, crossSectionalArea = None ,flowRates = [], overPressures = [], fluid = Fluid(), inputTemperature = None, downstreamPole = Pole("downstream pole"), upstreamPole = Pole("upstream Pole"), temperatureDifference = 0.0) : 
        Dipole.__init__(self, name, hydraulicDiameter, crossSectionalArea, downstreamPole, upstreamPole, flow = Flow(fluid = fluid, inputTemperature = inputTemperature), variables=[True,True, True, False])
        if (type(flowRates) is not list and not(isinstance(flowRates,np.ndarray))) or (type(overPressures) is not list and not(isinstance(overPressures,np.ndarray))):
            raise TypeError('flowRates and overPressures must be a list of functionnement points')
        downstreamPole.temperature = inputTemperature
        self.flow.temperatureDifference = temperatureDifference
        def caracteristic(flowRate = None):
            if flowRate == None:
                flowRate = self.flow.flowRate
            ex.typeErrorAtEntering(flowRate, message = 'the flowRate must be a float number')
            carac = DataAnalysis.interpolation(flowRates,overPressures)
            return carac(flowRate)
        self.caracteristic = caracteristic
            
    def hydraulicPower(self, flowRate = None):
        if flowRate == None:
            flowRate = self.flow.flowRate
        ex.typeErrorAtEntering(flowRate, message = 'the flowRate must be a float number')
        #print(self.caracteristic(flowRate), flowRate)
        return self.caracteristic(flowRate) * flowRate

#tests



# print(pipe.methodCaracteristic(500, eau, "m3/h", "mCE"))

# flowRate = [i/10 for i in range(1,20000)]
# headLoss = [pipe.methodCaracteristic(q, eau, "m3/h", "mCE") for q in flowRate]

# plt.plot(flowRate, headLoss)
# plt.show()
