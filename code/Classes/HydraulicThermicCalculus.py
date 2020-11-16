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

#tests
reynolds = HydraulicThermicCalculus.reynolds(10,15,300,0.00001)
print(reynolds)