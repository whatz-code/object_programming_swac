import unittest
import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Flow")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Graphe")
from FlowFolder.Flow import Flow
from GraphFolder.Graphe import Graph,Edge, Node
from Calculus import Resolve
from FluidFolder.Fluid import Fluid
from DipoleFolder.Dipole import Dipole, Pipe, PlateHeatExchangerSide, Pole, IdealPump
from HydraulicCricuit import HydraulicCircuit
import numpy as np

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

                
    def test_nodeslaw():
        print('\n'+'test_node law')
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        pole4 = Pole("pole4")
        dipole1 = Dipole("dipole1",downstreamPole = pole1, upstreamPole = pole2)
        dipole2 = Dipole("dipole2",downstreamPole = pole2, upstreamPole = pole3)
        dipole3 = Dipole("dipole3",downstreamPole = pole3, upstreamPole = pole1)
        dipole4 = Dipole("dipole4",downstreamPole = pole3, upstreamPole = pole4)
        dipole5 = Dipole("dipole5",downstreamPole = pole4, upstreamPole = pole1)

        hydraulicCircuit = HydraulicCircuit(dipoles = [dipole1, dipole2, dipole3, dipole4, dipole5])
        hydraulicCircuit.print()
        f, M = hydraulicCircuit.nodesLaw()

        print(M)
        print(np.linalg.matrix_rank(M))
        print(f([1,1,1,1,1]))
    test_nodeslaw = staticmethod(test_nodeslaw)

    def test_looplaw():
        print('\n'+'test_node law')
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        pole4 = Pole("pole4")
        dipole1 = Dipole("dipole1",downstreamPole = pole1, upstreamPole = pole2)
        dipole2 = Dipole("dipole2",downstreamPole = pole2, upstreamPole = pole3)
        dipole3 = Dipole("dipole3",downstreamPole = pole3, upstreamPole = pole1)
        dipole4 = Dipole("dipole4",downstreamPole = pole3, upstreamPole = pole4)
        dipole5 = Dipole("dipole5",downstreamPole = pole4, upstreamPole = pole1)

        hydraulicCircuit = HydraulicCircuit(dipoles = [dipole1, dipole2, dipole3, dipole4, dipole5])
        hydraulicCircuit.print()
        f = hydraulicCircuit.loopLaw()
        print(f([1,1,1,1,1]))
    test_looplaw = staticmethod(test_looplaw)
    def test_variablesAndEquationsOfHydraulicFunctionnement():
        print('\n' + 'test variables and equations of hydraulic functionnement')
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        pole4 = Pole("pole4")
        pole5 = Pole("pole5")
        pump = IdealPump("ideal pump", flowRate=0.175, downstreamPole=pole1,upstreamPole=pole2, inputTemperature = 20.0)
        pipe1 = Pipe("pipe1",downstreamPole=pole2, upstreamPole=pole5)
        pipe2 = Pipe("pipe2", downstreamPole=pole5, upstreamPole= pole1)
        pipe3 = Pipe("pipe3", downstreamPole=pole3, upstreamPole=pole4)
        flowOfblanck = Flow(pressureDifference=0.0)
        blanck1 = Dipole("blanck1", flow = flowOfblanck, downstreamPole=pole2, upstreamPole=pole3)
        blanck2 = Dipole("blanck2", flow = flowOfblanck, downstreamPole=pole4, upstreamPole=pole5 )

        hydraulicCircuit = HydraulicCircuit(dipoles = [pump, pipe1, pipe2, pipe3, blanck1, blanck2])
        hydraulicCircuit.print()
        print(hydraulicCircuit.testingVariables)
        equationsAndVariables = hydraulicCircuit.variablesAndEquationsOfHydraulicFunctionnement()
        print(equationsAndVariables[0][1])
        print(equationsAndVariables[1][2])

    def hydraulicSystem():
        print('\n' + 'test hydraulic system')
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        pole4 = Pole("pole4")
        pole5 = Pole("pole5")
        pump = IdealPump("ideal pump", flowRate=0.175, downstreamPole=pole1,upstreamPole=pole2)
        pipe1 = Pipe("pipe1",downstreamPole=pole2, upstreamPole=pole5)
        pipe2 = Pipe("pipe2", downstreamPole=pole5, upstreamPole= pole1)
        pipe3 = Pipe("pipe3", downstreamPole=pole3, upstreamPole=pole4)
        flowOfblanck = Flow(pressureDifference=0.0)
        blanck1 = Dipole("blanck1", flow = flowOfblanck, downstreamPole=pole2, upstreamPole=pole3)
        blanck2 = Dipole("blanck2", flow = flowOfblanck, downstreamPole=pole4, upstreamPole=pole5 )

        hydraulicCircuit = HydraulicCircuit(dipoles = [pump, pipe1, pipe2, pipe3, blanck1, blanck2])
        hydraulicCircuit.print()
        print(hydraulicCircuit.testingVariables)
        hydraulicSystem = hydraulicCircuit.hydraulicSystem()
        print(hydraulicSystem[1])
        print(hydraulicSystem[2])
        print(hydraulicSystem[3])
        print(hydraulicSystem[0]([1.0,1.0,1.0,1.0,1.0,1.0,1.0]))
    
    def testpointfunctionnement():
        print('\n' + 'test hydraulic system')
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        pole4 = Pole("pole4")
        pole5 = Pole("pole5")
        pump = IdealPump("ideal pump", flowRate=0.233, downstreamPole=pole1,upstreamPole=pole2, inputTemperature=20.0)
        pipe1 = Pipe("pipe1",downstreamPole=pole2, upstreamPole=pole5)
        pipe2 = Pipe("pipe2", downstreamPole=pole5, upstreamPole= pole1)
        pipe3 = Pipe("pipe3", downstreamPole=pole3, upstreamPole=pole4)
        flowOfblanck = Flow(pressureDifference=0.0)
        blanck1 = Dipole("blanck1", flow = flowOfblanck, downstreamPole=pole2, upstreamPole=pole3, variables=[True, False, False, False])
        blanck2 = Dipole("blanck2", flow = flowOfblanck, downstreamPole=pole4, upstreamPole=pole5, variables=[True, False, False, False] )
        hydraulicCircuit = HydraulicCircuit(dipoles = [pump, pipe1, pipe2, pipe3, blanck1, blanck2])
        hydraulicCircuit.print()
        f, M = hydraulicCircuit.nodesLaw()
        print(np.linalg.matrix_rank(M))
        print(M)
        hydraulicCircuit.resolutionFonctionnement()
        print(pipe1.flow.flowRate)
    
    def testpointfunctionnement2():
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        pole4 = Pole("pole4")
        pump = IdealPump("ideal pump", flowRate=0.1, downstreamPole=pole1,upstreamPole=pole2)
        pipe = Pipe("pipe1",downstreamPole=pole3, upstreamPole=pole4)
        flowOfblanck = Flow(pressureDifference=0.0)
        blanck1 = Dipole("blanck1", flow = flowOfblanck, downstreamPole=pole2, upstreamPole=pole3, variables=[True, False, False, False])
        blanck2 = Dipole("blanck2", flow = flowOfblanck, downstreamPole=pole4, upstreamPole=pole1, variables=[True, False, False, False])
        hydraulicCircuit = HydraulicCircuit(dipoles = [pump, pipe, blanck1, blanck2])
        hydraulicCircuit.print()
        f, M = hydraulicCircuit.nodesLaw()
        hydraulicCircuit.resolutionFonctionnement()
        hydraulicCircuit.assignPressure(pole1, 10**5 )
        print(pipe.flow.flowRate)
        for pole in hydraulicCircuit.poles :
            print(pole.name)
            print(pole.pressure)
    
        
        


if __name__ == '__main__':
    #unittest.main()
    TestGraphe.testpointfunctionnement2()
