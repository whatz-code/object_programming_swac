from FluidModule import Fluid
eau = Fluid()
class HydraulicThermicCalculus :
    #méthode permettant de calculer le nombre de Reynolds ou de tirer une autre variable si le nombre de Reynolds est connu
    def reynolds(caracteristicLength = None, caracteristicVelocity = None, volumetricMass = 1000, dynamicViscosity = 0.001,reynoldsNumber =  None):
        if caracteristicLength == None :
            return(reynoldsNumber * dynamicViscosity / (volumetricMass * caracteristicVelocity))
        if caracteristicVelocity == None : 
            return(reynoldsNumber * dynamicViscosity / (volumetricMass * caracteristicLength))
        if reynoldsNumber == None :
            return(volumetricMass * caracteristicVelocity * caracteristicLength / dynamicViscosity)
    reynolds = staticmethod(reynolds)

    def nusselt(caracteristicLength = None, thermalConductivity = 0.6071, nusselt = None, thermalTransferCoefficient = None) :
        if nusselt == None :
            return thermalTransferCoefficient * caracteristicLength / thermalConductivity
        if thermalTransferCoefficient == None :
            return nusselt * thermalConductivity / caracteristicLength
    nusselt = staticmethod(nusselt)

    def prandtl(dynamicViscosity = 0.001, thermalCapacity = 4150, thermalConductivity = 0.6071):
        return dynamicViscosity * thermalCapacity / thermalConductivity
    prandtl = staticmethod(prandtl)

    def headLoss(headLossCoefficient = None, volumetricMass = 1000, averageVelocity = None):
        return headLossCoefficient * volumetricMass * averageVelocity * averageVelocity / 2
    headLoss = staticmethod(headLoss)
    
    def caracteristic(dipole, flowRate, fluid = eau, flowRateUnity = "m3/s", pressureUnity = "Pa"):
        if flowRateUnity == "m3/h" :
            flowRate = flowRate / 3600
        velocity = flowRate / dipole.crossSectionalArea
        reynoldsNumber = HydraulicThermicCalculus.reynolds(dipole.hydraulicDiameter,velocity,fluid.volumetricMass,fluid.dynamicViscosity,None)
        headLossCoefficient = dipole.hydraulicCorrelation(float(reynoldsNumber))
        headLoss = HydraulicThermicCalculus.headLoss(headLossCoefficient, fluid.volumetricMass, velocity)
        if pressureUnity == "Pa":
            return headLoss
        if pressureUnity == "bar" :
            return headLoss / 10 ** 5
        if pressureUnity == "mCE" :
            return headLoss / 10 ** 5 * 9.81



#tests
reynolds = HydraulicThermicCalculus.reynolds(10,15,300,0.00001)
