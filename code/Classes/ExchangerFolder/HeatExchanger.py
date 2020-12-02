""" Into the module HeatExchanger are initialised the classes :
        - heatExchanger
        - plateHeatExchanger



 """
import sys
sys.path.append("./Classes")
sys.path.append(".")
import numpy as np
from DipoleFolder.Dipole import Dipole, PlateHeatExchangerSide, Pole
from math import pi
from HydraulicThermicCalculus import HydraulicThermicCalculus
from FluidFolder.Fluid import Fluid, SeaWater
from math import exp
from math import log
from Calculus import Resolve
from FlowFolder.Flow import Flow
from ExceptionsAndErrors import typeErrorAtEntering

class HeatExchanger:
    def __init__(self,name = 'heat exchanger', materialConductivity = 21.9,exchangeSurface = 600, 
                hydraulicDipoleCold = None,hydraulicDipoleWarm = None, globalThermicCoefficient = 5000, 
                downstreamPoleCold = Pole('downstreamPoleCold'), upstreamPoleCold = Pole('upstreamPoleCold'), 
                downstreamPoleWarm = Pole('downstreamPoleWarm'), upstreamPoleWarm = Pole('upstreamPoleWarm')) : 
        """Class HeatExchanger __init__ method : 
        
        Note : 
            The heatExchanger class is used to represent any thermic transfert between Warm different flows.
 
            the __init__ method offers the opportunity to give the attributes of the dipole object.

        Args:
            name( type:any ): 
                this parameters indicates the private attribute name. This parameter gives 
                        the user the opportunity to organise his dipole objects.

            materialConductivity (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute materialConductivity of the 
                dipole object initialised from the class Dipole. 
                It represents how much the material between the 2 flows can conduct the heat.
                By default it's equal to 21.9 because it's the titanium conductivity.
                unity : W/m/K

            globalThermicCoefficient(type:float,Nonetype or :obj:np.float64): 
                This parameter indicate the initialisation of the private attribute 
                globalThermicCoefficient of the class. 
                It represents the coefficient K in the formula :
                    Q = K S DTLM
                where:
                    - Q is the thermal power exchanged
                    - S is the exchange surface 
                    - DTLM is average logithmic difference between the 2 flows.
                unity : W/m²/K

            exchangeSurface(type:float,Nonetype or :obj:np.float64): 
                This parameter indicate the initialisation of the private attribute 
                exchangeSurface of the class. 
                It represents contact surface of between the 2 flows.
                unity : m²

            hydraulicDipoleCold( :obj:Dipole ): 
                This parameter indicate the attribute hydraulicDipoleCold of the class. 
                It represents one of the 2 dipole where one of the flow is flowing.
                It is the dipole which the fluid enters with the coldest temperature of the 2. 

            hydraulicDipoleWarm( :obj:Dipole )
                This parameter indicate the attribute hydraulicDipoleCold of the class. 
                It represents one of the 2 dipole where one of the flow is flowing.
                It is the dipole which the fluid enters with the warmest temperature of the 2. 

            downstreamPoleCold (:obj:Pole): 
                it's the attribute downstreamPole of the attribute hydraulicDipoleCold.

            upstreamPoleCold (:obj:Pole): 
                it's the attribute upstreamPole of the attribute hydraulicDipoleCold.

            downstreamPoleWarm (:obj:Pole): 
                it's the attribute downstreamPole of the attribute hydraulicDipole2.

            upstreamPoleWarm (:obj:Pole): 
                it's the attribute upstreamPole of the attribute hydraulicDipole2.

        Raises : 
            TypeError : 
                It's raised by the function typeErrorAtEntering when the Types and the object
                don't match with the type and the object defined.
            ValueError: 
                If the variables haven't the physical reality, example : hydraulicDiameter < 0

        """
        if hydraulicDipoleCold == None:
            hydraulicDipoleCold = Dipole('hydraulc dipole Cold', upstreamPole=upstreamPoleCold,downstreamPole=downstreamPoleCold)
        if hydraulicDipoleWarm == None: 
            hydraulicDipoleWarm = Dipole('hydraulic dipole Warm', upstreamPole = upstreamPoleWarm, downstreamPole=downstreamPoleWarm)

        typeErrorAtEntering(hydraulicDipoleCold,Types = [], Classes = [Dipole], message = "the hydraulic dipole Cold must be a dipole")

        typeErrorAtEntering(hydraulicDipoleWarm,Types = [], Classes = [Dipole], message = "the hydraulic dipole Warm must be a dipole")

        typeErrorAtEntering(materialConductivity,Types = [float, type(None)], message = "the materialConductivity must be a float or a None type")

        typeErrorAtEntering(globalThermicCoefficient,Types = [float, type(None)], message = "the globalThermicCoefficient must be a float or a None type")

        typeErrorAtEntering(exchangeSurface,Types = [float, type(None)], message = "the exchangeSurface must be a float or a None type")

        self.__materialConductivity = materialConductivity
        self.__exchangeSurface = exchangeSurface
        self.__hydraulicDipoleCold = hydraulicDipoleCold
        self.__hydraulicDipoleWarm = hydraulicDipoleWarm
        self.__globalThermicCoefficient = globalThermicCoefficient

    @property 
    def materialConductivity(self): 
       """ get method and set method to access the private variable materialConductivity """
        return self.__materialConductivity

    @materialConductivity.setter 
    def materialConductivity(self,materialConductivity): 
        typeErrorAtEntering(materialConductivity,Types = [float, type(None)], message = "the materialConductivity must be a float or a None type")
        self.__materialConductivity = materialConductivity

    @property 
    def exchangeSurface(self): 
        """ get method and set method to access the private variable exchangeSurface """
        return self.__exchangeSurface

    @exchangeSurface.setter 
    def exchangeSurface(self,exchangeSurface): 
        typeErrorAtEntering(exchangeSurface,Types = [float, type(None)], message = "the exchangeSurface must be a float or a None type")
        self.__exchangeSurface = exchangeSurface

    @property 
    def hydraulicDipoleCold(self): 
        """ get method and set method to access the private variable hydraulicDipoleCold """
        return self.__hydraulicDipoleCold

    @hydraulicDipoleCold.setter 
    def hydraulicDipoleCold(self,hydraulicDipoleCold): 
        typeErrorAtEntering(hydraulicDipoleCold,Types = [], Classes = [Dipole], message = "the hydraulic dipole Cold must be a dipole")
        self.__hydraulicDipoleCold = hydraulicDipoleCold

    @property 
    def hydraulicDipoleWarm(self): 
        """ get method and set method to access the private variable hydraulicDipoleWarm """
        return self.__hydraulicDipoleWarm

    @hydraulicDipoleWarm.setter 
    def hydraulicDipoleWarm(self,hydraulicDipoleWarm): 
        typeErrorAtEntering(hydraulicDipoleWarm,Types = [], Classes = [Dipole], message = "the hydraulic dipole Warm must be a dipole")
        self.__hydraulicDipoleWarm = hydraulicDipoleWarm

    @property 
    def globalThermicCoefficient(self): 
        """ get method and set method to access the private variable globalThermicCoefficient """
        return self.__globalThermicCoefficient

    @globalThermicCoefficient.setter 
    def globalThermicCoefficient(self,hydraulicDipoleWarm): 
        typeErrorAtEntering(globalThermicCoefficient,Types = [float, type(None)], message = "the globalThermicCoefficient must be a float or a None type")
        self.__globalThermicCoefficient = globalThermicCoefficient

    def NUT(self, globalThermicCoefficient = None, exchangeSurface = None, volumetricMassCold = None, 
            thermicCapacityCold = None, flowRateCold = None, volumetricMassWarm = None, thermicCapacityWarm = None, 
            flowRateWarm = None):
        """ the method NUT 

        Note: 
            this method allow the class to calcul the number of transfert unit. 
        Args:
            globalThermicCoefficient(type:float,Nonetype or :obj:np.float64): 
                This parameter indicate the initialisation of the private attribute 
                globalThermicCoefficient of the class. 
                It represents the coefficient K in the formula :
                    Q = K S DTLM
                where:
                    - Q is the thermal power exchanged
                    - S is the exchange surface 
                    - DTLM is average logithmic difference between the 2 flows.
                unity = W / m² / K
            
            exchangeSurface(type:float,Nonetype or :obj:np.float64): 
                This parameter indicate the initialisation of the private attribute 
                exchangeSurface of the class. 
                It represents contact surface of between the 2 flows.
                unity = m²

            volumetricMassCold(type:float, NoneType or :obj: np.float64)
            thermicCapacityCold(type:float, NoneType or :obj: np.float64)
            flowRateCold(type:float, NoneType or :obj: np.float64)
                These 3 parameters represent the flow parameters of the flow Cold.
                if undefined, the parameters are taken from the hydraulicDipoleCold.flow
            
            volumetricMassWarm(type:float, NoneType or :obj: np.float64)
            thermicCapacityWarm(type:float, NoneType or :obj: np.float64)
            flowRateWarm(type:float, NoneType or :obj: np.float64)
                These 3 parameters represent the flow parameters of the flow Warm.
                if undefined, the parameters are taken from the hydraulicDipoleWarm.flow

        Returns:
            NUT(type:float) 
            None when the method is not defined
                        
        Raises: 
            TypeError : If types don't match.


        """
        if globalThermicCoefficient == None:
            globalThermicCoefficient = self.globalThermicCoefficient
        if exchangeSurface == None:
            exchangeSurface = self.exchangeSurface
        
        #taking the parameters from flowCold
        if volumetricMassCold == None:
            volumetricMassCold = self.hydraulicDipoleCold.flow.fluid.volumetricMass
        if thermicCapacityCold == None:
            thermicCapacityCold = self.hydraulicDipoleCold.flow.fluid.thermicCapacity
        if flowRateCold == None:
            flowRateCold = self.hydraulicDipoleCold.flow.flowRate
        
        #taking the parameters from flowWarm
        if volumetricMassWarm == None:
            volumetricMassWarm = self.hydraulicDipoleWarm.flow.fluid.volumetricMass
        if thermicCapacityWarm == None:
            thermicCapacityWarm = self.hydraulicDipoleWarm.flow.fluid.thermicCapacity
        if flowRateWarm == None:
            flowRateWarm = self.hydraulicDipoleWarm.flow.flowRate

        #raise of the exceptions :

        typeErrorAtEntering(globalThermicCoefficient, message = "the globalThermicCoefficient must be a float or a None type")

        typeErrorAtEntering(exchangeSurface, message = "the exchangeSurface must be a float or a None type")

        typeErrorAtEntering(volumetricMassCold, message = "the volumetricMassCold must be a float or a None type")
        typeErrorAtEntering(thermicCapacityCold, message = "the thermicCapacityCold must be a float or a None type")
        typeErrorAtEntering(flowRateCold, message = "the flowRateCold must be a float or a None type")

        typeErrorAtEntering(volumetricMassWarm, message = "the volumetricMassWarm must be a float or a None type")
        typeErrorAtEntering(thermicCapacityWarm, message = "the thermicCapacityWarm must be a float or a None type")
        typeErrorAtEntering(flowRateWarm, message = "the flowRateWarm must be a float or a None type")

        hydraulicCapacityCold = flowRateCold * thermicCapacityCold * volumetricMassCold
        hydraulicCapacityWarm = flowRateWarm * thermicCapacityWarm * volumetricMassWarm

        hydraulicCapacity = min(hydraulicCapacityCold, hydraulicCapacityWarm)

        return globalThermicCoefficient * exchangeSurface / hydraulicCapacity
    
    def DTLM(self, outletColdTemperature = None, outletWarmTemperature = None, 
            entryColdTemperature = None, entryWarmTemperature = None):
        """ the method DTLM 

        Note: 
            this method allow the class to calcul the logarithmic mean temperature 
            difference between the 2 flows. 
            It represents the coefficient DTLM in the formula :
                    Q = K S DTLM
                where:
                    - Q is the thermal power exchanged
                    - S is the exchange surface 
                    - K is the global thermic exchange coefficient
        Args:
            outletColdTemperature(type:float,Nonetype or :obj:np.float64): 
                It's the temperature at the end of the dipole where the 
                temperature of the fluid was the coldest. If it's undefined
                it take one of the temperature of one of the hydraulic dipoles.
            unity:°C

            outletWarmTemperature(type:float,Nonetype or :obj:np.float64): 
                It's the temperature at the end of the dipole where the 
                temperature of the fluid was the warmest. If it's undefined
                it take one of the temperature of one of the hydraulic dipoles.
            unity:°C

            entryColdTemperature(type:float,Nonetype or :obj:np.float64): 
                It's the temperature at the end of the dipole where the 
                temperature of the fluid was the coldest. If it's undefined
                it take one of the temperature of one of the hydraulic dipoles.
            unity:°C

            entryWarmTemperature(type:float,Nonetype or :obj:np.float64): 
                It's the temperature at the end of the dipole where the 
                temperature of the fluid was the warmest. If it's undefined
                it take one of the temperature of one of the hydraulic dipoles.
            unity:°C

        Returns:
            DTLM(type:float) :
                unity:°C
                        
        Raises: 
            TypeError : If types don't match.


        """
        if entryColdTemperature == None:
            entryColdTemperature = self.hydraulicDipoleCold.flow.inputTemperature
        if outletColdTemperature == None:
            outletColdTemperature = self.hydraulicDipoleCold.flow.outletTemperature
        
        if entryWarmTemperature == None:
            entryWarmTemperature = self.hydraulicDipoleWarm.flow.inputTemperature
        if outletWarmTemperature == None:
            outletWarmTemperature = self.hydraulicDipoleWarm.flow.outletTemperature

        #raise exceptions :

        typeErrorAtEntering(entryColdTemperature, message = "the entryColdTemperature must be a float or a None type")
        typeErrorAtEntering(outletColdTemperature, message = "the outletColdTemperature must be a float or a None type")

        typeErrorAtEntering(entryWarmTemperature, message = "the entryWarmTemperature must be a float or a None type")
        typeErrorAtEntering(outletWarmTemperature, message = "the outletWarmTemperature must be a float or a None type")

        temperatureDifference1 = entryWarmTemperature - outletColdTemperature
        temperatureDifference2 = outletWarmTemperature - entryColdTemperature

        DTLM = (temperatureDifference1 - temperatureDifference2) / log(temperatureDifference1 / temperatureDifference2)
        return DTLM
    
    

    
    def stateEquation(self, flowRateCold = None, flowRateWarm = None, inputTemperatureCold = None, inputTemperatureWarm = None,
                        outletTemperatureCold = None, outletTempertureWarm = None, variables = [False, False, False, False, True, True],
                        averagePressureCold = None, averaPressureWarm = None, modify = True):
        """ the method stateEquation

        Note: 
            this method allow the class to calcul the variables wanted
            from the others fixed variables.
        Args:
            flowRateCold(type:float,Nonetype or :obj:np.float64): 
                If it's a fixed variable, it's the fixed cold flow rate
                which enters in the exhanger. If it's a variable, it's
                an estimation of the flowRate expected.
            unity:m³/s

            flowRateWarm(type:float,Nonetype or :obj:np.float64): 
                If it's a fixed variable, it's the fixed warm flow rate
                which enters in the exhanger.If it's a variable, it's
                an estimation of the flowRate expected.
            unity:m³/s

            inputTemperatureCold(type:float,Nonetype or :obj:np.float64): 
                If it's a fixed variable, it's the fixed cold temperature
                which enters in the exhanger. If it's a variable, it's
                an estimation of the temperature expected.
            unity:°C

            inputTemperatureWarm(type:float,Nonetype or :obj:np.float64): 
                If it's a fixed variable, it's the fixed warm temperature
                which enters in the exhanger. If it's a variable, it's
                an estimation of the temperature expected.
            unity:°C

            outletTemperatureCold(type:float,Nonetype or :obj:np.float64): 
                If it's a fixed variable, it's the fixed cold temperature
                which exits the exchanger. If it's not fixed, it's an
                estimation of the temperature expected.
            unity:°C

            outletTemperatureWarm(type:float,Nonetype or :obj:np.float64): 
                If it's a fixed variable, it's the fixed cold temperature
                which exits the exchanger. If it's not fixed, it's an
                estimation of the temperature expected.
            unity:°C

            variables(type: list of booleans):
                - if variables[0] == False : flowRateCold is fixed else:
                it's a variable
                - if variables[1] == False : flowRateWarm is fixed else:
                it's a variable
                - if variables[2] == False : inputTemperatureCold is fixed else:
                it's a variable
                - if variables[3] == False : inputTemperatureWarm is fixed else:
                it's a variable
                - if variables[4] == False : outletTemperatureCold is fixed else:
                it's a variable
                - if variables[5] == False : outletTemperatureWarm is fixed else:
                it's a variable

            averagePressureCold(type:float,Nonetype or :obj:np.float64): 
                It's parameter wich allows the class fluid to compute its
                states variables
            unity:°C

            averagePressureWarm(type:float,Nonetype or :obj:np.float64): 
                It's parameter wich allows the class fluid to compute its
                states variables
            unity:°C


        Returns:
            flowRateCold(type:float,Nonetype or :obj:np.float64): 
            unity:m³/s

            flowRateWarm(type:float,Nonetype or :obj:np.float64): 
            unity:m³/s

            inputTemperatureCold(type:float,Nonetype or :obj:np.float64): 
            unity:°C

            inputTemperatureWarm(type:float,Nonetype or :obj:np.float64): 
            unity:°C

            outletTemperatureCold(type:float,Nonetype or :obj:np.float64): 
            unity:°C

            outletWarmTemperature(type:float,Nonetype or :obj:np.float64): 
            unity:°C

            exchangedThermicPower(type:float):
            unity: W
                        
        Raises: 
            TypeError : If types don't match.


        """
        #definition of the variables :
        flowCold = self.hydraulicDipoleCold.flow
        flowWarm = self.hydraulicDipoleWarm.flow

        #cold side
        if flowRateCold == None:
            flowRateCold = flowCold.flowRate
        if inputTemperatureCold == None:
            inputTemperatureCold = flowCold.inputTemperature
        if outletTemperatureCold == None:
            outletTemperatureCold = flowCold.outletTemperature
        if averagePressureCold == None:
            try:
            averagePressureCold = self.hydraulicDipoleCold.downstreamPole.pressure + \
                                self.hydraulicDipoleCold.upstreamPole.pressure
            except TypeError:
                #if the pressure is not defined, gives the atmospheric pressure value : 
                averagePressureCold = 10 ** 5 
        
        #warm side
        if flowRateWarm == None:
            flowRateWarm = flowWarm.flowRate
        if inputTemperatureWarm == None:
            inputTemperatureWarm = flowWarm.inputTemperature
        if outletTemperatureWarm == None:
            outletTemperatureWarm = flowWarm.outletTemperature
        if averagePressureWarm == None:
            try:
            averagePressureWarm = self.hydraulicDipoleWarm.downstreamPole.pressure + \
                                self.hydraulicDipoleWarm.upstreamPole.pressure
            except TypeError:
                #if the pressure is not defined, gives the atmospheric pressure value : 
                averagePressureWarm = 10 ** 5 
        
        #raising exceptions 

        #coldside
        typeErrorAtEntering(flowRateCold, message = "the flowRateCold must be a float number")
        typeErrorAtEntering(inputTemperatureCold, message = "the inputTemperatureCold must be a float number")
        typeErrorAtEntering(outletTemperatureCold, message = "the outletTemperatureCold must be a float number")
        #warmside
        typeErrorAtEntering(flowRateWarm, message = "the flowRateWarm must be a float number")
        typeErrorAtEntering(inputTemperatureWarm, message = "the inputTemperatureWarm must be a float number")
        typeErrorAtEntering(outletTemperatureWarm, message = "the outletTemperatureWarm must be a float number")

        
        #taking the function from the fluid objects by redefining them
        #cold side
        if isinstance(flowCold.fluid, SeaWater):
            salinity = flowCold.fluid.salinity
            volumetricMassCold = lambda T, P: flowCold.fluid.volumetricMassEvolution(T, P, salinity)
            dynamicViscosityCold = lambda T, P: flowCold.fluid.dynamicViscosityEvolution(T, P, salinity)
            thermicCapacityCold = lambda T, P: flowCold.fluid.thermicCapacityEvolution(T, P, salinity)
            thermicConductivityCold = lambda T, P: flowCold.fluid.thermicConductivityEvolution(T, P, salinity)
        else :
            volumetricMassCold = lambda T, P: flowCold.fluid.volumetricMassEvolution(T, P)
            dynamicViscosityCold = lambda T, P: flowCold.fluid.dynamicViscosityEvolution(T, P)
            thermicCapacityCold = lambda T, P: flowCold.fluid.thermicCapacityEvolution(T, P)
            thermicConductivityCold = lambda T, P: flowCold.fluid.thermicConductivityEvolution(T, P)
        
        #warm side
        if isinstance(flowWarm.fluid, SeaWater):
            salinity = flowWarm.fluid.salinity
            volumetricMassWarm = lambda T, P: flowWarm.fluid.volumetricMassEvolution(T, P, salinity)
            dynamicViscosityWarm = lambda T, P: flowWarm.fluid.dynamicViscosityEvolution(T, P, salinity)
            thermicCapacityWarm = lambda T, P: flowWarm.fluid.thermicCapacityEvolution(T, P, salinity)
            thermicConductivityWarm = lambda T, P: flowWarm.fluid.thermicConductivityEvolution(T, P, salinity)
        else :
            volumetricMassWarm = lambda T, P: flowWarm.fluid.volumetricMassEvolution(T, P)
            dynamicViscosityWarm = lambda T, P: flowWarm.fluid.dynamicViscosityEvolution(T, P)
            thermicCapacityWarm = lambda T, P: flowWarm.fluid.thermicCapacityEvolution(T, P)
            thermicConductivityWarm = lambda T, P: flowWarm.fluid.thermicConductivityEvolution(T, P)
        
        #taking the global thermic coefficient function by redefining it:
        def constructor():
            exchanger = self
            def K(flowRateCold, meanTemperatureCold, flowRateWarm, meanTemperatureWarm):
                #cold side
                caracteristicalVelocityCold = flowRateCold / exchanger.hydraulicDipoleCold.crossSectionalArea
                reynoldsNumberCold = HydraulicThermicCalculus.reynolds(exchanger.hydraulicDipoleCold.hydraulicDiameter,
                                                                         caracteristicalVelocityCold, 
                                                                         volumetricMassCold(meanTemperatureCold, averagePressureCold),
                                                                         dynamicViscosityCold(meanTemperatureCold, averagePressureCold)) 
                prandtlNumberCold = dynamicViscosityCold(meanTemperatureCold, averagePressureCold) \
                                     * thermicCapacityCold) / thermicConductivityCold(meanTemperatureCold, averagePressureCold)
                thermicConductivityColdFixed = thermicConductivityCold(meanTemperatureCold, averagePressureCold)
                #warm side 
                caracteristicalVelocityWarm = flowRateWarm / exchanger.hydraulicDipoleWarm.crossSectionalArea
                reynoldsNumberWarm = HydraulicThermicCalculus.reynolds(exchanger.hydraulicDipoleWarm.hydraulicDiameter,
                                                                         caracteristicalVelocityWarm, 
                                                                         volumetricMassWarm(meanTemperatureWarm, averagePressureWarm),
                                                                         dynamicViscosityWarm(meanTemperatureWarm, averagePressureWarm)) 
                prandtlNumberWarm = dynamicViscosityWarm(meanTemperatureWarm, averagePressureWarm) \
                                     * thermicCapacityWarm) / thermicConductivityWarm(meanTemperatureWarm, averagePressureWarm)
                thermicConductivityWarmFixed = thermicConductivityWarm(meanTemperatureWarm, averagePressureWarm)
                globalThermicCoefficient = exchanger.globalThermicCoefficient(reynoldsNumberCold = reynoldsNumberCold, prandtlNumberCold = prandtlNumberCold,
                                                                    thermicConductivityCold = thermicConductivityCold, reynoldsNumberWarm = reynoldsNumberWarm, 
                                                                    prandtlNumberWarm = prandtlNumberWarm, thermicConductivityWarm = thermicConductivityWarm)
                return globalThermicCoefficient
            return K
        K = constructor()

        #taking the exchange surface 
        exchangeSurface = self.exchangeSurface

        #taking the DTLM function by redefining it
        DTLM = lambda inputTemperatureCold, outletTemperatureCold, inputTemperatureWarm, outletTemperatureWarm :\
            self.DTLM(outletTemperatureCold, outletTemperatureWarm, inputTemperatureCold, inputTemperatureWarm)

        def stateEquations(flowRateCold, flowRateWarm, inputTemperatureCold, inputTemperatureWarm,
                        outletTemperatureCold, outletTempertureWarm):
            """ gives the 2 equations which an heat exchanger have to verify """
            #computing the mean temperature:
            meanTemperatureCold = inputTemperatureCold + outletTemperatureCold
            meanTemperatureWarm = inputTemperatureWarm + outletTemperatureWarm

            #computing of global thermic transfert coefficient:
            globalThermicTransfertCoefficient = K(flowRateCold, meanTemperatureCold, flowRateWarm, meanTemperatureWarm)

            #the energy conservation equation :
            thermalPowerCold = flowRateCold * thermicCapacityCold(meanTemperatureCold, averagePressureCold) \
                            * volumetricMassCold(meanTemperatureCold, averagePressureCold) * (outletTemperatureCold - inputTemperatureCold)
            thermalPowerWarm = flowRateWarm * thermicCapacityWarm(meanTemperatureWarm, averagePressureWarm) \
                            * volumetricMassWarm(meanTemperatureWarm, averagePressureWarm) * (inputTemperatureWarm - outletTemperatureWarm)
            EnergyEquation = (thermalPowerCold - thermalPowerWarm) / globalThermicTransfertCoefficient / exchangeSurface

            meanEnergy = thermalPowerCold + thermalPowerWarm
            #the DTLM equation
            DTLMequation = meanEnergy / globalThermicTransfertCoefficient / exchangeSurface \
                 - DTLM(inputTemperatureCold, outletTemperatureCold, inputTemperatureWarm, outletTemperatureWarm)

            return [EnergyEquation, DTLMequation]



    def efficacity(self, NUT = None, rapport = None):
    if NUT == None:
        NUT = self.NUT()
    if rapport == None:
        flow1 = self.hydraulicDipole1.flow
        flow2 = self.hydraulicDipole2.flow
        hydraulicCapacity1 = flow1.flowRate * flow1.fluid.thermicCapacity * flow1.fluid.volumetricMass
        hydraulicCapacity2 = flow2.flowRate * flow2.fluid.thermicCapacity * flow2.fluid.volumetricMass 
        rapport = min(hydraulicCapacity1 / hydraulicCapacity2, hydraulicCapacity2 / hydraulicCapacity1)
    if rapport != 1.0:
        efficacity = (1 - exp(- NUT * (1 - rapport))) / (1 - rapport * (- NUT * (1 - rapport))) 
    else :
        efficacity = NUT / (1 + NUT)
    return efficacity



