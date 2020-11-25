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
        self.__nodesLawFunction = None
        self.__dipoles = self.edges
        self.__poles = self.nodes
        self.__loopLawFunction = None
    


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
        return self.edges

    @dipoles.setter 
    def dipoles(self,dipoles): 
        self.__init__(name = self.name, dipoles = dipoles, poles = [])

    @property 
    def poles(self): 
        self.nodes

    @poles.setter 
    def poles(self,poles): 
        self.nodes = poles

    @property 
    def nodesLawFunction(self): 
        self.__nodesLawFunction

    @property 
    def loopLawfunction(self): 
        self.__loopLawFunction

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
        if self.edges == []:
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

    def variablesAndEquationsOfHydraulicFunctionnement(self):
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
        variablePressureDipole = [] #on fait une liste des ids dans lesquels la différence de pression est inconnue
        dipoleWithCaracteristic = [] #on fait une liste des ids dans lesquels ni la différence de pression est connue ni le débit n'est connue
        for i in range(N):
            dipole = self.dipoles[i]
            if testingVariables[i][0]: #si le débit du dipole i n'est pas fixé
                variableFlowRateDipole.append(i) 
                if dipole.flowRateMax == None:
                    testMaximalFlowRate = False #si jamais le débit maximum n'est pas fixé on ne peut pas estimer une solution pour commencer l'algorithme
                    print("it should be easier to conoverge if the maximal flow rate of " + str(dipole.name) + " was defined")
            if testingVariables[i][1]:
                variablePressureDipole.append(i)
            if testingVariables[i][0] and testingVariables[i][1]: #s'il n'y a ni le débit ni la différence de pression qui est fixée il doit obligatoirement y avoir la caracteristique du circuit qui est définie
                dipoleWithCaracteristic.append(i)
                if dipole.caracteristic(1.0) == None: #on appelle la fonction il ne faut pas qu'elle retourne None
                    raise ValueError("the hydraulic caracteristic of the dipole " +str(dipole.name)+ "needs to be defined to calcul the hydraulic fonctionnement of the circuit" )


        #les fonctions qu'il va falloir annuler:
        if self.loopLawfunction == None:
            self.loopLaw
        if self.nodesLawFunction == None:
            self.nodesLawFunction
        
        looplaw = self.loopLaw
        nodeslawfunction = self.nodesLawFunction
        
        #on modifie ces fonctions en fixant les paramètres qui ont été fixés précédemment
        def modifiyFunction()
            N = len(variableFlowRateDipole)
            localVariableFlowRate = {variableFlowRateDipole[i] : i for i in range(N)}
            N = len(variablePressureDipole)
            localVariablePressure = {variableFlowRateDipole[i] : i for i in range(N)}
            N = len(self.dipoles)
            localNodesLaw = nodeslawfunction
            def newNodesLaw(QNew): #avec QNew qui réunit tout les débits inconnus QNew[i] = Q[variableFlowRateDipole[i]]
                Q = np.zeros((N,1))
                for id in range(N):
                    if id not in localVariableFlowRate:
                        Q[id] = self.dipoles[id].flow.flowRate

                    else :
                        Q[id] = QNew[localVariableFlowRate[id]]
                return localNodesLaw(Q)
            def newEdgeLaw(Xnew): #Xnew est un mélange de quelques débits tels que leurs dipoles admettent une caracteristique et de quelques pression dont le débit est fixé et la pression est variable
                

    def NodesLaw(self): #les équations vérifiées par les débits Q rangées dans l'ordre croissant des ids
        loopsByEdge = self.loops(self.nodes[0])
        loopsByNode = self.loops(self.nodes[0],by = 'nodes')
        loopNumber = len(loopsByEdge)
        dipoles = [] #liste des dipoles déjà rencontrés
        poles = [] #liste des poles déjà rencontrées
        M = [] #la matrice de l'équation linéaire finale : MQ=0
        NumberOfEquations = 0
        for i in range(loopNumber):
            dipolesNumber = len(self.dipoles)
            loopByNode = loopsByNode[i]
            loopsByEdge = loopsByEdge[i]
            for pole in loopByNode:
                searchDipoles = self.searchEdgesByNodes(pole)
                if pole not in poles:
                    poles.append(pole)
                    yn = []
                    ids = []
                    lignOfM = [0 for i in range(dipolesNumber)]
                    for dipole in searchDipoles:
                            id = dipole[0].id
                            ids.append(id)
                            lignOfM[id] = dipole[1]
                    M.append(lignOfM)
                    NumberOfEquations += 1
        M = np.array(M)
        for i in range(NumberOfEquations):
            MminusLigni = np.delete(M, (i), axis = 0)
            if np.linalg.matrix_rank(M) == np.linalg.matrix_rank(MminusLigni):
                Mnew = MminusLigni
        M = Mnew
        def f():
            Mlocal = M
            def g(P):
                np.array(P)
                return np.dot(Mlocal,P)
            return g
        localNodesLaw = f()
        self.__nodesLawFunction = localNodesLaw
        return localNodesLaw, M
    
    def loopLaw(self):
        F = []
        loopsByEdge = self.loops(self.nodes[0])
        loopsByNode = self.loops(self.nodes[0],by = 'nodes')
        loopNumber = len(loopsByEdge)
        F = []
        for i in range(loopNumber):
            def floop():
                ids = []
                for edge in loopsByEdge[i]:
                    id = edge.id
                    ids.append(id)
                def f(P):
                    sum = 0
                    for id in ids:
                        sum += P[id]
                    return sum
                return f
            F.append(floop())
        def loopLawfunction():
            Nequations = len(F)
            Y = np.zeros((Nequations,1))
            Flocal = F
            def g(P):
                for i in range(Nequations):
                    Y[i] = F[i](P)
                return Y
            return g
        self.__loopLawFunction = loopLawfunction()
        return loopLawfunction()

                    
                    

                            

                    




                        

                

        
