"""The module Flow allows the user to creat flow objects and SeaWater objects"""
import sys
sys.path.append("./Classes")
from FluidFolder.Fluid import Fluid
sys.path.append(".")
from ExceptionsAndErrors import typeErrorAtEntering

class Flow:

    def __init__(self, flowRate = None, pressureDifference = None, inputTemperature = None, averageTemperature = None, outletTemperature = None, fluid = Fluid()) : 
        """Class Flow __init__ method : 
        
        Note : 
            The Flow class is used to give the state of the flow in a dipole object.
            the __init__ method offers the opportunity to give the attributes of the flow object.

        Args:
            flowRate (type:float or :obj:np.float64): This parameter indicates the private attribute flowRate of the 
                                    object created from the class Flow. 
                                    unity : m³/s
            pressureDifference (type:float or :obj:np.float64): This parameter indicates the private attribute pressureDifference of the 
                                    object created from the classe Flow. It represents the difference of pressure between the inlet and the
                                    outlet of the dipole the object flow is associated with as an attribute.
                                    unity : Pascal.
            inputTemperature (type:float or :obj:np.float64): This parameter indicates the private attribute inputTemperature of the 
                                    object created from the classe Flow. It represents the temperature of the fluid when it enters 
                                    into the dipole the flow is associated with as an attribute.
                                    unity : °C
            averageTemperature (type:float or :obj:np.float64): This parameter indicates the private attribute averageTemperature of the 
                                    object created from the classe Flow. It represents the temperature of the average temperature of the
                                    into the dipole the flow is associated with as an attribute.
                                    unity : °C
            outletTemperature (type:float or :obj:np.float64): This parameter indicates the private attribute outletTemperature of the 
                                    object created from the classe Flow. It represents the temperature of the fluid when it exits
                                    the dipole the flow is associated with as an attribute.
                                    unity : °C
            fluid(:obj: Fluid): This parameter indicates the private attribute fluid of the obkect created from the class Flow. It represents
                                the fluid which flows into the dipole the flow object is associated with as an attribtute.
                                    
                        
        Raises : 
            TypeError : it's raised by the function typeErrorAtEntering.

        """
        typeErrorAtEntering(flowRate,types = [float, type(None)], message = "the flow rate must be a float or a None type")
        self.__flowRate = flowRate

        typeErrorAtEntering(pressureDifference,types = [float, type(None)], message = "the difference of pressure must be a float number or a None type")
        self.__pressureDifference = pressureDifference

        typeErrorAtEntering(inputTemperature,types = [float, type(None)], message = "the input temperature must be a float or a None type")
        self.__inputTemperature = inputTemperature
        
        typeErrorAtEntering(averageTemperature,types = [float, type(None)], message = "the average temperature must be a float or a None type")
        self.__averageTemperature = averageTemperature

        typeErrorAtEntering(outletTemperature,types = [float, type(None)], message = "the outlet temperature must be a float or a None type")
        self.__outletTemperature = outletTemperature
        
        typeErrorAtEntering(flowRate,types = [], instances = [Fluid], message = "the fluid must be a Fluid object")
        self.__fluid = fluid


    @property 
    def flowRate(self): 
        """ get method and set method to access the private variable flowRate """
        return self.__flowRate

    @flowRate.setter 
    def flowRate(self,flowRate): 
        typeErrorAtEntering(flowRate,types = [float, type(None)], message = "the flow rate must be a float or a None type")
        self.__flowRate = flowRate

    @property 
    def pressureDifference(self): 
        """ get method and set method to access the private variable pressureDifference """
        return self.__pressureDifference

    @pressureDifference.setter 
    def pressureDifference(self,pressureDifference): 
        typeErrorAtEntering(pressureDifference,types = [float, type(None)], message = "the difference of pressure must be a float number or a None type")
        self.__pressureDifference = pressureDifference

    @property 
    def inputTemperature(self): 
        """ get method and set method to access the private variable inputTemperature """
        return self.__inputTemperature

    @inputTemperature.setter 
    def inputTemperature(self,inputTemperature): 
        typeErrorAtEntering(inputTemperature,types = [float, type(None)], message = "the input temperature must be a float or a None type")
        self.__inputTemperature = inputTemperature

    @property 
    def averageTemperature(self):
        """ get method and set method to access the private variable averageTemperature """ 
        return self.__averageTemperature

    @averageTemperature.setter 
    def averageTemperature(self,averageTemperature): 
        typeErrorAtEntering(averageTemperature,types = [float, type(None)], message = "the average temperature must be a float or a None type")
        self.__averageTemperature = averageTemperature

    @property 
    def outletTemperature(self): 
        """ get method and set method to access the private variable outletTemperature """
        return self.__outletTemperature

    @outletTemperature.setter 
    def outletTemperature(self,outletTemperature): 
        typeErrorAtEntering(outletTemperature,types = [float, type(None)], message = "the outlet temperature must be a float or a None type")
        self.__outletTemperature = outletTemperature

    @property 
    def fluid(self):
        """ get method and set method to access the private variable fluid """
        return self.__fluid

    @fluid.setter 
    def fluid(self,fluid): 
        typeErrorAtEntering(flowRate,types = [], instances = [Fluid], message = "the fluid must be a Fluid object")
        self.__fluid = fluid




    
    
