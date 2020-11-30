import unittest
import sys
sys.path.append("./Classes")

from DipoleFolder.Dipole import Dipole, Pipe, PlateHeatExchangerSide, IdealPump, Pole, Pump
from FlowFolder.Flow import Flow
from FluidFolder.Fluid import Fluid
from GraphFolder.Graphe import Graph, Node, Edge, Queue
from  math import pi
import numpy as np
import matplotlib.pyplot as plt
class TestPump(unittest.TestCase):
    def setUp(self):
        self.flowRates = np.linspace(0,1,1000)
        self.overPressures = [(1 - flowRate ** 2) * 10 ** 5 * 3 for flowRate in self.flowRates]
        self.pump = Pump(flowRates=self.flowRates, overPressures=self.overPressures, inputTemperature=20.0)
    
    def test_caracteristic(self):
        overPressures = [self.pump.caracteristic(flowRate) for flowRate in self.flowRates]
        fig = plt.figure()
        plt.plot(self.flowRates, overPressures)
        plt.show()
    
    def test_power(self):
        hydraulicPowers = [self.pump.hydraulicPower(flowRate) for flowRate in self.flowRates[1:]]
        fig2 = plt.figure()
        plt.plot(self.flowRates[1:], hydraulicPowers)
        plt.show()
    
if __name__ == '__main__':
    unittest.main()