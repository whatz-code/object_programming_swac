""" Into the module dipole are initialised the classes : 
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
import numpy as np
from FlowModule import Flow
from GraphModule import Edge, Node
from Calculus import Resolve
from HydraulicThermicCalculus import HydraulicThermicCalculus
from FluidModule import Fluid
from Calculus import DataAnalysis
from ExceptionsAndErrors import typeErrorAtEntering

eau = Fluid()

class Pole(Node):
    """The Pole class represents the state of the flow between 
    the dipoles. It's a child class of the class Node from the
    module Graph.

    Attributes:
        pressure (type:float,Nonetype or :obj:np.float64):
            unity : Pascal.
        temperature (type:float,Nonetype or :obj:np.float64): 
            unity : °C
                 
    

    """
    def __init__(self,name = None, pressure = None, temperature = None, successors = [], fluid = Fluid()) : 
        """Class Pole __init__ method : 
        
        Note : 
            The Pole class is used to give the ponctual state of the flow between various dipoles.
            It's a child of the Node class and so has a important role to play for the definition
            of the topology of the hydraulic and thermic network. 
            the __init__ method offers the opportunity to give the attributes of the Pole object.

        Args:
            pressure (type:float,Nonetype or :obj:np.float64): This parameter indicates the private attribute pressure of the 
                                    object initialised from the classe Pole. It represents the pressures between dipoles which are
                                    associated with the pole object as an attribute.
                                    unity : Pascal.
            temperature (type:float,Nonetype or :obj:np.float64): This parameter indicates the private attribute temperature
                                    of the object initialised from the classe Pole. It represents the pressures between dipoles which are
                                    associated with the pole object as an attribute.
                                    unity : °C
            successors (type:list of :obj:Pole): This parameter indicates the private attribute successors of the 
                                    object initialised from the parent class Node. It represents the other poles linked
                                    by a dipole where the pole object is the downstream attribute.
            fluid(:obj: Fluid): This parameter indicates the private attribute fluid of the obkect initialised from the class Flow. It represents
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

        typeErrorAtEntering(fluid,Types = [], Classes = [Fluid], message = "the fluid must be a Fluid object")
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
    """The Dipole class represents the caracteristics
    of a dipole (place where there is a flow between 
    a pole A to a pole B).
    It's a child class of the class Edge from the module Graph.

    Attributes:

        hydraulicDiameter (type:float,Nonetype or :obj:np.float64): 
            It represents the caracteristical length in the dipole to computes the 
            reynolds or other important numbers.
            unity : m

        crossSectionnalArea (type:float,Nonetype or :obj:np.float64): 
            It represents the sectionnal area of the flow, it's an important parameter to compute 
            the average velocity of the fluid into the dipole.
            unity : m²

        downstreamPole (:obj:Pole): 
            It represents the pole where the fluid enters into the dipole (or the
            dipole entry). By default all the states attributes of the object downstreamPole 
            are undefined (with the None variable).

        upstreamPole (:obj:Pole): 
            It represents the pole where the fluid exits the dipole (or the
            dipole outlet). By default all the states attributes of the object 
            upstreamPole are undefined (with the None variable).

        flow(:obj: Flow): 
            It represents the state of the flow of the dipole. By default all the states
            attributes of the object flow are undefined (with the None variable).

        variables(type:list of 4 booleans): 
            It gives the knowledge of how the variables of the flow can be calculated : 
                - if variables[0] == False : the flow rate is fixed (so flowRate is not
                 a variable of the system)
                - if variables[1] == False : the difference of pressure is fixed
                - if variables[2] == False : the input temperature is fixed
                - if variables[3] == False : the outlet temperature is fixed      

            This attribute is usefull to reduce the unknown variables in the system which has to be 
            resolved to know the functionnement hydraulic and thermic of the networks

        caracteristics(type:list of 2 booleans):
            This parameter indicate the private attribut caracteristics of the object initialised from
            the class Dipole.
            It gives the knowledge of what caracteristics are defined :
                - if caracteristics[0] = False : the method hydraulicCaracteristic is not defined (True : is defined)
                - if caracteristics[1] = False : the method hydraulicCaracteristic is not defined (True : is defined)
        
        exchanger(type:boolean):
            this paramete indicate the private attribute exchanger of the object initialised from the class
            exchanger.
            It gives the knowledge : 
                - if the dipole is a part of an exchanger : True, else : False

                 
    

    """
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

            hydraulicDiameter (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute hydraulicDiameter of the 
                dipole object initialised from the class Dipole. 
                It represents the caracteristical length in the dipole to computes the 
                reynolds or other important numbers.
                unity : m

            crossSectionnalArea (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute crossSectionalArea of the object 
                initialised from the Dipole class. 
                It represents the sectionnal area of the flow, it's an important parameter to compute 
                the average velocity of the fluid into the dipole.
                unity : m²

            downstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[0] of the 
                object initialised from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid enters into the dipole (or the
                dipole entry). By default all the states attributes of the object downstreamPole 
                are undefined (with the None variable).

            upstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[1] of the 
                object initialised from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid exits the dipole (or the
                dipole outlet). By default all the states attributes of the object 
                upstreamPole are undefined (with the None variable).

            flow(:obj: Flow): 
                This parameter indicates the private attribute flow of the object initialised from 
                the class Dipole. 
                It represents the state of the flow of the dipole. By default all the states
                attributes of the object flow are undefined (with the None variable).

            variables(type:list of 4 booleans):
                This parameter indicates the private attribute variables of the object initialised from 
                the class Dipole.    
                It gives the knowledge of how the variables of the flow can be calculated : 
                    - if variables[0] == False : the flow rate is fixed (so flowRate is a variable of the system)
                    - if variables[1] == False : the difference of pressure is fixed
                    - if variables[2] == False : the input temperature is fixed
                    - if variables[3] == False : the outlet temperature is fixed      

                This attribute is usefull to reduce the unknown variables in the system which has to be 
                resolved to know the functionnement hydraulic and thermic of the networks

            caracteristics(type:list of 2 booleans):
                This parameter indicate the private attribut caracteristics of the object initialised from
                the class Dipole.
                It gives the knowledge of what caracteristics are defined :
                    - if caracteristics[0] = False : the method hydraulicCaracteristic is not defined (True : is defined)
                    - if caracteristics[1] = False : the method hydraulicCaracteristic is not defined (True : is defined)
            
            exchanger(type:boolean):
                this paramete indicate the private attribute exchanger of the object initialised from the class
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
        #Edge is initialised with Poles[0] = downstreamPole and Poles[1] = upstreamPole
        typeErrorAtEntering(downstreamPole,Types = [], Classes = [Pole], message = "the downstreamPole must be an instance of the class Pole")
        typeErrorAtEntering(upstreamPole,Types = [], Classes = [Pole], message = "the upstreamPole must be an instance of the class Pole")
        Edge.__init__(self, name, [downstreamPole, upstreamPole])
        
        typeErrorAtEntering(flow,Types = [], Classes = [Flow], message = "the flow must be an instance of the class Flow")
        self.__flow = flow

        typeErrorAtEntering(hydraulicDiameter, Types = [float, type(None)], message = "the hydraulic diameter must be a float number")
        if hydraulicDiameter !=None:
            if hydraulicDiameter <= 0:
                raise ValueError('hydraulic diameter must be strictly positive')
        self.__hydraulicDiameter = hydraulicDiameter

        typeErrorAtEntering(crossSectionalArea, Types = [float, type(None)], message = "the cross sectionnal area must be a float number")
        if crossSectionalArea != None:
            if crossSectionalArea <= 0:
                raise ValueError('cross sectionnal area must be strictly positive')
        self.__crossSectionalArea = crossSectionalArea

        typeErrorAtEntering(variables, Types = [list], message = "the variables must be a list of 4 booleans")
        if len(variables) != 4:
            raise TypeError("the variables must be a list of 4 booleans")
        for variable in variables :
            if type(variable) is not bool: 
                raise TypeError("the variables must be a list of 4 booleans")
        self.__variables = variables

        typeErrorAtEntering(caracteristics, Types = [list], message = "the caracteristics must be a list of 2 booleans")
        if len(caracteristics) != 2:
            raise TypeError("the caracteristics must be a list of 2 booleans")
        for variable in caracteristics :
            if type(variable) is not bool: 
                raise TypeError("the caracteristics must be a list of 2 booleans")
        self.__caracteristics = caracteristics

        typeErrorAtEntering(exchanger, Types = [bool], message = "the variables must be a boolean")
        self.__exchanger = exchanger

    @property 
    def hydraulicDiameter(self):
        """ get method and set method to access the private variable flowRate """
        return self.__hydraulicDiameter

    @hydraulicDiameter.setter 
    def hydraulicDiameter(self,hydraulicDiameter):
        typeErrorAtEntering(hydraulicDiameter, Types = [float, type(None)], message = "the hydraulic diameter must be a float number")
        if hydraulicDiameter !=None:
            if hydraulicDiameter <= 0:
                raise ValueError('hydraulic diameter must be strictly positive')
        self.__hydraulicDiameter = hydraulicDiameter

    @property 
    def crossSectionalArea(self): 
        """ get method and set method to access the private variable crossSectionnalArea """
        return self.__crossSectionalArea

    @crossSectionalArea.setter 
    def crossSectionalArea(self,crossSectionalArea): 
        typeErrorAtEntering(crossSectionalArea, Types = [float, type(None)], message = "the cross sectionnal area must be a float number")
        if crossSectionalArea != None:
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
        self.nodes = [downstreamPole, self.upstreamPole]
    
    @property 
    def upstreamPole(self): 
        """ get method and set method to access the private variable upstreamPole """
        return self.nodes[1]

    @upstreamPole.setter 
    def upstreamPole(self,upstreamPole): 
        typeErrorAtEntering(upstreamPole,Types = [], Classes = [Pole], message = "the upstreamPole must be an instance of the class Pole")
        self.nodes = [self.downstreamPole, upstreamPole]

    @property 
    def variables(self): 
        """ get method and set method to access the private variable variables """
        return self.__variables

    @variables.setter 
    def variables(self,variables): 
        typeErrorAtEntering(variables, Types = [list], message = "the variables must be a list of 5 booleans")
        if len(variables) != 4:
            raise TypeError("the variables must be a list of 4 booleans")
        for variable in variables :
            if type(variable) is not bool: 
                raise TypeError("the variables must be a list of 4 booleans")
        self.__variables = variables
    
    @property 
    def caracteristics(self): 
        """ get method and set method to access the private variable caracteristics """
        return self.__caracteristics

    @caracteristics.setter 
    def caracteristics(self,caracteristics): 
        typeErrorAtEntering(caracteristics, Types = [list], message = "the caracteristics must be a list of 5 booleans")
        if len(caracteristics) != 2:
            raise TypeError("the caracteristics must be a list of 2 booleans")
        for caracteristic in caracteristics :
            if type(caracteristic) is not bool: 
                raise TypeError("the caracteristics must be a list of 2 booleans")
        self.__caracteristics = caracteristics
    
    @property 
    def exchanger(self): 
        """ get method and set method to access the private variable exchanger """
        return self.__exchanger

    @exchanger.setter 
    def exchanger(self,exchanger): 
        typeErrorAtEntering(exchanger, Types = [bool], message = "the variables must be a boolean")
        self.__echanger = echanger
    

    def hydraulicCorrelation(self, reynoldsNumber) :
        """ the method hydraulicCorrelation 

        Note: 
            When this method is defined, it take into account the caracteristics
            of the object initialised from the class Dipole and the reynolds number of 
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
            of the object initialised from the class Dipole and the flow rate and the 
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
            of the object initialised from the class Dipole, the reynolds number and
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
            of the object initialised from the class Dipole, the flow rate and the 
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
    """The Pipe class represents the caracteristics
    of a pipe. It's a child class of the class Dipole.

    Attributes:
        name( type:any ): 
            this parameters indicates the private attribute name. This parameter gives 
            the user the opportunity to organise his dipole objects.

        pipeDiameter (type:float,Nonetype or :obj:np.float64): 
            It represents the caracteristical length in the dipole to computes the 
            reynolds or other important numbers.
            By default the pipeDiameter is fixed to 0.348 m because it's an pipe
            diameter that exists in reality.
            unity : m
        
        rugosity(type:float): 
            It represents the surface roughness of the pipe.
            By default it's fixed to 0.0001 m because it's a good order of magnitude
            unity:m
        
        length(type:float): 
            It represents the length of the pipe.
            By default it's 50 m but it should be any other length while it's far superior to
            the pipeDiameter.
            unity:m

            

    """
    def __init__(self,name = 'Pipe', pipeDiameter = 0.348, rugosity = 0.0001, length = 50.0,
                    downstreamPole = Pole('downstream pole'), upstreamPole = Pole('upstream Pole'), 
                    flow = Flow(), variables = [True, True, True, True], caracteristics = [True, True], 
                    exchanger = False) : 
        """Class Pipe __init__ method : 
        
        Note : 
            The Pipe class is a child of the Dipole class. It represents pipes in a pipe network.
            the __init__ method offers the opportunity to give the attributes of the Pipe object.

        Args:
            name( type:any ): 
                this parameters indicates the private attribute name. This parameter gives 
                        the user the opportunity to organise his dipole objects.

            pipeDiameter (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute pipeDiameter of the 
                dipole object initialised from the class Dipole. 
                It represents the caracteristical length in the dipole to computes the 
                reynolds or other important numbers.
                By default the pipeDiameter is fixed to 0.348 m because it's an pipe
                diameter that exists in reality.
                unity : m
            
            rugosity(type:float): 
                This parameter indicates the private attribute flow of the object initialised from 
                the class Pipe. 
                It represents the surface roughness of the pipe.
                By default it's fixed to 0.0001 m because it's a good order of magnitude
                unity:m
            
            length(type:float): 
                This parameter indicates the private attribute length of the object initialised from 
                the class Pipe. 
                It represents the length of the pipe.
                By default it's 50 m but it should be any other length while it's far superior to
                the pipeDiameter.
                unity:m

            downstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[0] of the 
                object initialised from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid enters into the dipole (or the
                dipole entry). By default all the states attributes of the object downstreamPole 
                are undefined (with the None variable).

            upstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[1] of the 
                object initialised from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid exits the dipole (or the
                dipole outlet). By default all the states attributes of the object 
                upstreamPole are undefined (with the None variable).

            flow(:obj: Flow): 
                This parameter indicates the private attribute flow of the object initialised from 
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
                If the variables haven't the physical reality, example : pipeDiameter < 0

        """
        Dipole.__init__(self, name, pipeDiameter, pipeDiameter**2*pi/4,
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
    def pipeDiameter(self): 
        """ get and set allows the user to modify the private pipeDiameter attribute """ 
        return self.hydraulicDiameter

    @pipeDiameter.setter 
    def pipeDiameter(self,pipeDiameter): 
        typeErrorAtEntering(pipeDiameter, message = "the pipeDiameter must be a float number")
        if type(pipeDiameter) is not type(None):
            if pipeDiameter < 0:
                raise ValueError('pipeDiameter must be positive')
        self.__crossSectionalArea = pipeDiameter**2*pi/4
        self.hydraulicDiameter = pipeDiameter

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
            of the object initialised from the class Dipole and the reynolds number of 
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
            of the object initialised from the class Dipole and the flow rate and the 
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
            of the object initialised from the class Dipole, the flow rate and the 
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
    """The PlateHeatExchangerSide class represents the caracteristics
    of one side of the plate heat exchanger. It's a child class of the 
    class Dipole.

    Attributes:
        width (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute width of the 
                plateHeatExchangerSide object initialised from the class PlateHeatExchangerSide. 
                It represents the caracteristical width of the exchanger.
                unity : m
            
        plateGap(type:float, Nonetype or :obj:np.float64): 
            This parameter indicates the private attribute plateGape of the object initialised from 
            the class PlateHeatExchangerSide. 
            unity:mm
        
        streakWaveLength(type:float, Nonetype or :obj:np.float64): 
            This parameter indicates the private attribute streakWaveLength of the object initialised from 
            the class PlateHeatExchangerSide. 
            It represents the Wave length of the relief of the heat echanger plates
            unIy:mm
        
        plateNumber(type:float, Nonetype or :obj:np.float64): 
            This parameter indicates the private attribute plateNumber of the object initialised from 
            the class PlateHeatExchangerSide. 
            It represents the number of plates of the heat exchanger
        
        angle(type:float, Nonetype or :obj:np.float64): 
            This parameter indicates the private attribute angle of the object initialised from 
            the class PlateHeatExchangerSide. 
            It represents the angle of the relief on the surface of the plates.
            unity:°

        length(type:float, Nonetype or :obj:np.float64): 
            This parameter indicates the private attribute length of the object initialised from 
            the class PlateHeatExchangerSide. 
            It represents the length of the plates of the heat exchanger.
            unity:m
        
        Npasse(type:int, Nonetype or :obj:np.int64): 
            This parameter indicates the private attribute Npasses of the object initialised from 
            the class PlateHeatExchangerSide. 
            It represents the number of pass of the heat exchanger.
        
        hydraulicCorrectingFactor(type:float or :obj:np.float64): 
            This parameter indicates the private attribute hydraulicCorrectingFactor of the object initialised from 
            the class PlateHeatExchangerSide. 
            It's a parameter to minimize the error between the manufacturer and the hydraulic computation.
        
        thermicCorrectingFactor(type:float or :obj:np.float64): 
            This parameter indicates the private attribute thermicCorrectingFactor of the object initialised from 
            the class PlateHeatExchangerSide. 
            It's a parameter to minimize the error between the manufacturer and the thermic computation.

            

    """
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
                plateHeatExchangerSide object initialised from the class PlateHeatExchangerSide. 
                It represents the caracteristical width of the exchanger.
                unity : m
            
            plateGap(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute plateGape of the object initialised from 
                the class PlateHeatExchangerSide. 
                unity:mm
            
            streakWaveLength(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute streakWaveLength of the object initialised from 
                the class PlateHeatExchangerSide. 
                It represents the Wave length of the relief of the heat echanger plates
                unIy:mm
            
            plateNumber(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute plateNumber of the object initialised from 
                the class PlateHeatExchangerSide. 
                It represents the number of plates of the heat exchanger
            
            angle(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute angle of the object initialised from 
                the class PlateHeatExchangerSide. 
                It represents the angle of the relief on the surface of the plates.
                unity:°

            length(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute length of the object initialised from 
                the class PlateHeatExchangerSide. 
                It represents the length of the plates of the heat exchanger.
                unity:m
            
            Npasse(type:int, Nonetype or :obj:np.int64): 
                This parameter indicates the private attribute Npasses of the object initialised from 
                the class PlateHeatExchangerSide. 
                It represents the number of pass of the heat exchanger.
            
            hydraulicCorrectingFactor(type:float or :obj:np.float64): 
                This parameter indicates the private attribute hydraulicCorrectingFactor of the object initialised from 
                the class PlateHeatExchangerSide. 
                It's a parameter to minimize the error between the manufacturer and the hydraulic computation.
            
            thermicCorrectingFactor(type:float or :obj:np.float64): 
                This parameter indicates the private attribute thermicCorrectingFactor of the object initialised from 
                the class PlateHeatExchangerSide. 
                It's a parameter to minimize the error between the manufacturer and the thermic computation.

            downstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[0] of the 
                object initialised from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid enters into the dipole (or the
                dipole entry). By default all the states attributes of the object downstreamPole 
                are undefined (with the None variable).

            upstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[1] of the 
                object initialised from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid exits the dipole (or the
                dipole outlet). By default all the states attributes of the object 
                upstreamPole are undefined (with the None variable).

            flow(:obj: Flow): 
                This parameter indicates the private attribute flow of the object initialised from 
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
        phi = 1 / 6 * (1 + (1 + x ** 2) ** (1/2) + 4 * (1 + x ** 2) ** (1/2))
        hydraulicDiameter = 4 * plateGap / phi


        # calcul of the cross sectionnal area 
        crossSectionalArea = (plateNumber - 1) * plateGap * 10 ** (-3) * width / 2 / Npasse

 
        # the caracteristics are fixed to [True, False] because it only have an hydraulic caracteristic,
        # indeed, the thermic caracteristic depends on the other part of the heat exchanger. So exchanger = True.
        Dipole.__init__(self, name, hydraulicDiameter, crossSectionalArea, downstreamPole,
                        upstreamPole, flow, variables, caracteristics = [True, False], exchanger=True)

        typeErrorAtEntering( width, message = "the width must be a float number")
        if length < 0 :
            raise   ValueError("the width must be a positive float")

        typeErrorAtEntering( plateGap, message = "the plate gap must be a float number")
        if plateGap < 0 :
            raise   ValueError("the plate gap must be a positive float")

        typeErrorAtEntering( streakWaveLength, message = "the streak wave length must be a float number")
        if streakWaveLength < 0 :
            raise   ValueError("the streak wave length must be a positive float")

        typeErrorAtEntering( plateNumber, Types = [int], Classes = [np.int64], message = "the plateNumber must be a integer number")
        if plateNumber < 1:
            raise ValueError("the number of plates must be a positive integer superior to 1")
        
        typeErrorAtEntering( angle, message = "the angle must be a float number")
        if angle <0 or angle >90:
            raise ValueError("the angle must be 0 and 90 degree")

        typeErrorAtEntering( length, message = "the length must be a float number")
        if length < 0 :
            raise   ValueError("the length must be a positive float")

        typeErrorAtEntering( Npasse, Types = [int], Classes = [np.int64], message = "the Npasse must be a integer number")
        if Npasse < 1:
            raise ValueError("the number of passe must be a positive integer superior to 1")

        typeErrorAtEntering( hydraulicCorrectingFactor, message = "the hydraulicCorrectingFactor must be a float number")
        if hydraulicCorrectingFactor <= 0 :
            raise TypeError("the hydraulic correcting factor must be a strictly positive float close to 1")

        typeErrorAtEntering( thermicCorrectingFactor, message = "the thermicCorrectingFactor must be a float number")
        if thermicCorrectingFactor <= 0 :
            raise TypeError("the thermic correcting factor must be a strictly positive float close to 1")
        
        self.__width = width
        self.__plateGap = plateGap
        self.__streakWaveLength = streakWaveLength
        self.__plateNumber = plateNumber
        self.__angle = angle
        self.__length = length
        self.__Npasse = Npasse
        self.__hydraulicCorrectingFactor = hydraulicCorrectingFactor
        self.__thermicCorrectingFactor = thermicCorrectingFactor


    @property 
    def width(self): 
        """ get and set allows the user to modify the private width attribute """
        return self.__width

    @width.setter 
    def width(self,width): 
        typeErrorAtEntering(width, message = "the width must be a float number")
        if type(width) is not type(None):
            if width < 0:
                raise ValueError('width must be positive')
        plateGap = self.plateGap
        Npasse = self.Npasse
        plateNumber = self.plateNumber

        # calcul of the cross sectionnal area 
        crossSectionalArea = (plateNumber - 1) * plateGap * 10 ** (-3) * width / 2 / Npasse

        self.__width = width
        self.crossSectionalArea = crossSectionalArea

    @property 
    def plateGap(self): 
        """ get and set allows the user to modify the private plateGap attribute """
        return self.__plateGap

    @plateGap.setter 
    def plateGap(self,plateGap): 
        typeErrorAtEntering(plateGap, message = "the plateGap must be a float number")
        if type(plateGap) is not type(None):
            if plateGap < 0:
                raise ValueError('plateGap must be positive')
        
        width = self.width
        streakWaveLength = self.streakWaveLength
        plateNumber = self.plateNumber
        Npasse = self.Npasse

        # calcul of the hydraulic diameter
        x = 2 * pi * plateGap / streakWaveLength
        phi = 1 / 6 * (1 + (1 + x ** 2) ** (1/2) + 4 * (1 + x ** 2) ** (1/2))
        hydraulicDiameter = 4 * plateGap / phi


        # calcul of the cross sectionnal area 
        crossSectionalArea = (plateNumber - 1) * plateGap * 10 ** (-3) * width / 2 / Npasse

        self.__plateGap = plateGap
        self.__hydraulicDiameter = hydraulicDiameter
        self.__crossSectionalArea = crossSectionalArea
    
    @property 
    def streakWaveLength(self): 
        """ get and set allows the user to modify the private streakWaveLength attribute """
        return self.__streakWaveLength

    @streakWaveLength.setter 
    def streakWaveLength(self,streakWaveLength): 
        typeErrorAtEntering(streakWaveLength, message = "the streakWaveLength must be a float number")
        if type(streakWaveLength) is not type(None):
            if streakWaveLength < 0:
                raise ValueError('streakWaveLength must be positive')
        
        plateGap = self.plateGap

        # calcul of the hydraulic diameter
        x = 2 * pi * plateGap / streakWaveLength
        phi = 1 / 6 * (1 + (1 + x ** 2) ** (1/2) + 4 * (1 + x ** 2) ** (1/2))
        hydraulicDiameter = 4 * plateGap / phi

        self.__streakWaveLength = streakWaveLength
        self.__hydraulicDiameter = hydraulicDiameter
    
    @property 
    def plateNumber(self): 
        """ get and set allows the user to modify the private plateNumber attribute """
        return self.__plateNumber

    @plateNumber.setter 
    def plateNumber(self,plateNumber): 
        typeErrorAtEntering( plateNumber, Types = [int], Classes = [np.int64], message = "the plateNumber must be a integer number")
        if plateNumber < 1:
            raise ValueError("the number of plates must be a positive integer superior to 1")
        
        width = self.width
        plateGap = self.plateGap
        Npasse = self.Npasse

        # calcul of the cross sectionnal area 
        crossSectionalArea = (plateNumber - 1) * plateGap * 10 ** (-3) * width / 2 / Npasse

        self.__plateNumber = plateNumber
        self.__crossSectionalArea = crossSectionalArea

    @property 
    def angle(self): 
        """ get and set allows the user to modify the private angle attribute """
        return self.__angle

    @angle.setter 
    def angle(self,angle): 
        typeErrorAtEntering(angle, message = "the angle must be a float number")
        if angle <0 or angle >90:
            raise ValueError("the angle must be 0 and 90 degree")
        self.__angle = angle

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
    
    @property 
    def Npasse(self): 
        """ get and set allows the user to modify the private Npasse attribute """
        return self.__Npasse

    @Npasse.setter 
    def Npasse(self,Npasse): 
        typeErrorAtEntering( Npasse, Types = [int], Classes = [np.int64], message = "the Npasse must be a integer number")
        if Npasse < 1:
            raise ValueError("the number of plates must be a positive integer superior to 1")

        width = self.width
        plateGap = self.plateGap

        # calcul of the cross sectionnal area 
        crossSectionalArea = (plateNumber - 1) * plateGap * 10 ** (-3) * width / 2 / Npasse

        self.__crossSectionalArea = crossSectionalArea
        self.__Npasse = Npasse

    @property 
    def hydraulicCorrectingFactor(self): 
        """ get and set allows the user to modify the private hydraulicCorrectingFactor attribute """
        return self.__hydraulicCorrectingFactor

    @hydraulicCorrectingFactor.setter 
    def hydraulicCorrectingFactor(self,hydraulicCorrectingFactor): 
        typeErrorAtEntering(hydraulicCorrectingFactor, message = "the hydraulicCorrectingFactor must be a float number")
        if type(hydraulicCorrectingFactor) is not type(None):
            if hydraulicCorrectingFactor < 0:
                raise ValueError('hydraulicCorrectingFactor must be positive')
        self.__hydraulicCorrectingFactor = hydraulicCorrectingFactor

    @property 
    def thermicCorrectingFactor(self): 
        """ get and set allows the user to modify the private thermicCorrectingFactor attribute """
        return self.__thermicCorrectingFactor

    @thermicCorrectingFactor.setter 
    def thermicCorrectingFactor(self,thermicCorrectingFactor): 
        typeErrorAtEntering(thermicCorrectingFactor, message = "the thermicCorrectingFactor must be a float number")
        if type(thermicCorrectingFactor) is not type(None):
            if thermicCorrectingFactor < 0:
                raise ValueError('thermicCorrectingFactor must be positive')
        self.__thermicCorrectingFactor = thermicCorrectingFactor
    
    #it's the Martin correlation
    def hydraulicCorrelation(self, reynoldsNumber, length = None, angle = None, Npasse = None, 
                            hydraulicDiameter = None, parameterA = 3.8, parameterB = 0.045, parameterC = 0.09, 
                            hydraulicCorrectingFactor = 1.0): 
        """ the method hydraulicCorrelation 

        Note: 
            When this method is defined, it take into account the caracteristics
            of the object initialised from the class Dipole and the reynolds number of 
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
            Npasse(type:int or None type):
                If the Npasse is equal to None, then the Npasse
                taken into account is taken from the dipole object.
            parameterA(type:float or None type):
            parameterB(type:float or None type):
            parameterc(type:float or None type):
                these 3 parameters are the parameters in the correlation
                of Martin, it have default values, it is the value taken
                from the handbook : fundamentals of heat exchanger design
                but others value could be more accurate.
            hydraulicCorrectingFactor(type:float or None type):
                If the hydraylicCorrectingFactor is equal to None, then 
                the hydraylicCorrectingFactor taken into account is taken 
                from the dipole object.
                unity: m

        Returns:
            headLossCoefficient(type:float)
                        
        Raises: 
            TypeError : If reynoldsNumber is not a float


        """
        #intern parameters are taken if not defined
        if length == None:
            length = self.length
        if angle == None:
            angle = self.angle
        if Npasse == None:
            Npasse = self.Npasse
        if hydraulicDiameter == None:
            hydraulicDiameter = self.hydraulicDiameter

        #exceptions are initialised :
        typeErrorAtEntering(angle, message = "the angle must be a float number")
        if angle <0 or angle >90:
            raise ValueError("the angle must be 0 and 90 degree")

        typeErrorAtEntering(length, message = "the length must be a float number")
        if length < 0 :
            raise   ValueError("the length must be a positive float")

        typeErrorAtEntering( Npasse, Types = [int], Classes = [np.int64], message = "the Npasse must be a integer number")
        if Npasse < 1:
            raise ValueError("the number of passe must be a positive integer superior to 1")

        typeErrorAtEntering(hydraulicCorrectingFactor, message = "the hydraulicCorrectingFactor must be a float number")
        if hydraulicCorrectingFactor <= 0 :
            raise TypeError("the hydraulic correcting factor must be a strictly positive float close to 1")

        typeErrorAtEntering(reynoldsNumber, message = "the reynoldsNumber must be a float number")
        if reynoldsNumber <=0 :
            raise ValueError("the reynolds number must be a strictly positive float")
        
        #conversion of the angle in radiant
        angle = angle * pi / 180
        
        def laminar(reynoldsNumber, angle):
            """ returns the regular head loss coefficient for a laminar flow """
            if reynoldsNumber > 0 :
                f0 = 16 / reynoldsNumber
                f1 = 149.25 / reynoldsNumber + 0.9625
                etape = etapeCalcul(angle, f0, f1)
                return 1 / etape ** 2
            else : 
                raise ValueError('reynoldsNumber should be superior to 0')

        def turbulent(reynoldsNumber, angle):
            """ returns the regular head loss coefficient for a turbulent flow """
            f0 = (1.56 * log(reynoldsNumber) - 3) ** (-2)
            f1 = 9.75 / reynoldsNumber ** 0.289
            etape = etapeCalcul(angle, f0, f1)
            return 1 / etape ** 2

        #just a step to calcul
        def etapeCalcul(angle, f0, f1):
            return cos(angle) / (parameterB * tan(angle) + parameterC * sin(angle) + f0 / cos(angle)) ** (1/2) + (1 - cos(angle)) / (parameterA * f1) ** (1/2)

        #it's considered that the flow is laminar if the reynolds number is higher than 2000 and
        #turbulent if the reynolds number is higher than 4000, between the 2 limits it's the 
        #average balanced by the distance of the limits 
        if reynoldsNumber < 2000 :
            return laminar(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse
        if reynoldsNumber >= 2000 and reynoldsNumber <=4000 :
            coefficient = (reynoldsNumber - 2000)/2000
            return (1-coefficient) * laminar(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse + coefficient * turbulent(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse
        else :
            return turbulent(reynoldsNumber, angle) * length / hydraulicDiameter * Npasse

    def hydraulicCaracteristic(self, flowRate = None, fluid = None, flowRateUnity = "m3/s", pressureUnity = "Pa", hydraulicCorrectingFactor = None):
        """ the method hydraulicCaracteristic 

        Note: 
            When this method is defined, it take into account the hydraulicCaracteristics
            of the object initialised from the class Dipole and the flow rate and the 
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
        if hydraulicCorrectingFactor == None :
            hydraulicCorrectingFactor = self.hydraulicCorrectingFactor
        if flowRate == None:
            flowRate = self.flow.flowRate
        if fluid == None:
            fluid = self.flow.fluid

        typeErrorAtEntering( flowRate, message = "the flow rate must be a float number")
        typeErrorAtEntering( flowRate, Types = [], Classes = [Fluid], message = "the fluid must be a fluid object")

        return - HydraulicThermicCalculus.caracteristic(self, flowRate, fluid, flowRateUnity, pressureUnity) * hydraulicCorrectingFactor

    def thermicCorrelation(self, reynoldsNumber, prandtlNumber = None, length = None, 
                            angle = None, Npasse = None, hydraulicDiameter = None, parameterA = 3.8, 
                            parameterB = 0.045, parameterC = 0.09, thermicCorrectingFactor = 1.0):
        """ the method thermicCorrelation 

        Note: 
            It take into account the caracteristics
            of the object initialised from the class Dipole, the reynolds number and
            the prandtl number to give the Nusselt number

        Args:
            reynoldsNumber(type:float):
                It corresponds to the Reynolds number which combines the
                importants information of the flow and the dipole.
            prandtlNumber(type:float):
                It corresponds to the prandtl number which is the ratio 
                between the momentum diffusivity and the thermal diffusivity :
                prantlNumber = thermicCapacity * dynamicViscosity / thermicConductivity
            hydraulicDiameter(type:float or None type):
                If the hydraulicDiameter is equal to None, then the hydraulicDiameter
                taken into account is taken from the dipole object.
                unity: m
            Npasse(type:int or None type):
                If the Npasse is equal to None, then the Npasse
                taken into account is taken from the dipole object.
            parameterA(type:float or None type):
            parameterB(type:float or None type):
            parameterc(type:float or None type):
                these 3 parameters are the parameters in the correlation
                of Martin, it have default values, it is the value taken
                from the handbook : fundamentals of heat exchanger design
                but others value could be more accurate.
            thermicCorrectingFactor(type:float or None type):
                If the thermicCorrectingFactor is equal to None, then 
                the thermicCorrectingFactor taken into account is taken 
                from the dipole object.

        Returns:
            NusseltNumber(type:float)
                        
        Raises: 
            TypeError : If the variables have not the types specified


        """
        #taking of the intern variables if not defined
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

        #raise of exceptions

        typeErrorAtEntering(angle, message = "the angle must be a float number")
        if angle <0 or angle >90:
            raise ValueError("the angle must be 0 and 90 degree")

        typeErrorAtEntering(length, message = "the length must be a float number")
        if length < 0 :
            raise   ValueError("the length must be a positive float")

        typeErrorAtEntering( Npasse, Types = [int], Classes = [np.int64], message = "the Npasse must be a integer number")
        if Npasse < 1:
            raise ValueError("the number of passe must be a positive integer superior to 1")

        typeErrorAtEntering(prandtlNumber, message = "the prandtl number must be a float number")

        typeErrorAtEntering(thermicCorrectingFactor, message = "the thermicCorrectingFactor must be a float number")
        if thermicCorrectingFactor <= 0 :
            raise TypeError("the hydraulic correcting factor must be a strictly positive float close to 1")

        typeErrorAtEntering(reynoldsNumber, message = "the reynoldsNumber must be a float number")
        if reynoldsNumber <=0 :
            raise ValueError("the reynolds number must be a strictly positive float")
   
        headLossCoefficient = self.hydraulicCorrelation(reynoldsNumber, parameterA = 3.8, parameterB = 0.045, parameterC = 0.09) / Npasse / length * hydraulicDiameter
        angle *= pi / 180
        nusseltNumber = 0.122 * prandtlNumber ** (1/3) * (headLossCoefficient * reynoldsNumber ** 2 * sin(2 * angle) ) ** 0.374

        return nusseltNumber * thermicCorrectingFactor

class IdealPump(Dipole):
    """The IdealPump class represents the caracteristics
    of a pump which deliver a constant flowRate.  It's a child class of the 
    class Dipole.

    Attributes:       
        thermicPower(type:float,Nonetype or :obj:np.float64): 
            This parameter allows the class to build a constant thermic caracteristic. By default, it's equal to 0, but
            for real pump there is always some thermic transfert.
            

    """
    def __init__(self,name = 'Ideal Pump', hydraulicDiameter = None, crossSectionalArea = None,
                flowRate = None, fluid = Fluid(), inputTemperature = None, thermicPower = 0.0,
                downstreamPole = Pole("downstream pole"), upstreamPole = Pole("upstream Pole")) : 
        """Class IdealPump __init__ method : 
        
        Note : 
            The class IdealPump is used to fixe a flowRate in any point in the hydraulic Network.
            for example it can be used when it's convenient to know the HMT for a given flow rate.

            the __init__ method offers the opportunity to give the attributes of the idealpump object.

        Args:
            name( type:any ): 
                this parameters indicates the private attribute name. This parameter gives 
                the user the opportunity to organise his dipole objects.

            hydraulicDiameter (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute hydraulicDiameter of the 
                dipole object initialised from the class Dipole. 
                It represents the caracteristical length in the dipole to computes the 
                reynolds or other important numbers.
                unity : m

            crossSectionnalArea (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute crossSectionalArea of the object 
                initialised from the Dipole class. 
                It represents the sectionnal area of the flow, it's an important parameter to compute 
                the average velocity of the fluid into the dipole.
                unity : m²

            downstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[0] of the 
                object initialised from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid enters into the dipole (or the
                dipole entry). By default all the states attributes of the object downstreamPole 
                are undefined (with the None variable).

            upstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[1] of the 
                object initialised from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid exits the dipole (or the
                dipole outlet). By default all the states attributes of the object 
                upstreamPole are undefined (with the None variable).

            flowRate(type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute flowrate of the attribute object flow, it initialised 
                from the class Flow. 
                It represents the fixed flowRate of the functionnement of the pump.
                unity:m³/s

            fluid(:obj: Fluid): 
                This parameter indicates the private attribute fluid of the attribute object flow, it initialised 
                from the class Flow. 
                It represents the state of the flow of the dipole. By default all the states
                attributes of the object flow are undefined (with the None variable).
            
            inputTemperature(type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute inputTemperature of the attribute object flow, it initialised 
                from the class Flow. 
                It the temperature of the fluid pumped, it's not necessary to enter this variable here, but in the majority
                of case the pump are at the input of the Hydraulic Network.
                unity:°C
            
            thermicPower(type:float,Nonetype or :obj:np.float64): 
                This parameter allows the class to build a constant thermic caracteristic. By default, it's equal to 0, but
                for real pump there is always some thermic transfert.

        Raises : 
            TypeError : 
                It's raised by the function typeErrorAtEntering when the Types and the object
                don't match with the type and the object defined.
            ValueError: 
                If the variables haven't the physical reality, example : hydraulicDiameter < 0

        """

        typeErrorAtEntering(inputTemperature,Types = [float, type(None)], message = "the inputTemperature must be a float or a None type") 
        if inputTemperature == None:
            variables = [False, True, True, True]
        
        #initalisation of the class Dipole with the informations
        Dipole.__init__(self, name = name, hydraulicDiameter = hydraulicDiameter, crossSectionalArea = crossSectionalArea, 
                        downstreamPole = downstreamPole, upstreamPole = upstreamPole, flow = Flow(fluid = fluid, flowRate = flowRate,
                        inputTemperature = inputTemperature), variables=[False,True, False, True], caracteristics=[False, True], 
                        exchanger = False)

        typeErrorAtEntering( thermicPower, message = "the thermicPower must be a float number")
      
        #if the input temperature is fixed, the input temperature is fixed as a variable :
        if inputTemperature == None:
            variables = [False, True, True, True]
        # the temperature is fixed in the object link to the pump :
        downstreamPole.temperature = inputTemperature
        self.flow.inputTemperature = inputTemperature

        #definition of the thermic caracteristic
        def buildThermicCaracteristic():
            thermalPower = thermicPower
            def thermicCaracteristic(flowRate = None, fluid = None):
                """ the method thermicCaracteristic 

                Note: 
                    When this method is defined, it take into account the caracteristics
                    of the object initialised from the class Dipole, the flow rate and the 
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
                    thermalPower(type:float): It's the thermal energy transfered to the fluid
                    unity : J
                                
                Raises: 
                    TypeError : If flowRate is not a float 


                """
                #takes the intern variables if undefined
                if flowRate == None:
                    flowRate = self.flow.flowRate
                if fluid == None:
                    fluid = self.flow.fluid

                return thermalPower
        
        self.thermicCaracteristic = buildThermicCaracteristic()
        self.__thermicPower = thermicPower
    
    @property 
    def thermicPower(self): 
        """ get and set allows the user to modify the private thermicPower attribute """
        return self.__thermicPower

    @thermicPower.setter 
    def thermicPower(self,thermicPower): 
        typeErrorAtEntering(thermicPower, message = "the thermicPower must be a float number")
        #definition of the thermic caracteristic
        def buildThermicCaracteristic():
            thermalPower = thermicPower
            def thermicCaracteristic(flowRate = None, fluid = None):
                """ the method thermicCaracteristic 

                Note: 
                    When this method is defined, it take into account the caracteristics
                    of the object initialised from the class Dipole, the flow rate and the 
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
                    thermalPower(type:float): It's the thermal energy transfered to the fluid
                    unity : J
                                
                Raises: 
                    TypeError : If flowRate is not a float 


                """
                #takes the intern variables if undefined
                if flowRate == None:
                    flowRate = self.flow.flowRate
                if fluid == None:
                    fluid = self.flow.fluid

                return thermalPower
        self.thermicCaracteristic = buildThermicCaracteristic()
        self.__thermicPower = thermicPower

        



class Pump(Dipole):
    """The Pump class represents the caracteristics of a pump 
    where the flowRate evolve with the overPressure deliver. It's a child class of the 
    class Dipole.

    Attributes:   
        flowRates(type:list of float or :obj:array of np.float64): 
                This parameter indicates the x coordonate of the caracteristic of the pump.
                It allows the code to create a caracteristic function.
                unity:m³/s

        overPressures(type:list of float or :obj:array of np.float64): 
            This parameter indicates the z coordonate of the caracteristic of the pump.
            It allows the code to create a caracteristic function.
            unity:Pa    
            
        thermicPower(type:float,Nonetype or :obj:np.float64): 
            This parameter allows the class to build a constant thermic caracteristic. By default, it's equal to 0, but
            for real pump there is always some thermic transfert.
            

    """
    def __init__(self,name = 'Pump', hydraulicDiameter = None, crossSectionalArea = None ,flowRates = [], 
                overPressures = [], fluid = Fluid(), inputTemperature = None, thermicPower = 0.0, 
                downstreamPole = Pole("downstream pole"), upstreamPole = Pole("upstream Pole"), temperatureDifference = 0.0) : 
        """Class Pump __init__ method : 
        
        Note : 
            The class Pump is used when the caracteristic of the pump is knew, to test the real application
            of a pump.

            the __init__ method offers the opportunity to give the attributes of the idealpump object.

        Args:
            name( type:any ): 
                this parameters indicates the private attribute name. This parameter gives 
                the user the opportunity to organise his dipole objects.

            hydraulicDiameter (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute hydraulicDiameter of the 
                dipole object initialised from the class Dipole. 
                It represents the caracteristical length in the dipole to computes the 
                reynolds or other important numbers.
                unity : m

            crossSectionnalArea (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute crossSectionalArea of the object 
                initialised from the Dipole class. 
                It represents the sectionnal area of the flow, it's an important parameter to compute 
                the average velocity of the fluid into the dipole.
                unity : m²

            downstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[0] of the 
                object initialised from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid enters into the dipole (or the
                dipole entry). By default all the states attributes of the object downstreamPole 
                are undefined (with the None variable).

            upstreamPole (:obj:Pole): 
                This parameter indicates the private attribute Poles[1] of the 
                object initialised from the Edge class (the parent class of Dipole). 
                It represents the pole where the fluid exits the dipole (or the
                dipole outlet). By default all the states attributes of the object 
                upstreamPole are undefined (with the None variable).

            flowRates(type:list of float or :obj:array of np.float64): 
                This parameter indicates the x coordonate of the caracteristic of the pump.
                It allows the code to create a caracteristic function.
                unity:m³/s

            overPressures(type:list of float or :obj:array of np.float64): 
                This parameter indicates the z coordonate of the caracteristic of the pump.
                It allows the code to create a caracteristic function.
                unity:Pa

            fluid(:obj: Fluid): 
                This parameter indicates the private attribute fluid of the attribute object flow, it's initialised 
                from the class Flow. 
                It represents the state of the flow of the dipole. By default all the states
                attributes of the object flow are undefined (with the None variable).
            
            inputTemperature(type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute inputTemperature of the attribute object flow, it's initialised 
                from the class Flow. 
                It the temperature of the fluid pumped, it's not necessary to enter this variable here, but in the majority
                of case the pump are at the input of the Hydraulic Network.
                unity:°C
            
            thermicPower(type:float,Nonetype or :obj:np.float64): 
                This parameter allows the class to build a constant thermic caracteristic. By default, it's equal to 0, but
                for real pump there is always some thermic transfert.

        Raises : 
            TypeError : 
                It's raised by the function typeErrorAtEntering when the Types and the object
                don't match with the type and the object defined.
            ValueError: 
                If the variables haven't the physical reality, example : hydraulicDiameter < 0

        """
        typeErrorAtEntering(inputTemperature,Types = [float, type(None)], message = "the inputTemperature must be a float or a None type") 
        if inputTemperature == None:
            variables = [True, True, True, True]

        #the informations are fixed in the parent class Dipole
        Dipole.__init__(self, name, hydraulicDiameter, crossSectionalArea, downstreamPole, upstreamPole, 
        flow = Flow(fluid = fluid, inputTemperature = inputTemperature), variables=[True,True, False, True],
        caracteristics=[True, True], exchanger=False)

        #raise of exceptions
        typeErrorAtEntering(flowRates, Types = [list], Classes=[np.ndarray],
                            message = "the flowRates must be a list of float") 
        for flowRate in flowRates:
            typeErrorAtEntering(flowRate, message = "the flowRates must be a list of float") 

        typeErrorAtEntering(overPressures, Types = [list], Classes=[np.ndarray],
                            message = "the overPressures must be a list of float") 
        for overPressure in overPressures:
            typeErrorAtEntering(overPressure, message = "the overPressures must be a list of float") 

        downstreamPole.temperature = inputTemperature

        #build of the caracteristic with the interpollation of the points :
        def buildingHydraulicCaracteristic():
            #calling of the function DataAnalysis.interpolation which build the function 
            carac = DataAnalysis.interpolation(flowRates,overPressures)
            #creation of the function :
            def hydraulicCaracteristic(flowRate = None):
                """ the method hydraulicCaracteristic 

                Note: 
                    When this method is defined, it take into account the hydraulicCaracteristics
                    of the object initialised from the class Dipole and the flow rate and the 
                    fluid to compute the difference of pressure between the outlet and the
                    inlet of the dipole. 
                    This hydraulicCaracteristic can be deduced from the hydraulic correlation, if it's
                    defined.
                Args:
                    flowRate(type:float or None type):
                        If the flowRate is equal to None, the flowRate use for the calcul
                        is the flowRate from the flow object attribute.
                        unity: defined by flowRateUnity

                Returns:
                    pressureDifference(type:float):
                        unity: m³/s
                                
                Raises: 
                    TypeError : If flowRate is not a float 
                    TypeError : If fluid is not a Fluid object


                """
                #test if the flowRate is defined
                if flowRate == None:
                    flowRate = self.flow.flowRate
                typeErrorAtEntering(flowRate, message = 'the flowRate must be a float number')

                return carac(flowRate)
            return hydraulicCaracteristic
        self.hydraulicCaracteristic = buildingHydraulicCaracteristic()

        typeErrorAtEntering( thermicPower, message = "the thermicPower must be a float number")
        #definition of the thermic caracteristic
        def buildThermicCaracteristic():
            thermalPower = thermicPower
            def thermicCaracteristic(flowRate = None, fluid = None):
                """ the method thermicCaracteristic 

                Note: 
                    When this method is defined, it take into account the caracteristics
                    of the object initialised from the class Dipole, the flow rate and the 
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
                    thermalPower(type:float): It's the thermal energy transfered to the fluid
                    unity : J
                                
                Raises: 
                    TypeError : If flowRate is not a float 


                """
                #takes the intern variables if undefined
                if flowRate == None:
                    flowRate = self.flow.flowRate
                if fluid == None:
                    fluid = self.flow.fluid

                return thermalPower
            
    @property 
    def thermicPower(self): 
        """ get and set allows the user to modify the private thermicPower attribute """
        return self.__thermicPower

    @thermicPower.setter 
    def thermicPower(self,thermicPower): 
        typeErrorAtEntering(thermicPower, message = "the thermicPower must be a float number")
        #definition of the thermic caracteristic
        def buildThermicCaracteristic():
            thermalPower = thermicPower
            def thermicCaracteristic(flowRate = None, fluid = None):
                """ the method thermicCaracteristic 

                Note: 
                    When this method is defined, it take into account the caracteristics
                    of the object initialised from the class Dipole, the flow rate and the 
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
                    thermalPower(type:float): It's the thermal energy transfered to the fluid
                    unity : J
                                
                Raises: 
                    TypeError : If flowRate is not a float 


                """
                #takes the intern variables if undefined
                if flowRate == None:
                    flowRate = self.flow.flowRate
                if fluid == None:
                    fluid = self.flow.fluid

                return thermalPower
        self.thermicCaracteristic = buildThermicCaracteristic()
        self.__thermicPower = thermicPower

    def hydraulicPower(self, flowRate = None):
        """ the method hydraulicPower 

                Note: 
                    When this method is defined, it take into account the caracteristics
                    of the object initialised from the class Dipole, the flow rate and the 
                    fluid to compute the hydraulic power of the pump.
                Args:
                    flowRate(type:float or None type):
                        If the flowRate is equal to None, the flowRate use for the calcul
                        unity:m³/s

                Returns:
                    hydraulicPower(type:float): It's hydraulic energy raised by the pump
                    unity : J
                                
                Raises: 
                    TypeError : If flowRate is not a float 


        """
        if flowRate == None:
            flowRate = self.flow.flowRate
        typeErrorAtEntering(flowRate, message = 'the flowRate must be a float number')
        return self.hydraulicCaracteristic(flowRate) * flowRate

#tests



# print(pipe.methodCaracteristic(500, eau, "m3/h", "mCE"))

# flowRate = [i/10 for i in range(1,20000)]
# headLoss = [pipe.methodCaracteristic(q, eau, "m3/h", "mCE") for q in flowRate]

# plt.plot(flowRate, headLoss)
# plt.show()
