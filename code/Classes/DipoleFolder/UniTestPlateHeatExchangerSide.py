import unittest
import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Flow")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Graphe")
from DipoleFolder.Dipole import Dipole, Pipe, PlateHeatExchangerSide, IdealPump, Pole
from FlowFolder.Flow import Flow
from FluidFolder.Fluid import Fluid
from GraphFolder.Graphe import Graph, Node, Edge, Queue
from  math import pi
class TestPlateHeatExchangerSide(unittest.TestCase):
    def setUp(self):
        self.downstreamPole = Pole('pole1')
        self.upstreamPole = Pole('pole2')
        self.flow = Flow()
        self.default = Pipe(downstreamPole=self.downstreamPole,upstreamPole=self.upstreamPole)
        self.pipe = Pipe('pipe',0.1,0.1,0.1,self.downstreamPole,self.upstreamPole,self.flow)




        






if __name__ == '__main__':
    unittest.main()