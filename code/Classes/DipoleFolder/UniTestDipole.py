import unittest
import sys
sys.path.append("./Classes")
sys.path.append("./Classes/Flow")
sys.path.append("./Classes/Fluid")
sys.path.append("./Classes/Graphe")
from DipoleFolder.DipoleModule import Dipole, Pipe, PlateHeatExchangerSide, IdealPump, Pole
from FlowFolder.FlowModule import Flow
from FluidFolder.FluidModule import Fluid
from GraphFolder.GraphModule import Graph, Node, Edge, Queue

class TestDipole(unittest.TestCase):
    def setUp(self):
        self.downstreamPole = Pole('pole1')
        self.upstreamPole = Pole('pole2')
        self.flow = Flow()
        self.default = Dipole(downstreamPole=self.downstreamPole,upstreamPole=self.upstreamPole)
        self.dipole = Dipole('dipole',0.1,0.1,self.downstreamPole,self.upstreamPole,self.flow)
    def test_init(self):
        with self.assertRaises(TypeError):
            self.initTest = Dipole(hydraulicDiameter=1)
            self.initTest = Dipole(crossSectionalArea=1)
            self.initTest = Dipole(downstreamPole=1)
            self.initTest = Dipole(upstreamPole=1)
            self.initTest = Dipole(flow=1)
    def test_getter(self):
        self.assertEqual(self.dipole.name,'dipole')
        self.assertEqual(self.dipole.hydraulicDiameter,0.1)
        self.assertEqual(self.dipole.crossSectionalArea,0.1)
        self.assertEqual(self.dipole.downstreamPole,self.downstreamPole)
        self.assertEqual(self.dipole.upstreamPole,self.upstreamPole)
        self.assertEqual(self.dipole.flow,self.flow)

    def test_setter(self):
        self.dipole.name = 1
        self.dipole.hydraulicDiameter = 0.1
        self.dipole.crossSectionalArea = 0.1
        self.dipole.downstreamPole = self.upstreamPole
        self.dipole.upstreamPole = self.downstreamPole
        self.dipole.flow = self.flow
        with self.assertRaises(TypeError):
            self.dipole.hydraulicDiameter = 1
            self.dipole.crossSectionalArea = 1
            self.dipole.downstreamPole = 1
            self.dipole.upstreamPole = 1
            self.dipole.flow = 1
    



        






if __name__ == '__main__':
    unittest.main()