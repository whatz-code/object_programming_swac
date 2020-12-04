import sys
sys.path.append("./Classes")
from Calculus import Resolve
from DipoleModule import Pipe, Dipole, PlateHeatExchangerSide, IdealPump, Pole
from GraphModule import Graph, Node, Edge, Queue
from matplotlib import numpy as np
class HydraulicCircuit(Graph):
    """The hydraulicCircuit class is used to represent an assembly of dipoles connected
    by poles.

    Attributes:
        name( type:any ): 
            This parameter gives the user the opportunity to organise his dipole objects.

        dipoles(:obj: Dipole):
            It's a list of dipoles connected by the poles listed in the list poles
            
        poles(:obj: Pole):
            It's a list of poles which connect dipoles between them.
        
        testingVariables (type:list of list of booleans):
            It's a list which repertories all the attribute variables of dipoles.
        
        testingCaracteristics (type:list of list of booleans):
            It's a list which repertories all the attribute caracteristics of dipoles.
        
        testingVariables (type:list of booleans):
            It's a list which repertories all the attribute exchanger of dipoles.

        All of the next attributes are private and are here to memorize the 
        building of functions for future dynamic applications :

            nodesLawFunction(type:function or NoneType):
                It's a function that is equal to 0 when the node law is verified in 
                the circuit.

            loopLawFunction(type:function or NoneType):
                It's a function that is equal to 0 when the loop law is verified in 
                the circuit.
            
            hydraulicSystem(type : function or NoneType):
                It's a function of the variables defined by testing variables, when it's 
                equal to 0, the loop law and the nodes law are verified and the system
                have reached his functionnement point.
    

    """
    def __init__(self,name = 'Hydraulic circuit',dipoles = [],poles = []) : 
        """Class Hydraulic __init__ method : 
        
        Note : 
            The Class HydraulicCircuit represents an assembly of dipoles connected by the poles.
 
            the __init__ method offers the opportunity to give the attributes of the exchanger object.

        Args:
            name( type:any ): 
                this parameters indicates the private attribute name. This parameter gives 
                the user the opportunity to organise his hydraulic circuit objects.

            dipoles(:obj: Dipole):
                It's a list of dipoles connected by the poles listed in the list poles
            
            poles(:obj: Pole):
                It's a list of poles which connect dipoles between them.

        Raises : 
            TypeError : 
                It's raised by the function typeErrorAtEntering when the Types and the object
                don't match with the type and the object defined.

        """
        #raising of exceptions :
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
        testingCaracteristics = []
        testingExchanger = []
        for dipole in self.dipoles:       
            testingVariables.append(dipole.variables)
            testingCaracteristics.append(dipole.caracteristics)
            testingExchanger.append(dipole.exchanger)

        #assign informations attributes :
        self.__testingVariables = testingVariables
        self.__testingCaracteristics = testingCaracteristics
        self.__testingExchanger = testingExchanger

        #assign undefined attributes to the system equations :
        self.__nodesLawFunction = None
        self.__loopLawFunction = None
        self.__hydraulicSystem = None


    @property 
    def testingVariables(self): 
        """ get method and set method to access the private variable testingVariables """
        return self.__testingVariables

    @testingVariables.setter 
    def testingVariables(self,testingVariables): 
        self.__testingVariables = testingVariables
    
    @property 
    def testingCaracteristics(self): 
        """ get method and set method to access the private variable testingCaracteristics """
        return self.__testingCaracteristics

    @testingCaracteristics.setter 
    def testingCaracteristics(self,testingCaracteristics): 
        self.__testingCaracteristics = testingCaracteristics
    
    @property 
    def testingExchanger(self): 
        """ get method and set method to access the private attribute testingExchanger"""
        return self.__testingExchanger

    @testingExchanger.setter 
    def testingExchanger(self,testingExchanger): 
        self.__testingExchanger = testingExchanger

    @property 
    def name(self): 
        """ get method and set method to access the private attribute name """
        return self.__name

    @name.setter 
    def name(self,name): 
        self.__name = namflowRatee

    @property 
    def dipoles(self): 
        """ get method and set method to access the private attribute dipoles"""
        return self.edges

    @dipoles.setter 
    def dipoles(self,dipoles): 
        self.__init__(name = self.name, dipoles = dipoles, poles = [])

    @property 
    def poles(self): 
        """ get method and set method to access the private attribute poles """
        return self.nodes

    @poles.setter 
    def poles(self,poles): 
        self.nodes = poles

    @property 
    def nodesLawFunction(self): 
        """ get method and set method to access the private attribute nodesLawfuntion """
        self.__nodesLawFunction
    
    @nodesLawFunction.setter 
    def nodesLawFunction(self,nodesLawFunction): 
        self.__nodesLawFunction = nodesLawFunction

    @property
    def loopLawFunction(self):
        """ get method and set method to access the private attribute loopLawFunction """
        self.__loopLawFunction

    @loopLawFunction.setter 
    def loopLawFunction(self,loopLawFunction): 
        self.__loopLawFunction = loopLawFunction

    @property 
    def hydraulicSystem(self): 
        """ get method and set method to access the private attribute hydraulicSystem """
        return self.__hydraulicSystem

    @hydraulicSystem.setter 
    def hydraulicSystem(self,hydraulicSystem): 
        self.__hydraulicSystem = hydraulicSystem

    def addDipole(self, dipole, name = None):
        """ function to a dipole in dipoles attribute """
        if not(isinstance(dipole,Dipole)):
                raise TypeError("dipole must a dipole object")

        test = self.appendEdge(dipole)
        if test :
            self.testingVariables.append(dipole.variables)

    def delDipole(self, dipole):
        """ function to del dipole from dipoles """
        self.delEdge( dipole, by = "edge")
        del self.testingVariables[dipole.id]
        del self.testingCaracteristics[dipole.id]
        del self.testingExchanger[dipole.id]

    def testCircuit(self):
        """ this function test if the circuit is possible  """
        if self.edges == []:
            raise ValueError("the circuit must have a dipole")
        if self.opengGraph(): #si un graphe est ouvert il faut nécessairement qu'il y ait du liquide qui rentre de l'extérieur (et donc qu'un noeud n'ait pas de noeud ascendant)
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

    def assignPressure(self, node, pressure):
        node.pressure = pressure
        nodes = self.nodes
        pressureAssign = {node.id : False for node in nodes}

        node.pressure = pressure
        pressureAssign[node.id] = True
        if node not in nodes:
            raise ValueError("the node must be in the graph")
        loops = []

        def exploration(node, queue):
            for successor in node.successors:
                if not(pressureAssign[successor.id]):
                    edge = self.searchEdgesByNodes([node, successor])
                    pressureDifference = edge.flow.pressureDifference
                    successor.pressure = node.pressure  + pressureDifference
                    pressureAssign[successor.id] = True
                    queue.appendQueue(successor)
        queue = Queue([node])
        while queue.emptyQueue() == False:
            node = queue.remove()
            exploration(node, queue)
                




    def resolutionFonctionnement(self, flowRateMagnitude = 0.1 ,pressureMagnitude = 100000.0, buildSystem = False):
        """ This function resole the system and assign the variables to all the dipoles. 
        
            args :
                flowRateMagnitude(type:float):
                    It gives an estimation of the flowRate in all of the dipoles
                    that haven't any estimation yet.
                    unity : m³/h
                
                pressureMagnitude(type:float):
                    It gives an estimation of the pressure difference in all of the dipoles
                    that haven't any estimation yet.
                    unity : m³/h
                """
        if self.hydraulicSystem == None or buildSystem:
            self.BuildingOfHydraulicSystem(buildLaws=True)

        #estimations of the parameters :
        hydraulicSystem = self.hydraulicSystem
        (functionToZero ,XToDipolesFlowRateOnly, XToDipolesUnknownPressureAndUnknownFlowRate,XToDipolesUnknownPressureOnly) = hydraulicSystem
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
            self.dipoles[XToDipolesUnknownPressureAndUnknownFlowRate[key]].flow.pressureDifference = self.dipoles[XToDipolesUnknownPressureAndUnknownFlowRate[key]].hydraulicCaracteristic()

    def BuildingOfHydraulicSystem(self, buildLaws = False):
        """ This function creates the hydraulic systeme from
        the node laws and the loop laws """

        #raising some exceptions : 
        if len(self.edges) == 0:
            raise ValueError("the hydraulic circuit must have at least one dipole")
        if self.openGraph():
            raise ValueError("the hydraulic circuit must be close")

        #taking the information of which variables are fixed :
        testingVariables = self.testingVariables
        #taking the information of which dipoles admit a hydraulic caracteristic:
        testingCaracteristics = self.testingCaracteristics


        #list of ids of dipoles where only the flowRate is variable :
        variableFlowRateDipole = [] 
        #list of ids of dipoles where only the differencePressure is variable :
        variablePressureDipole = [] 
        #list of ids of dipoles where the flowRate and the 
        #differenceOfPressure are variable
        dipoleWithCaracteristic = [] 

        #number of dipoles :
        N = len(self.dipoles) 
        for i in range(N):
            dipole = self.dipoles[i]
            if testingVariables[i][0] and not(testingVariables[i][1]): 
                variableFlowRateDipole.append(i) 
            if testingVariables[i][1] and not(testingVariables[i][0]):
                variablePressureDipole.append(i)
            if testingVariables[i][0] and testingVariables[i][1]: 
                dipoleWithCaracteristic.append(i)
                if not(testingCaracteristics[i][0]):
                    raise ValueError("the hydraulic hydraulicCaracteristic of the dipole " 
                                        +str(dipole.name)+ "needs to be defined to calcul the "
                                        +"hydraulic fonctionnement of the circuit" )

        #all the variables flowRate are stocked :
        allVariableFlowRate = variableFlowRateDipole + dipoleWithCaracteristic

        #all the variable pressure are stocked : 
        allVariablePressure = dipoleWithCaracteristic + variablePressureDipole

        #taking the loop law functions from the attibutes build before:
        if self.__loopLawFunction == None or buildLaws:
            self.loopLaw()
        if self.__nodesLawFunction == None or buildLaws:
            self.nodesLaw()
        loopLaw = self.__loopLawFunction
        nodesLawFunction = self.__nodesLawFunction
        
        def hydraulicFunctionToResolution():
            """ functions rearranged for all the variables  """
            #the value of the flowRates and of the pressures are taken
            listOfQ = []
            listOfP = []
            N =len(self.dipoles)
            for id in range(N):
                listOfQ.append(self.dipoles[id].flow.flowRate)
                listOfP.append(self.dipoles[id].flow.pressureDifference)

            #definition f(id) = indice of the variables 
            N = len(allVariableFlowRate) 
            localVariableFlowRate = {allVariableFlowRate[i] : i for i in range(N)}

            N = len(allVariablePressure)
            localPressureUnknown = {allVariablePressure[i] : i for i in range(N)}

            N = len(dipoleWithCaracteristic)
            localDipoleCaracteristic = {dipoleWithCaracteristic[i] : i for i in range(N)}

            N = len(self.dipoles)
            #redefinition of the nodes Law:
            localNodesLaw = nodesLawFunction
            def newNodesLaw(QNew): #avec QNew qui réunit tout les débits inconnus QNew[i] = Q[variableFlowRateDipole[i]]
                Q = [0 for i in range(N)]
                for id in range(N):
                    if not(id in localVariableFlowRate):
                        Q[id] = listOfQ[id]
                    else :
                        Q[id] = QNew[localVariableFlowRate[id]]
                return localNodesLaw(Q)
            #redefinition of the loop law :
            #list of the dipoles caracteristics :
            F = [] 
            for id in dipoleWithCaracteristic:
                def f():
                    def hydraulicCaracteristic(q, fluid):
                        return self.dipoles[id].hydraulicCaracteristic(q , fluid)
                    hydraulicCaracteristic = self.dipoles[id].hydraulicCaracteristic
                    fluid = self.dipoles[id].flow.fluid
                    def g(q):
                        if q == None:
                            raise ValueError("the flow rate of the dipole " + string(self.dipoles[id].name) + " must be given")
                        return hydraulicCaracteristic(q, fluid)
                    return g
                f = f()
                F.append(f)
            localLoopLaw = loopLaw
            def newEdgeLaw(Xnew): 
                P = [0 for i in range(N)]
                for id in range(N):
                    if not(id in localPressureUnknown):
                        P[id] = listOfP[id] 
                    else:
                        if not(id in localDipoleCaracteristic):
                            P[id] = Xnew[localPressureUnknown[id]] / 10 ** 5
                        else :
                            f = F[localDipoleCaracteristic[id]]
                            if Xnew[localPressureUnknown[id]] < 0:
                                P[id] = f(-Xnew[localPressureUnknown[id]]) / 10 ** 5 
                            else :
                                P[id] = f(Xnew[localPressureUnknown[id]]) / 10 ** 5
                return loopLaw(P)

            #in X are first stocked the variables flowRates, then are stocked the rest :
            X = variableFlowRateDipole + dipoleWithCaracteristic + variablePressureDipole 
            XtoId = {i : X[i] for i in range(N)}
            IdtoX = {X[i] : i for i in range(N)}
            Nflow = len(variableFlowRateDipole)
            Ncarac = len(dipoleWithCaracteristic)
            Npressure = len(variablePressureDipole)
            def hydraulicSystem(X):
                Ydeb = newNodesLaw(X[0:Nflow + Ncarac])
                Ypressure = newEdgeLaw(X[Nflow:])
                return Ydeb + Ypressure

            XtoIdflowRateOnly = {i : X[i] for i in range(0, Nflow)}
            XtoIdpressureOnly = {i : X[i] for i in range(Nflow, Nflow + Ncarac)}
            XtoIdcaracteristic = {i : X[i] for i in range(Nflow + Ncarac, N)}

            return (hydraulicSystem, XtoIdflowRateOnly, XtoIdpressureOnly, XtoIdcaracteristic)
        system = hydraulicFunctionToResolution()
        self.hydraulicSystem = system
        print(self.hydraulicSystem)
        return system


                

    def nodesLaw(self): 
        """ definition of the node law with the topology of the graph """
        M = []
        #for each pole, a node equation is taken :
        for pole in self.poles:
            searchDipoles = self.searchEdgesByNodes(pole)
            lignOfM = [0 for dipole in self.dipoles]
            for dipole in searchDipoles:
                id = dipole[0].id
                lignOfM[id] = dipole[1]
            M.append(lignOfM)
        
        #there is too much equation (too much ligns in the matrice M)
        #some ligns are dependant, it's necessary to minimize the number
        #of ligns :
        M = np.array(M)
        rank = np.linalg.matrix_rank(M)
        def minimumLigns(M):
            numberOfLigns = M.shape[0]
            #if the number of ligns is minimised it's ok 
            if numberOfLigns == rank:
                return M
            else : 
            #else, we recall the function with the matrice minus one lign
            #which is dependent of the other :
                for i in range(numberOfLigns):
                    MminusLigni = np.delete(M, (i), axis = 0)
                    if rank == np.linalg.matrix_rank(MminusLigni):
                        return minimumLigns(MminusLigni)
        #We define the new matrice and compute the function associate
        M = minimumLigns(M)
        def f():
            Mlocal = M
            def g(P):
                """ This function take all flowRates into argument (sorted by id) """
                P = np.array(P, dtype=object)
                Y = np.dot(Mlocal,P)
                Y = [Y[i] for i in range(len(Y))]
                return Y
            return g
        localNodesLaw = f()
        self.nodesLawFunction = f()

        return localNodesLaw, M
    
    def loopLaw(self):
        """ definition of the loop law with the topology of the graph : """
        #first we take all the loops by calling the function 
        #we assumed that if the graph hydraulic circuit is possible,
        #every loop are taking into account
        loopsByEdge = self.loops(self.nodes[0])
        loopNumber = len(loopsByEdge)
        #we define a vector F which contains each loop law equation
        F = []
        for i in range(loopNumber):
            #for each loop we defibe a function 
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
                """ this function take all the pressure differences into argumen """
                for i in range(Nequations):
                    Y[i] = F[i](P)
                return Y
            return g
        self.loopLawFunction = loopLawfunction()
        return loopLawfunction()

                    
                    

                            

                    




                        

                

        