class PlateExchanger(HeatExchanger):
    def __init__(self, name = 'plate heat exchanger', materialConductivity = 21.9,hydraulicDipoleCold = None, 
                hydraulicDipoleWarm = None, length = 2.5, width = 1.0, plateNumber = 385.0, Npasse = 1,
                plateThickness = 0.5,plateGap = 3.0,angle = 45.0,streakWaveLength = None, 
                downstreamPoleCold = Pole('downstreamPoleCold'), upstreamPoleWarm = Pole('upstreamPoleCold'), 
                downstreamPoleWarm = Pole('downstreamPoleWarm'), upstreamPoleWarm = Pole('upstreamPoleWarm'), 
                flowCold = Flow(), flowWarm = Flow()) : 
        """Class HeatExchanger __init__ method : 
        
        Note : 
            The heatExchanger class is used to represent any thermic transfert between Warm different flows.
 
            the __init__ method offers the opportunity to give the attributes of the dipole object.

        Args:
            name( type:any ): 
                this parameters indicates the private attribute name. This parameter gives 
                        the user the opportunity to organise his dipole objects.

            materialConductivity (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute materialConductivity of the 
                dipole object initialised from the class Dipole. 
                It represents how much the material between the 2 flows can conduct the heat.
                By default it's equal to 21.9 because it's the titanium conductivity.
                unity : W/m/K

            width (type:float,Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute width of the 
                plateHeatExchangerSide object initialised from the class PlateHeatExchangerSide. 
                It represents the caracteristical width of the exchanger.
                unity : m
            
            plateGap(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute plateGape of the object initialised from 
                the class PlateHeatExchangerSide of the hydraulic dipoles attributes. 
                unity:mm

            plateThickness(type:float, Nonetype or :obj:np.float64):
                This parameter indicates the private attribute plateThickness of the PlateExchanger class.
                It represents the thickness of the plates.
                unity:mm
            
            streakWaveLength(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute streakWaveLength of the object initialised from 
                the class PlateHeatExchangerSide of the hydraulic dipoles attributes. 
                It represents the Wave length of the relief of the heat echanger plates
                unIy:mm
            
            plateNumber(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute plateNumber of the object initialised from 
                the class PlateHeatExchangerSide of the hydraulic dipoles attributes. 
                It represents the number of plates of the heat exchanger
            
            angle(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute angle of the object initialised from 
                the class PlateHeatExchangerSide of the hydraulic dipoles attributes. 
                It represents the angle of the relief on the surface of the plates.
                unity:°

            length(type:float, Nonetype or :obj:np.float64): 
                This parameter indicates the private attribute length of the object initialised from 
                the class PlateHeatExchangerSide of the hydraulic dipoles attributes. 
                It represents the length of the plates of the heat exchanger.
                unity:m
            
            Npasse(type:int, Nonetype or :obj:np.int64): 
                This parameter indicates the private attribute Npasses of the object initialised from 
                the class PlateHeatExchangerSide of the hydraulic dipoles attributes. 
                It represents the number of pass of the heat exchanger.
            
            hydraulicDipoleCold( :obj:Dipole ): 
                This parameter indicate the attribute hydraulicDipoleCold of the class. 
                It represents one of the 2 dipole where one of the flow is flowing.
                It is the dipole which the fluid enters with the coldest temperature of the 2. 

            hydraulicDipoleWarm( :obj:Dipole )
                This parameter indicate the attribute hydraulicDipoleCold of the class. 
                It represents one of the 2 dipole where one of the flow is flowing.
                It is the dipole which the fluid enters with the warmest temperature of the 2. 

            downstreamPoleCold (:obj:Pole): 
                it's the attribute downstreamPole of the attribute hydraulicDipoleCold.

            upstreamPoleCold (:obj:Pole): 
                it's the attribute upstreamPole of the attribute hydraulicDipoleCold.

            downstreamPoleWarm (:obj:Pole): 
                it's the attribute downstreamPole of the attribute hydraulicDipole2.

            upstreamPoleWarm (:obj:Pole): 
                it's the attribute upstreamPole of the attribute hydraulicDipole2.

        Raises : 
            TypeError : 
                It's raised by the function typeErrorAtEntering when the Types and the object
                don't match with the type and the object defined.
            ValueError: 
                If the variables haven't the physical reality

        """

        # creation of dipoles objects if undefined:
        if hydraulicDipoleCold == None:
            hydraulicDipoleCold = PlateHeatExchangerSide('Plate heat exchanger side Cold', width, plateGap,
                                                        streakWaveLength, plateNumber, angle, length, Npasse,
                                                        hydraulicCorrectingFactor = 1.0, thermicCorrectingFactor = 1.0,
                                                        downstreamPoleCold, upstreamPoleCold, flowCold)
        if hydraulicDipoleWarm == None:
            hydraulicDipoleWarm = PlateHeatExchangerSide('Plate heat exchanger side Warm', width, plateGap,
                                                        streakWaveLength, plateNumber, angle, length, Npasse,
                                                        hydraulicCorrectingFactor = 1.0, thermicCorrectingFactor = 1.0,
                                                        downstreamPoleWarm, upstreamPoleWarm, flowWarm)
        # raising of exceptions :
        typeErrorAtEntering(hydraulicDipoleCold,Types = [], Classes=[PlateHeatExchangerSide] message = "the hydraulicDipoleCold must be a float or a None type")
        typeErrorAtEntering(hydraulicDipoleWarm,Types = [], Classes=[PlateHeatExchangerSide] message = "the hydraulicDipoleWarm must be a float or a None type")

        typeErrorAtEntering(plateThickness, Types = [float, type(None)], message = "the plate thickness must be a float number")
        if type(plateThickness) is not type(None):
            if plateThickness < 0:
                raise ValueError("the plate thickness must be positive")

        # Initialisation : 
        HeatExchanger.__init__(self, name = name, materialConductivity = materialConductivity,
                              hydraulicDipoleCold=hydraulicDipoleCold, hydraulicDipoleWarm=hydraulicDipoleWarm)
        self.__length = length
        self.__width = width
        self.__plateNumber = plateNumber
        self.__passeNumber = passeNumber
        self.__plateThickness = plateThickness
        self.__plateGap = plateGap
        self.__angle = angle
        self.__streakWaveLength = streakWaveLength

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
        self.hydraulicDipoleCold.length = length
        self.hydraulicDipoleWarm.length = length

    @property 
    def width(self): 
        return self.__width

    @width.setter 
    def width(self,width): 
        typeErrorAtEntering(width, message = "the width must be a float number")
        if type(width) is not type(None):
            if width < 0:
                raise ValueError('width must be positive')
        self.__width = width
        self.hydraulicDipoleCold.width = width
        self.hydraulicDipoleWarm.width = width

    @property 
    def plateNumber(self): 
        """ get and set allows the user to modify the private width attribute """
        return self.__plateNumber

    @plateNumber.setter 
    def plateNumber(self,plateNumber): 
        typeErrorAtEntering( plateNumber, Types = [int], Classes = [np.int64], message = "the plateNumber must be a integer number")
        if plateNumber < 1:
            raise ValueError("the
        self.__plateNumber = plateNumber
        self.hydraulicDipoleCold.plateNumber = plateNumber
        self.hydraulicDipoleWarm.plateNumber = plateNumber

    @property 
    def plateThickness(self): 
        """ get and set allows the user to modify the private plateThickness attribute """
        return self.__plateThickness

    @plateThickness.setter 
    def plateThickness(self, plateThickness): 
        typeErrorAtEntering(plateThickness, Types = [float, type(None)], message = "the plate thickness must be a float number")
        if type(plateThickness) is not type(None):
            if plateThickness < 0:
                raise ValueError("the plate thickness must be positive")
        self.__plateThickness = plateThickness

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
        self.__plateGap = plateGap
        self.hydraulicDipoleCold.plateGap = plateGap
        self.hydraulicDipoleWarm.plateGap = plateGap

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
        self.hydraulicDipoleCold.angle = angle
        self.hydraulicDipoleWarm.angle = angle

    @property 
    def streakWaveLength(self): 
        """ get and set allows the user to modify the private steakWaveLength attribute """
        return self.__streakWaveLength

    @streakWaveLength.setter 
    def streakWaveLength(self,streakWaveLength): 
        typeErrorAtEntering(streakWaveLength, message = "the streakWaveLength must be a float number")
        if type(streakWaveLength) is not type(None):
            if streakWaveLength < 0:
                raise ValueError('streakWaveLength must be positive')
        self.__streakWaveLength = streakWaveLength
        self.hydraulicDipoleCold.streakWaveLength = streakWaveLength
        self.hydraulicDipoleWarm.streakWaveLength = streakWaveLength
    
    def thermicTransfertCoefficient(self, reynoldsNumberCold = None, prandtlNumberCold = None, reynoldsNumberWarm = None, 
                                    prandtlNumberWarm = None, length = None, angle = None, Npasse = None, hydraulicDiameterCold = None, 
                                    hydraulicDiameterWarm = None,thermicConductivityCold = None, thermicConductivityWarm = None, 
                                    materialConductivity = None, plateThickness = None, parameterA = 3.8, parameterB = 0.045, 
                                    parameterC = 0.09, thermicCorrectingFactorCold = None, thermicCorrectingFactorWarm = None, modify = True):
        """ the method thermicTransfertCoefficient

        Note: 
            It take into account the caracteristics
            of the object initialised from the attributes hydraulic dipole sides.

        Args:
            reynoldsNumberCold(type:float):
                It corresponds to the Reynolds number which combines the
                importants information of the flow and the dipole correspondant.

            prandtlNumberCold(type:float):
                It corresponds to the prandtl number which is the ratio 
                between the momentum diffusivity and the thermal diffusivity :
                prantlNumber = thermicCapacity * dynamicViscosity / thermicConductivity

            hydraulicDiameterCold(type:float or None type):
                If the hydraulicDiameterCold is equal to None, then the hydraulicDiameterCold
                taken into account is taken from the dipole object cold.
                unity: m
            
            thermicConductivityCold(type:float or None type):
                If the thermicConductivityCold is equal to None, then the thermicConductivityCold
                taken into account is taken from the dipole object cold.
                unity: W/m/K

            thermicCorrectingFactorCold(type:float or None type):
                If the thermicCorrectingFactor is equal to None, then 
                the thermicCorrectingFactor taken into account is taken 
                from the dipole object.

            reynoldsNumberWarm(type:float):
                It corresponds to the Reynolds number which combines the
                importants information of the flow and the dipole correspondant.

            prandtlNumberWarm(type:float):
                It corresponds to the prandtl number which is the ratio 
                between the momentum diffusivity and the thermal diffusivity :
                prantlNumber = thermicCapacity * dynamicViscosity / thermicConductivity

            hydraulicDiameterWarm(type:float or None type):
                If the hydraulicDiameterWarm is equal to None, then the hydraulicDiameterWarm
                taken into account is taken from the dipole object cold.
                unity: m

            thermicConductivityWarm(type:float or None type):
                If the thermicConductivityWarm is equal to None, then the thermicConductivityWarm
                taken into account is taken from the dipole object cold.
                unity: W/m/K

            thermicCorrectingFactorWarm(type:float or None type):
                If the thermicCorrectingFactor is equal to None, then 
                the thermicCorrectingFactor taken into account is taken 
                from the dipole object.

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
            
            modify(type:boolean):
                If modify = True, the global heat transfert coefficient attribute 
                is modified.
                else : the global heat transfert coefficient is not modified.

        Returns:
            globalHeatTransfertCoefficient(type:float)
                        
        Raises: 
            TypeError : If the variables have not the types specified


        """
        hydraulicDipoleCold = self.hydraulicDipoleCold
        hydraulicDipoleWarm = self.hydraulicDipoleWarm

        #the two sides parameters :
        if length == None:
            length = self.length
        if angle == None:
            angle = self.angle
        if Npasse == None:
            Npasse = self.Npasse
        if materialConductivity == None :
            materialConductivity = self.materialConductivity
        if plateThickness == None :
            plateThickness = self.plateThickness * 10 ** (-3)
        
        #the cold side parameters :
        if thermicCorrectingFactorCold == None:
            thermicCorrectingFactor = hydraulicDiameterCold.thermicCorrectingFactor
        if hydraulicDiameterCold == None:
            hydraulicDiameter = hydraulicDiameterCold.hydraulicDiameter
        if prandtlNumberCold == None:
            prandtlNumber = hydraulicDiameterCold.flow.fluid.thermicCapacity * hydraulicDiameterCold.flow.fluid.dynamicViscosity / hydraulicDiameterCold.flow.fluid.thermicConductivity
        if thermicConductivityCold == None:
            thermicConductivityCold = hydraulicDiameterCold.flow.fluid.thermicConductivity

        #the warm side parameters :
        if thermicCorrectingFactorWarm == None:
            thermicCorrectingFactor = hydraulicDiameterWarm.thermicCorrectingFactor
        if hydraulicDiameterWarm == None:
            hydraulicDiameter = hydraulicDiameterWarm.hydraulicDiameter
        if prandtlNumberWarm == None:
            prandtlNumber = hydraulicDiameterWarm.flow.fluid.thermicCapacity * hydraulicDiameterWarm.flow.fluid.dynamicViscosity / hydraulicDiameterWarm.flow.fluid.thermicConductivity
        if thermicConductivityWarm == None:
            thermicConductivityWarm = hydraulicDiameterWarm.flow.fluid.thermicConductivity

        #raising exceptions :

        # the 2 sides
        typeErrorAtEntering(angle, message = "the angle must be a float number")
        if angle <0 or angle >90:
            raise ValueError("the angle must be 0 and 90 degree")

        typeErrorAtEntering(length, message = "the length must be a float number")
        if length < 0 :
            raise   ValueError("the length must be a positive float")

        typeErrorAtEntering( Npasse, Types = [int], Classes = [np.int64], message = "the Npasse must be a integer number")
        if Npasse < 1:
            raise ValueError("the number of passe must be a positive integer superior to 1")
            
        typeErrorAtEntering(materialConductivity, message = "the materialConductivity must be a float number")

        typeErrorAtEntering(plateThickness, message = "the plateThickness must be a float number")

        #Cold side :
        typeErrorAtEntering(thermicCorrectingFactorCold, message = "the thermicCorrectingFactorCold must be a float number")
        if thermicCorrectingFactorCold <= 0 :
            raise TypeError("the hydraulic correcting factor must be a strictly positive float close to 1")

        typeErrorAtEntering(reynoldsNumberCold, message = "the reynoldsNumberCold must be a float number")
        if reynoldsNumberCold <=0 :
            raise ValueError("the reynolds number must be a strictly positive float")

        typeErrorAtEntering(prandtlNumberCold, message = "the prandtl number must be a float number")

        typeErrorAtEntering(thermicConductivityCold, message = "the thermic conductivity must be a float number")

        #Warm side :
        typeErrorAtEntering(thermicCorrectingFactorWarm, message = "the thermicCorrectingFactorWarm must be a float number")
        if thermicCorrectingFactorWarm <= 0 :
            raise TypeError("the hydraulic correcting factor must be a strictly positive float close to 1")

        typeErrorAtEntering(reynoldsNumberWarm, message = "the reynoldsNumberWarm must be a float number")
        if reynoldsNumberWarm <=0 :
            raise ValueError("the reynolds number must be a strictly positive float")

        typeErrorAtEntering(prandtlNumberWarm, message = "the prandtl number must be a float number")

        typeErrorAtEntering(thermicConductivityWarm, message = "the thermic conductivity must be a float number")

        # Nusselt in the cold side :
        nusseltNumberCold = hydraulicDipoleCold.thermicCorrelation(reynoldsNumberCold, prandtlNumberCold, length, angle, Npasse,
                                                                    hydraulicDiameterCold, parameterA, parameterB, parameterC, 
                                                                    thermicCorrectingFactorCold)
        thermicConvectiveCoefficientCold = HydraulicThermicCalculus.nusselt(hydraulicDiameterCold, thermalConductivityCold, nusseltNumberCold)

        # Nusselt in the Warm side :
        nusseltNumberWarm = hydraulicDipoleWarm.thermicCorrelation(reynoldsNumberWarm, prandtlNumberWarm, length, angle, Npasse,
                                                                    hydraulicDiameterWarm, parameterA, parameterB, parameterC, 
                                                                    thermicCorrectingFactorWarm)
        thermicConvectiveCoefficientWarm = HydraulicThermicCalculus.nusselt(hydraulicDiameterWarm, thermalConductivityWarm, nusseltNumberWarm)

        if materialConductivity == None :
            materialConductivity = self.materialConductivity
        if plateThickness == None :
            plateThickness = self.plateThickness * 10 ** (-3)
        
        globalThermicCoefficient = 1 / (1 / thermicConvectiveCoefficientCold + 1 / thermicConvectiveCoefficientWarm + plateThickness/materialConductivity)
        
        if modify :
            self.globalThermicCoefficient = globalThermicCoefficient

        return globalThermicCoefficient
    

