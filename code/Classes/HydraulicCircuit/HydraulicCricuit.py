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

    def testCircuit(self):#cette fonction va renvoyer True si le circuit est possible et false sinon
        if self.edges == []
            raise ValueError("the circuit must have a dipole")
        if self.opengGraph(): #si un graphe est ouvert il faut nécessairement qu'il y ait du liquide qui rentre de l'extérieur (et donc qu'un noeud n'ait pas de noeud descendant)
            test = False
            for node in self.nodes:
                finds = self.searchEdgesByNodes(node)
                testing = True
                for find in finds:
                    if find[1] == 1: #si le noeud admet un ascendant
                        testing = False
                if testing:
                    test = True
            return test 
        else : #si le circuit est fermé, pour que le circuit vérifie la conservation de la quanttité de fluide il faut nécessairement que tout les dipoles appartiennent à une boucle (sinon le liquide s'accumulerait à un endroit) 
            test = False
            Loops = self.loops(self.nodes[0])
            for dipole in self.dipoles:
                for loop in Loops:
                    if dipole in loop:
                        test = True
            return test




    def hydraulicFunctionnementCloseCircuit(self):
        if len(self.edges) == 0:
            raise ValueError("the hydraulic circuit must have at least one dipole")
        if self.openGraph():
            raise ValueError("the hydraulic circuit must be close")
        loopsByEdge = self.loops(self.nodes[0]) #On commence par déterminer les différentes boucles du circuit pour appliquer : sum Dp = 0 sur chaque boucle
        loopsByNode = self.loops(self.nodes[0],by = 'nodes')
        # on essai de se rapprocher de la solution en utilisant le débit maximal s'il est donné:
        # test de si le débit maximal est donnée pour les débits variables :
        testingVariables = self.testingVariables
        N = len(testingVariables) #correspond aussi au nombre de dipoles présents dans le circuit
        testMaximalFlowRate = True
        variableFlowRateDipole = [] #on fait une liste des ids des dipoles dans lesquels s'écoule un débit inconnu
        for i in range(N):
            dipole = self.dipoles[i]
            if testingVariables[i][0]: #si le débit du dipole i n'est pas fixé
                variableFlowRateDipole.append(i) 
                if dipole.flowRateMax == None:
                    testMaximalFlowRate = False #si jamais le débit maximum n'est pas fixé on ne peut pas estimer une solution pour commencer l'algorithme
                    print("it should be easier to conoverge if the maximal flow rate of " + str(dipole.name) + " was defined")
            if testingVariables[i][0] and testingVariables[i][1]: #s'il n'y a ni le débit ni la différence de pression qui est fixée il doit obligatoirement y avoir la caracteristique du circuit qui est définie
                if dipole.caracteristic(1.0) == None: #on appelle la fonction il ne faut pas qu'elle retourne None
                    raise ValueError("the hydraulic caracteristic of the dipole " +str(dipole.name)+ "needs to be defined to calcul the hydraulic fonctionnement of the circuit" )
        #On commence par déterminer dans tout les cas la partie du système qui sera linéaire avec la lois des noeuds:
        loopNumber = len(loopsByEdge)
        for i in range(loopNumber):
            loopByNode = loopsByNode[i]
            loopsByEdge = loopsByEdge[i]


        if testMaximalFlowRate = True : #dans ce cas là on linéarise le système avec la méthode de la sécante (sur toute les caracteristiques) pour s'approcher de la solution par la résolution d'un système linéaire
            
        loopsByEdge = self.loops(self.node[0])






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