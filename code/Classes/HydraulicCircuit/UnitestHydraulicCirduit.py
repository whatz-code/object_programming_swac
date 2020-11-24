import unittest
import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Flow")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Graphe")
from Flow import Flow
from Graphe import Edge, Node
from Calculus import Resolve
from Fluid import Fluid
from Dipole import Dipole, Pipe, PlateHeatExchangerSide, Pole, IdealPump
from HydraulicCricuit import HydraulicCircuit


class TestGraphe(unittest.TestCase):

    def test_init(self):
        print('\n' + 'test_init')
        
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        dipole = Dipole(downstreamPole=pole1, upstreamPole=pole2)
        idealPump = IdealPump("Ideal pump", flowRate = 10.0, downstreamPole=pole2, upstreamPole=pole3)
        hydraulicCircuit = HydraulicCircuit(dipoles = [dipole, idealPump], poles=[])
        hydraulicCircuit.print()
        self.assertTrue(hydraulicCircuit.graphCoherency())
        print(hydraulicCircuit.testingVariables)
    def test_getter(self):
        print('\n' + 'test_getter')
        
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        dipole = Dipole(downstreamPole=pole1, upstreamPole=pole2)
        idealPump = IdealPump("Ideal pump", flowRate = 10.0, downstreamPole=pole2, upstreamPole=pole3)
        hydraulicCircuit = HydraulicCircuit(dipoles = [dipole, idealPump], poles=[])
        hydraulicCircuit.dipoles
        hydraulicCircuit.poles

    def test_setter(self):
        print('\n' + 'test_setter')
        
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        dipole = Dipole(downstreamPole=pole1, upstreamPole=pole2)
        idealPump = IdealPump("Ideal pump", flowRate = 10.0, downstreamPole=pole2, upstreamPole=pole3)
        hydraulicCircuit = HydraulicCircuit(dipoles = [dipole, idealPump], poles=[])

        hydraulicCircuit.dipoles = [dipole]
        hydraulicCircuit.print()
        print(hydraulicCircuit.testingVariables)

    def test_adddipole(self):
        print('\n' + 'test_adddipole')
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        dipole = Dipole(downstreamPole=pole1, upstreamPole=pole2)
        idealPump = IdealPump("Ideal pump", flowRate = 10.0, downstreamPole=pole2, upstreamPole=pole3)
        hydraulicCircuit = HydraulicCircuit(dipoles = [dipole], poles=[])
        hydraulicCircuit.addDipole(idealPump, "ideal pump")
        hydraulicCircuit.print()
        print(hydraulicCircuit.testingVariables)

    def test_delDipole(self):
        print('\n' + 'test_delDipole')
        
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        dipole = Dipole(downstreamPole=pole1, upstreamPole=pole2)
        idealPump = IdealPump("Ideal pump", flowRate = 10.0, downstreamPole=pole2, upstreamPole=pole3)
        hydraulicCircuit = HydraulicCircuit(dipoles = [dipole, idealPump], poles=[])
        hydraulicCircuit.delDipole(idealPump)
        hydraulicCircuit.print()
        self.assertTrue(hydraulicCircuit.graphCoherency())
        print(hydraulicCircuit.testingVariables)

                

if __name__ == '__main__':
    unittest.main()