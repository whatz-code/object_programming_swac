import unittest
import sys
sys.path.append("./Modules") 
from DipoleModule import Dipole, Pole
from FlowModule import Flow
from HeatExchangerModule import HeatExchanger, PlateExchanger
from FluidModule import Fluid
from HydraulicThermicCalculus import reynolds

class TestHeadExchanger(unittest.TestCase):
    def setUp(self):
        self.plateHeatExchanger = PlateExchanger(streakWaveLength=0.5)
        self.funke_plate_exchanger = PlateExchanger('Funke', materialConductivity=21.9, length = 2.267, width = 0.6, 
                                                    plateNumber=385.0, Npasse = 1, plateThickness=0.6,
                                                    plateGap=3.8, angle = 75.0, streakWaveLength=1.0)
    def test_stateEquationDefinition(self):
        stateEquation = self.plateHeatExchanger.stateEquationDefinition()
        state = stateEquation(0.5, 0.6, 10.0, 20.0, 14.0 ,12.0)
        print(state)
        state = self.plateHeatExchanger.resolutionStateEquations(0.5, 0.6, 10.0, 20.0, 18.0 ,11.0)
        print(state)
    def test_hydraulic_error_minimization(self):
        provider_state = [[0.1095, 0.267 * 10 ** 5],
                          [0.115, 0.299 * 10 ** 5],
                          [0.17, 0.611 * 10 ** 5],
                          [0.219, 0.611 * 10 ** 5]]
        flow_rate = 0.1095
        mean_velocity = flow_rate / self.funke_plate_exchanger.hydraulicDipoleWarm.crossSectionalArea
        
        print('mean velocity', mean_velocity)
        print(self.funke_plate_exchanger.hydraulicErrorMinimization(provider_state)) 
    def test_thermic_error_minimization(self):
        provider_state = [[0.115, 0.1095, 17.0, 27.10, 26.0, 18.0],
                          [0.17388, 0.16514, 19.0, 32.0, 28.0, 23.11],
                          [0.17396, 0.21805, 19.0, 27.3, 24.75, 23.0]]
        print(self.funke_plate_exchanger.thermicErrorMinimization(provider_state))
        print('thermic correcting factor', self.funke_plate_exchanger.hydraulicDipoleWarm.thermicCorrectingFactor)
        print('free cooling', self.funke_plate_exchanger.thermicTransfertCoefficient(flowRateCold=0.115,
                                                                     flowRateWarm = 0.1095))
        print('mixte', self.funke_plate_exchanger.thermicTransfertCoefficient(flowRateCold=0.17396,
                                                                     flowRateWarm = 0.21805))          
                   
if __name__ == '__main__':
    unittest.main()