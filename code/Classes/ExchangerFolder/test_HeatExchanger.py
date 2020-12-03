import unittest
from HeatExchanger import HeatExchanger, PlateExchanger
import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole") 
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid") 
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes") 
from DipoleFolder.Dipole import Pole
from HydraulicThermicCalculus import HydraulicThermicCalculus
from FlowFolder.Flow import Flow

from FluidFolder.Fluid import Fluid
class TestHeadExchanger(unittest.TestCase):
    def setUp(self):
        self.plateHeatExchanger = PlateExchanger(streakWaveLength=0.5)
    def test_stateEquationDefinition(self):
        stateEquation = self.plateHeatExchanger.stateEquationDefinition()
        state = stateEquation(0.5, 0.6, 10.0, 20.0, 14.0 ,12.0)
        print(state)
        state = self.plateHeatExchanger.resolutionStateEquations(0.5, 0.6, 10.0, 20.0, 18.0 ,11.0)
        print(state)
        help(PlateExchanger)
if __name__ == '__main__':
    unittest.main()