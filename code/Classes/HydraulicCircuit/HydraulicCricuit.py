import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Graphe")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole")
from Dipole import Pipe, Dipole, PlateHeatExchangerSide, IdealPump, Pole
from Graphe import Graph, Node, Edge, Queue
from matplotlib import numpy as np
class HydraulicCircuit(Graph):
    #l'initialisation de la classe : 
    def __init__(self,name = 'Hydraulic circuit',dipoles = [],poles = []) : 
        if type(dipoles) is not list:
            raise TypeError("dipoles must be a list of dipoles")
        for dipole in dipoles:
            if not(isinstance(dipole,Dipole)):
                raise TypeError("dipoles must be a list of dipoles")
        if type(poles) is not list:
            raise TypeError("poles must be a list of poles")
        for pole in poles:
            if not(isinstance(pole,Pole)):
                raise TypeError("poles must be a list of dipoles")
        Graph.__init__(self, edges = dipoles, nodes = poles)
        self.__name = name
        self.__variables = ['flowRate', 'pressureDifference', 'inputTemperature', 'outletTemperature']
        testingVariables = []
    
        for dipole in dipoles:
            variablesDipole = []
            if dipole.flow.flowRate == None:
                variablesDipole.append(True)
            else:
                variablesDipole.append(False)

            if dipole.flow.pressureDifference == None:
                variablesDipole.append(True)
            else:
                variablesDipole.append(False)
            
            if dipole.flow.inputTemperature == None:
                variablesDipole.append(True)
            else:
                variablesDipole.append(False)
            
            if dipole.flow.outletTemperature == None:
                variablesDipole.append(True)
            else:
                variablesDipole.append(False)
            
            testingVariables.append(variablesDipole)
        
        self.__testingVariables = testingVariables

    


    @property 
    def testingVariables(self): 
        return self.__testingVariables

    @testingVariables.setter 
    def testingVariables(self,testingVariables): 
        self.__testingVariables = testingVariables

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
        self.__init__(name = self.name, dipoles = dipoles, poles = [])

    @property 
    def poles(self): 
        self.nodes

    @poles.setter 
    def poles(self,poles): 
        self.nodes = poles


    def addDipole(self, dipole, name = None):
        pole1 = dipole.downstreamPole
        pole2 = dipole.upstreamPole
        self.newEdge(pole1, pole2, name = name)

        variablesDipole = []
        if dipole.flow.flowRate == None:
            variablesDipole.append(True)
        else:
            variablesDipole.append(False)

        if dipole.flow.pressureDifference == None:
            variablesDipole.append(True)
        else:
            variablesDipole.append(False)
        
        if dipole.flow.inputTemperature == None:
            variablesDipole.append(True)
        else:
            variablesDipole.append(False)
        
        if dipole.flow.outletTemperature == None:
            variablesDipole.append(True)
        else:
            variablesDipole.append(False)

        self.testingVariables.append(variablesDipole)

    def delDipole(self, dipole):
        self.delEdge( dipole, by = "edge")
        del self.testingVariables[dipole.id]

    def hydraulicFunctionnement(self):
            






        def functionToZero(self): #doit renvoyer la fonction à faire converger vers 0
            def function(flowRates, pressures): #on définit les variables dans l'ordre de définition des dipôles (correspondant en fait à leur id)
                equations = []
                for node in self.nodes:
                    edges = self.searchEdgesByNodes(node)
                    equations.append(0)
                    for edge in edges:
                        dipole = edge[0]
                        if edge[1] == 0:
                            factor = -1
                        else :
                            factor = 1
                        equations[-1] += factor * dipole.flow.flowRate
                        

                

        
#microtest
# pole1 = Pole('A',successors=[])
# pole2 = Pole('B',successors=[])
# pole3 = Pole('C',successors=[])
# pole1.successors = [pole2]
# pole2.successors = [pole3]
# pole3.successors = [pole1]
# pump = IdealPump(name = 'pump', downstreamPole=pole1,upstreamPole=pole2)
# pipe2 = Pipe(name = 'Pipe 1', downstreamPole=pole2,upstreamPole=pole3)
# pipe3 = Pipe(name = 'Pipe 2', downstreamPole=pole3,upstreamPole=pole1)
# hydraulicCircuit = HydraulicCircuit(dipoles=[pump,pipe2,pipe3])
# hydraulicCircuit.print()