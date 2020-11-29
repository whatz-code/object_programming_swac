import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Graphe")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole")
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes")
from Calculus import Resolve
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
        self.__variables = ['flowRate', 'pressureDifference', 'temperatureDifference']
        self.__dipoles = self.edges
        self.__poles = self.nodes

        testingVariables = []
        for dipole in self.dipoles:       
            testingVariables.append(dipole.variables)
        self.__testingVariables = testingVariables
        self.__nodesLawFunction = None
        self.__loopLawFunction = None
        self.__nodesLawToResolve = None
        self.__loopLawToResolve = None
        self.__hydraulicSystem = None


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
        self.__name = namflowRatee

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
    
    @nodesLawFunction.setter 
    def nodesLawFunction(self,nodesLawFunction): 
        self.__nodesLawFunction = nodesLawFunction

    @property
    def loopLawFunction(self):
        self.__loopLawFunction

    @loopLawFunction.setter 
    def loopLawFunction(self,loopLawFunction): 
        self.__loopLawFunction = loopLawFunction

    @property 
    def nodesLawToResolve(self): 
        self.__nodesLawToResolve

    @nodesLawToResolve.setter 
    def nodesLawToResolve(self,nodesLawToResolve): 
        self.__nodesLawToResolve = nodesLawToResolve

    @property 
    def loopLawToResolve(self): 
        self.__loopLawToResolve

    @loopLawToResolve.setter 
    def loopLawToResolve(self,loopLawToResolve): 
        self.__loopLawToResolve = loopLawToResolve

    @property 
    def hydraulicSystem(self): 
        self.__hydraulicSystem

    @hydraulicSystem.setter 
    def hydraulicSystem(self,hydraulicSystem): 
        self.__hydraulicSystem = hydraulicSystem
    
    def resetVariables(self):
        N = len(self.dipoles)
        for i in range(N):
            dipole = self.dipoles[i]
            variablesDipole = self.testingVariables[i]
            if variablesDipole[0]:
                dipole.flow.flowRate = None
            if variablesDipole[1]:
                dipole.flow.pressureDifference = None
            if variablesDipole[2]:
                dipole.flow.temperatureDifference = None




    def addDipole(self, dipole, name = None):
        if not(isinstance(dipole,Dipole)):
                raise TypeError("dipole must a dipole object")

        pole1 = dipole.downstreamPole
        pole2 = dipole.upstreamPole
        self.newEdge(pole1, pole2, name = name)
        self.testingVariables.append(dipole.variables)

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


    def resolutionFonctionnement(self, flowRateMagnitude = 0.1 ,pressureMagnitude = 100000.0 ):
        if self.__hydraulicSystem == None:
            self.hydraulicSystem()
        hydraulicSystem = self.__hydraulicSystem
        (functionToZero ,XToDipolesFlowRateOnly, XToDipolesUnknownPressureOnly,XToDipolesUnknownPressureAndUnknownFlowRate) = hydraulicSystem
        X0 = []
        for key in XToDipolesFlowRateOnly:
            flowRateEstimation = self.dipoles[XToDipolesFlowRateOnly[key]].flow.flowRate
            if flowRateEstimation != None:
                X0.append(flowRateEstimation)
            else :
                X0.append(flowRateMagnitude)
        for key in XToDipolesUnknownPressureAndUnknownFlowRate:
            flowRateEstimation = self.dipoles[XToDipolesUnknownPressureAndUnknownFlowRate[key]].flow.flowRate
            if flowRateEstimation != None:
                X0.append(flowRateEstimation)
            else :
                X0.append(flowRateMagnitude)
        for key in XToDipolesUnknownPressureOnly:
            pressureDifferenceEstimation = self.dipoles[XToDipolesUnknownPressureOnly[key]].flow.pressureDifference
            if pressureDifferenceEstimation != None:
                X0.append(pressureDifferenceEstimation)
            else :
                X0.append(pressureMagnitude)
        X0 = np.array(X0)
        solution = Resolve.multiDimensionnalNewtonResolution(functionToZero,X0)
        solution = [float(s) for s in solution]
        for key in XToDipolesFlowRateOnly:
            self.dipoles[XToDipolesFlowRateOnly[key]].flow.flowRate = solution[key]
        for key in XToDipolesUnknownPressureOnly:
            self.dipoles[XToDipolesUnknownPressureOnly[key]].flow.pressureDifference = solution[key]
        for key in XToDipolesUnknownPressureAndUnknownFlowRate:
            self.dipoles[XToDipolesUnknownPressureAndUnknownFlowRate[key]].flow.flowRate = solution[key]
            self.dipoles[XToDipolesUnknownPressureAndUnknownFlowRate[key]].flow.pressureDifference = self.dipoles[XToDipolesUnknownPressureAndUnknownFlowRate[key]].caracteristic()

        




    def hydraulicSystem(self):
        if self.nodesLawToResolve == None:
            nodesLawToResolve = self.variablesAndEquationsOfHydraulicFunctionnement()[0]
            loopLawToResolve = self.variablesAndEquationsOfHydraulicFunctionnement()[1]
        else : 
            nodesLawToResolve = self.nodesLawToResolve
            loopLawToResolve = self.loopLawToResolve

        nodeLaw = nodesLawToResolve[0]
        loopLaw = loopLawToResolve[0]

        dipolesFlowRateToX = nodesLawToResolve[1]
        dipolesUnknownPressureToX = loopLawToResolve[3]
        dipolesUnknownPressureAndUnknownFlowRateToX = loopLawToResolve[2]

        XToDipolesFlowRateOnly = {}
        XToDipolesUnknownPressureOnly = {}
        XToDipolesUnknownPressureAndUnknownFlowRate = {}
        N = len(self.dipoles)
        IdsInX = []
        for key in dipolesFlowRateToX:
            if not(key in dipolesUnknownPressureAndUnknownFlowRateToX):
                IdsInX.append(key)
                XToDipolesFlowRateOnly[len(IdsInX)-1] = key
        for key in dipolesFlowRateToX:
            if key in dipolesUnknownPressureAndUnknownFlowRateToX:    
                IdsInX.append(key)
                XToDipolesUnknownPressureAndUnknownFlowRate[len(IdsInX)-1] = key
        for key in dipolesUnknownPressureToX:
            IdsInX.append(key)
            XToDipolesUnknownPressureOnly[len(IdsInX)-1] = key
        if len(IdsInX) < N:
            raise ValueError("there is not enough equations")
        Ndeb = len(XToDipolesFlowRateOnly)
        Ncarac = len(XToDipolesUnknownPressureAndUnknownFlowRate)
        Npressure = len(XToDipolesUnknownPressureOnly)
        def buildOfSystem(X):
            X = X.reshape((len(X)))
            Ydeb = nodeLaw(X[0:Ndeb + Ncarac])
            Ypressure = loopLaw(X[Ndeb:])
            Y = Ydeb + Ypressure
            return Y
        self.__hydraulicSystem = (buildOfSystem,XToDipolesFlowRateOnly, XToDipolesUnknownPressureOnly,XToDipolesUnknownPressureAndUnknownFlowRate)
        return (buildOfSystem,XToDipolesFlowRateOnly, XToDipolesUnknownPressureOnly,XToDipolesUnknownPressureAndUnknownFlowRate)
            

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
        dipoleWithCaracteristic = [] #on fait une liste des ids dans lesquels ni la différence de pression est connue ni le débit n'est connue
        variablePressureDipole = [] #on fait une liste des ids dans lesquels la différence de pression est inconnue
        for i in range(N):
            dipole = self.dipoles[i]
            if testingVariables[i][0] and not(testingVariables[i][1]): #si le débit du dipole i n'est pas fixé
                variableFlowRateDipole.append(i) 
            if testingVariables[i][1]:
                variablePressureDipole.append(i)
            if testingVariables[i][0] and testingVariables[i][1]: #s'il n'y a ni le débit ni la différence de pression qui est fixée il doit obligatoirement y avoir la caracteristique du circuit qui est définie
                dipoleWithCaracteristic.append(i)
                if dipole.caracteristic(1.0) == None: #on appelle la fonction il ne faut pas qu'elle retourne None
                    raise ValueError("the hydraulic caracteristic of the dipole " +str(dipole.name)+ "needs to be defined to calcul the hydraulic fonctionnement of the circuit" )
        pressureIsUnknown = [] #on fait une liste d'ids dans laquelle la pression sera l'inconnue : tel que la pression est variable et n'admet pas de caractéristique
        for id in variablePressureDipole:
            if id not in dipoleWithCaracteristic:
                pressureIsUnknown.append(id)
        variableFlowRateDipole = variableFlowRateDipole + dipoleWithCaracteristic
        #les fonctions qu'il va falloir annuler:
        if self.__loopLawFunction == None:
            self.loopLaw()
        if self.__nodesLawFunction == None:
            self.nodesLaw()
        loopLaw = self.__loopLawFunction
        nodesLawFunction = self.__nodesLawFunction
        
        #on modifie ces fonctions en fixant les paramètres qui ont été fixés précédemment
        def hydraulicFunctionToResolution():
            N = len(variableFlowRateDipole) 
            localVariableFlowRate = {variableFlowRateDipole[i] : i for i in range(N)}
            N = len(variablePressureDipole)
            localVariablePressure = {variablePressureDipole[i] : i for i in range(N)}
            N = len(pressureIsUnknown)
            localPressureUnknown = {pressureIsUnknown[i] : i for i in range(N)}
            N = len(dipoleWithCaracteristic)
            localDipoleCaracteristic = {dipoleWithCaracteristic[i] : i for i in range(N)}
            N = len(self.dipoles)
            localNodesLaw = nodesLawFunction
            listOfQ = []
            listOfP = []
            for id in range(N):
                listOfQ.append(self.dipoles[id].flow.flowRate)
                listOfP.append(self.dipoles[id].flow.pressureDifference)
            X = dipoleWithCaracteristic + pressureIsUnknown
            N = len(X)
            allUnknownPressure = {X[i] : i for i in range(N)}
            def newNodesLaw(QNew): #avec QNew qui réunit tout les débits inconnus QNew[i] = Q[variableFlowRateDipole[i]]
                Q = [0 for i in range(N)]
                for id in range(N):
                    if not(id in localVariableFlowRate):
                        Q[id] = listOfQ[id]
                    else :
                        Q[id] = QNew[localVariableFlowRate[id]]
                return localNodesLaw(Q)
            N = len(self.dipoles)
            F = [] #La liste des fonctions caracteristiques des dipoles qui en admettent (F(Q) = DeltaP)
            for id in dipoleWithCaracteristic:
                def f():
                    def caracteristic(q, fluid):
                        return self.dipoles[id].caracteristic(q , fluid)
                    caracteristic = self.dipoles[id].caracteristic
                    fluid = self.dipoles[id].flow.fluid
                    def g(q):
                        if q == None:
                            raise ValueError("the flow rate of the dipole " + string(self.dipoles[id].name) + " must be given")
                        return caracteristic(q, fluid)
                    return g
                f = f()
                F.append(f)
            localLoopLaw = loopLaw
            def newEdgeLaw(Xnew): #Xnew est un mélange de quelques débits tels que leurs dipoles admettent une caracteristique et de quelques pression dont le débit est fixé et la pression est variable
                P = [0 for i in range(N)]
                for id in range(N):
                    if not(id in allUnknownPressure):
                        P[id] = listOfP[id]
                    else:
                        if not(id in localDipoleCaracteristic):
                            P[id] = Xnew[allUnknownPressure[id]] / 10 ** 5
                        else :
                            f = F[localDipoleCaracteristic[id]]
                            if Xnew[allUnknownPressure[id]] < 0:
                                P[id] = f(-Xnew[allUnknownPressure[id]]) / 10 ** 5
                            else :
                                P[id] = f(Xnew[allUnknownPressure[id]]) / 10 ** 5
                return loopLaw(P)
            return [(newNodesLaw, localVariableFlowRate),(newEdgeLaw, allUnknownPressure, localDipoleCaracteristic, localPressureUnknown)]
        equations = hydraulicFunctionToResolution()
        self.nodesLawToResolve = equations[0]
        self.loopLawToResolve = equations[1]
        return [equations[0],equations[1]]


                

    def nodesLaw(self): #les équations vérifiées par les débits Q rangées dans l'ordre croissant des ids
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
                p = np.array(P)
                Y = np.dot(Mlocal,P)
                Y = [Y[i] for i in range(len(Y))]
                return Y
            return g
        localNodesLaw = f()
        self.nodesLawFunction = f()

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
            Y = [0 for i in range(Nequations)]
            Flocal = F
            def g(P):
                for i in range(Nequations):
                    Y[i] = F[i](P)
                return Y
            return g
        self.loopLawFunction = loopLawfunction()
        return loopLawfunction()

                    
                    

                            

                    




                        

                

        
