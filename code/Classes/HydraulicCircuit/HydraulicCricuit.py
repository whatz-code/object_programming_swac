import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Graphe")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole")
from Dipole import Pipe, Dipole, PlateHeatExchangerSide, IdealPump, Pole
from Graphe import Graph, Node, Edge, Queue

class HydraulicCircuit(Graph):
    #l'initialisation de la classe : 
    def __init__(self,name = 'Hydraulic circuit',dipoles = [],poles = [],definedBy = 'edges') : 
        Graph.__init__(self, edges = dipoles, nodes = poles, definedBy = definedBy)
        self.__name = name
        self.__dipoles = dipoles
        self.__poles = poles

    @property 
    def name(self): 
        return self.__name

    @name.setter 
    def name(self,name): 
        self.__name = name

    @property 
    def dipoles(self): 
        self.edges

    @dipoles.setter 
    def dipoles(self,dipoles): 
        self.edges = dipoles

    @property 
    def poles(self): 
        self.nodes

    @poles.setter 
    def poles(self,poles): 
        self.nodes = poles

    def functionnement(self):
        
#microtest
pole1 = Pole('A',successors=[])
pole2 = Pole('B',successors=[])
pole3 = Pole('C',successors=[])
pole1.successors = [pole2]
pole2.successors = [pole3]
pole3.successors = [pole1]
pump = IdealPump(name = 'pump', downstreamPole=pole1,upstreamPole=pole2)
pipe2 = Pipe(name = 'Pipe 1', downstreamPole=pole2,upstreamPole=pole3)
pipe3 = Pipe(name = 'Pipe 2', downstreamPole=pole3,upstreamPole=pole1)
hydraulicCircuit = HydraulicCircuit(dipoles=[pump,pipe2,pipe3])
hydraulicCircuit.print()