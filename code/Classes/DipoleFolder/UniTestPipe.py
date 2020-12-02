import unittest
import sys
sys.path.append("./Classes")

from DipoleFolder.Dipole import Dipole, Pipe, PlateHeatExchangerSide, IdealPump, Pole
from FlowFolder.Flow import Flow
from FluidFolder.Fluid import Fluid
from GraphFolder.Graphe import Graph, Node, Edge, Queue
from  math import pi
class TestPipe(unittest.TestCase):
    def setUp(self):
        self.downstreamPole = Pole('pole1')
        self.upstreamPole = Pole('pole2')
        self.flow = Flow()
        self.default = Pipe(downstreamPole=self.downstreamPole,upstreamPole=self.upstreamPole)
        self.pipe = Pipe('pipe',0.1,0.1,0.1,self.downstreamPole,self.upstreamPole,self.flow)
    def test_init(self):
        with self.assertRaises(TypeError):
            self.initTest = Pipe(pipeDiameter=1)
            self.initTest = Pipe(rugosity=1)
            self.initTest = Pipe(length=1)
            self.initTest = Pipe(downstreamPole=1)
            self.initTest = Pipe(upstreamPole=1)
    def test_getter(self):
        self.assertEqual(self.pipe.name,'pipe')
        self.assertEqual(self.pipe.length,0.1)
        self.assertEqual(self.pipe.pipeDiameter,0.1)
        self.assertEqual(self.pipe.crossSectionalArea,pi * 0.1 ** 2 / 4)
        self.assertEqual(self.pipe.rugosity,0.1)
        self.assertEqual(self.pipe.downstreamPole,self.downstreamPole)
        self.assertEqual(self.pipe.upstreamPole,self.upstreamPole)
        self.assertEqual(self.pipe.flow,self.flow)

    def test_setter(self):
        self.pipe.name = 1
        self.pipe.pipeDiameter = 0.1
        self.pipe.crossSectionalArea = 0.1
        self.pipe.downstreamPole = self.upstreamPole
        self.pipe.upstreamPole = self.downstreamPole
        self.pipe.rugosity = 0.1
        self.pipe.flow = self.flow
        self.pipe.length = 0.1
        with self.assertRaises(TypeError):
            self.pipe.pipeDiameter = 1
            self.pipe.rugosity = 1
            self.pipe.length = 2
            self.pipe.crossSectionalArea = 1
            self.pipe.downstreamPole = 1
            self.pipe.upstreamPole = 1
            self.pipe.flow = 1
    
    def test_hydraulicCorrelation(self):
        self.pipe.hydraulicCorrelation(3000.0)
        self.pipe.hydraulicCorrelation(3000.0, 200.0, 2.0, 0.2)
        with self.assertRaises(ValueError):
            self.pipe.hydraulicCorrelation(reynoldsNumber = -1.0)
            self.pipe.hydraulicCorrelation(reynoldsNumber = 0.0)
    def test_caracteristic(self):
        self.pipe = Pipe(rugosity = 0.0001,length=500.0,downstreamPole=self.downstreamPole,upstreamPole=self.upstreamPole)
        self.pipe.flow.flowRate = 830.0 / 3600
        print(self.pipe.hydraulicCaracteristic() / 10 ** 5 * 9.8)




        






if __name__ == '__main__':
    unittest.main()