from matplotlib import numpy as np
class Graph:
#l'initialisation de la classe : 

    def TestEqualityOfEdges(edge1, edge2):
        if type(edge1) is not Edge or type(edge2) is not Edge:
            raise TypeError("it must be two edges")
        if edge1.nodes == edge2.nodes:
            return True
        return False

        if edge1.nodes == edge2.nodes:
            return True

    def __init__(self, nodes = [], edges = []) : 
        
        if type(nodes) is not list:
            raise TypeError("nodes must be a list of nodes")
        for node in nodes :
            if type(node) is not Node:
                raise TypeError("nodes must ba list of nodes")

        if type(edges) is not list:
            raise TypeError("edges must be a list of edges")
        for edge in edges :
            if type(edge) is not Edge:
                raise TypeError("edges must be a list of edges")
        

        for node in nodes:
            for successor in node.successors:
                if successor not in nodes:
                    node.delSuccessor(successor, by = 'node')
        for edge in edges:
            for node in edge.nodes:
                    nodes.append(node)

        for node in nodes:
            for successor in node.successors:
                newEdge = True
                for edge in edges:
                    if edge.nodes == [node, successor]:
                        newEdge = False
                if newEdge :
                    edges.append(Edge(nodes = [node, successor]))
        
        nodes = list(set(nodes))
        edges = list(set(edges))

        i = 0
        for node in nodes:
            node.id = i
            i += 1
        i = 0
        for edge in edges:
            edge.id = i
            i += 1
    
        self.__nodes = nodes
        self.__edges = edges

    @property 
    def nodes(self): 
        return self.__nodes

    @nodes.setter 
    def nodes(self,nodes): 
        if type(nodes) is not list:
            raise TypeError("nodes must be a list of nodes")
        for node in nodes :
            if type(node) is not Node:
                raise TypeError("nodes must ba list of nodes")
        i = 0
        nodes = list(set(nodes))
        for node in nodes:
            node.id = i
            i += 1
        edges = []
        for node in nodes:
            for successor in node.successors:
                edges.append(Edge(nodes = [node, successor]))
        i = 0
        for edge in edges:
            edge.id = i
            i += 1
        self.__nodes = nodes
        self.__edges = edges

    @property 
    def edges(self): 
        return self.__edges

    @edges.setter 
    def edges(self,edges):
        if type(edges) is not list:
            raise TypeError("edges must be a list of edges")
        for edge in edges :
            if type(edge) is not Edge:
                raise TypeError("edges must be a list of edges")
        
        nodes = []
        for edge in edges:
            for node in edge.nodes:
                if node not in nodes:
                    nodes.append(node)
        for node in nodes:
            for successor in node.successors:
                if successor not in nodes:
                    node.delSuccessor(successor, by = 'node')
        for node in nodes:
            for successor in node.successors:
                newEdge = True
                for edge in edges:
                    if edge.nodes == [node, successor]:
                        newEdge = False
                if newEdge :
                    edges.append(Edge(nodes = [node, successor]))

        nodes = list(set(nodes))
        i = 0
        for node in nodes:
            node.id = i
            i += 1
        edges = list(set(edges))
        i = 0
        for edge in edges:
            edge.id = i
            i += 1
        self.__edges = edges
        self.__nodes = nodes

    def appendNode(self,node):
        if type(node) is not Node:
            raise TypeError("node must be a node object")
        node.id = len(self.nodes)
        self.nodes.append(node)
        for node1 in node.successors:
            self.newEdge(node, node1)

    def newEdge(self, node1, node2, name = None):
        if type(node1) is not Node or type(node2) is not Node:
            raise TypeError("nodes schould be node objects")
        edge = Edge(name, nodes = [node1, node2])
        newEdge = True
        for edge in self.edges:
            if edge.nodes[0] == node1 and edge.nodes[1] == node2:
                newEdge = False
        if newEdge:
            edge.id = len(self.edges)
            self.edges.append(edge)

    def delNode(self, var, by = 'id', delEdge = True):
        N = len(self.nodes)
        newVar = var

        if by == 'name':
            for j in range(N):
                if nodes[j].name == var:
                    newVar = id
        if by == 'node':
            for j in range(N):
                if nodes[j] == var:
                    newVar = id
        
        var = newVar
        for node in self.nodes:
            node.delSuccessor(var, by = 'id')
        if delEdge :
            for edge in self.edges:
                if edge.nodes[0].id == var or edge.nodes[1].id == var :
                    self.delEdge(edge, 'edge', delNode = False)
        suppr = False
        for j in range(N):
            if suppr == True:
                if j < N:
                    self.nodes[j-1].id -= 1
            if j < N-1:
                if self.nodes[j].id == var:
                    del self.__nodes[j]
                    suppr = True

    def delEdge(self, var, by = 'id', delNode = True):
        N = len(self.edges)

        newVar = var
        if by == 'name':
            for j in range(N):
                if edges[j].name == var:
                    newVar = id

        if by == 'edge':
            for j in range(N):
                if edges[j] == var:
                    newVar = id
        var = newVar

        if delNode :
            for edge in self.edges:
                if edge.id == var :
                    self.delNode(edge.nodes[0].id, delEdge = False)
                    self.delNode(edge.nodes[1].id, delEdge = False)
        suppr = False
        for j in range(N):
            if suppr == True:
                if j < N:
                    self.edges[j-1].id -= 1
            if j < N-1:
                if self.edges[j].id == var:
                    del self.__edges[j]
                    suppr = True




        if by == 'name':
            if delNode : 
                for edge in self.edges:
                    if edge.name == var :
                        self.delNode(edge.nodes[0].id, delEdge = False)
                        self.delNode(edge.nodes[1].id, delEdge = False)
            suppr = False
            for j in range(N):
                if suppr == True:
                    if j < N:
                        self.edges[j-1].id -= 1
                if j < N-1:
                    if self.edges[j].name == var:
                        del self.__edges[j]
                        suppr = True
        if by == 'edge':
            if delNode : 
                for edge in self.edges:
                    if edge == var :
                        self.delNode(edge.nodes[0].id, delEdge = False)
                        self.delNode(edge.nodes[1].id, delEdge = False)
            suppr = False
            for j in range(N):
                if suppr == True:
                    if j < N:
                        self.edges[j-1].id -= 1
                if j < N-1:
                    if self.edges[j] == var:
                        del self.__edges[j]
                        suppr = True

    def print(self):
        Nodeids = []
        NodeSuccessors = []
        Edgeids = []
        NodeNames = []
        EdgeNames = []
        EdgeNodes = []
        for node in self.nodes:
            Nodeids.append(node.id)
            NodeNames.append(node.name)
            Successors = []
            for successor in node.successors:
                Successors.append(successor.name)

            NodeSuccessors.append(Successors)
        for edge in self.edges:
            Edgeids.append(edge.id)
            EdgeNames.append(edge.name)
            EdgeNodes.append([edge.nodes[0].name, edge.nodes[1].name])
        print('Nodes id')
        print(Nodeids)
        print('Edge id')
        print(Edgeids)
        print('Nodes name')
        print(NodeNames)
        print('Nodes successors')
        print(NodeSuccessors)
        print('Edge name')
        print(EdgeNames)
        print('Edge nodes')
        print(EdgeNodes)

    def adjencyMatrix(self):
        N = len(self.nodes)
        MAdjency = np.zeros((N,N))
        for edge in self.edges:
            lign = edge.nodes[0].id
            column = edge.nodes[1].id
            MAdjency[lign, column] = 1
        return MAdjency

    def searchNodeByName(self, name):
        for node in self.nodes:
            if node.name == name:
                return(node)
            raise ValueError("there is no node called by this name")
    
    def widthSearch(self, node): #ne fonctionne qu'avec des graphes orientés
        distance = {node0.id : [] for node0 in self.nodes}
        chemins = {node0.id : [] for node0 in self.nodes}   #Tout les chemins qui ont mené au noeud correspondant à l'id 
        boucles = [] #liste de toute les boucles auxquelles appartient node
        def exploration(node, queue, distance, chemins,boucles): #toNotFollow indique l'id du noeud qu'il ne faut pas suivre pour un graphe non orientee
            for successor in node.successors:
                id0 = node.id
                id = successor.id
                distance[id].append(distance[id0][-1]+1)
                boucle = False
                chemin = chemins[id0][-1]
                newChemin = chemin + [id]
                chemins[id].append(newChemin)
                if id in chemin :
                    boucle = True
                    boucles.append(newChemin)
                if not(boucle):
                    queue.appendQueue(successor.id)
        queue = Queue([node.id]) #structure de queue qui va permettre l'exploration en largeur
        distance[node.id].append(0) #permet d'assigner à chaque noeud sa distance au noeud d'origine
        chemins[node.id].append([node.id])
        while queue.emptyQueue() == False:
            id0 = queue.remove()
            toNotFollow = id0
            node = self.nodes[id0]
            exploration(node, queue, distance,chemins,boucles)

        return(distance, chemins, boucles)

    def distance(node1,node2):
        distancesToNode1, chemins, boucles = widthSearch(self, node1)
        distancesToNode2 = distancesToNode1[node2.id]

    def voisins(self, node):
        for edge in self.edges:
            if edge.nodes[0] == node:
                return [edge.nodes[1],-1]
            if edge.nodes[1] == node:
                return [edge.nodes[0],1]

    def searchEdgesByNodes(self, Node):
        edges = []
        for edge in self.edges:
            if edge.nodes[0] == node:
                edges.append([edge,0])
            if edge.nodes[1] == node:
                edges.append([edge,1])

    def graphCoherency(self):
        nodesInEdges = []
        nodes = self.nodes
        edges = self.edges
        successorsInEdges = {node.id : set([]) for node in nodes}
        visuSuccessorsInEdges = {node.id : set([]) for node in nodes}
        for edge in edges:
            nodesInEdges.append(edge.nodes[0])
            nodesInEdges.append(edge.nodes[1])
            id = edge.nodes[0].id 
            successorsInEdges[id].add(edge.nodes[1])
            visuSuccessorsInEdges[id].add(edge.nodes[1].name)
        print(visuSuccessorsInEdges)
        nodesInEdges = set(nodesInEdges)
        setOfNodes = set(nodes)
        nodesSet = setOfNodes == nodesInEdges

        if nodesSet:
            for node in nodes:
                id = node.id
                if set(node.successors) != successorsInEdges[id]:
                    return False
            return True


        return False

    




class Node:
    #l'initialisation de la classe : 
    def __init__(self, name = None, id = 0, successors = []): 
        self.__name = name
        if type(id) is type(1):
            if id >= 0:
                self.__id = id
            else :
                raise ValueError("id must be a positive integer")
        else :
            raise TypeError("id must be a positive integer")
        
        if type(successors) is list:
            for successor in successors :
                if type(successor) is not Node :
                    raise TypeError("successors must be a list of nodes")
            self.__successors = list(set(successors))
        else :
            raise TypeError("successors must be a list of nodes")
    @property 
    def name(self): 
        return self.__name

    @name.setter 
    def name(self,name): 
        self.__name = name
    
    @property 
    def id(self): 
        return self.__id
    @id.setter 
    def id(self,id): 
        if type(id) is type(1):
            if id >= 0:
                self.__id = id
            else :
                raise ValueError("id must be a positive integer")
        else :
            raise TypeError("id must be a positive integer")

    @property 
    def successors(self): 
        return self.__successors

    @successors.setter 
    def successors(self,successors): 
        if type(successors) is type([]):
            for successor in successors :
                if type(successor) is not Node :
                    raise TypeError("successors must be a list of nodes")
            self.__successors = list(set(successors))
        else :
            raise TypeError("successors must be a list of nodes")

    def addSuccessor(self, *nodes):
        for node in nodes:
            if type(node) is Node:
                if node not in self.__successors:
                    self.__successors.append(node)
            else :
                raise TypeError("successor must be a node")

    def delSuccessor(self, var, by = 'id'):
        N = len(self.successors)
        if by == 'id':
            for j in range(N):
                if j < N-1:
                    if self.successors[j].id == var:
                        del self.__successors[j]
        if by == 'name':
            for j in range(N):
                if j < N-1:
                    if self.successors[j].name == var:
                        del self.__successors[j]
        if by == 'node':
                self.__successors.remove(var)

class Edge:
    def __init__(self, name = None, nodes = None, id = 0):
        self.__name = name
        node = Node()
        if type(nodes) is type([]):
            if len(nodes) == 2:
                for node in nodes:
                    if type(node) is not type(node):
                        raise TypeError("nodes must be a list of 2 objects node")
                if nodes[1] not in nodes[0].successors:
                    nodes[0].addSuccessor(nodes[1])
                self.__nodes = nodes
            else : 
                raise ValueError("nodes must be a list of 2 objects node")

        else:
            raise TypeError("nodes must be a list of 2 objects node")
        
        if type(id) is type(1):
            if id >= 0:
                self.__id = id
            else :
                raise ValueError("id must be a positive integer")
        else :
            raise TypeError("id must be a positive integer")

    @property 
    def nodes(self): 
        return self.__nodes
    @nodes.setter
    def nodes(self,nodes): 
        node = Node()
        if type(nodes) is type([]):
            if len(nodes) == 2:
                for node in nodes:
                    if type(node) is not type(node):
                        raise TypeError("nodes must be a list of 2 objects node")
                if nodes[1] in nodes[0].successors:
                    raise ValueError("it can only be one edge for 2 nodes")
                else :
                    self.nodes[0].delSuccessor(self.nodes[1], by = 'node')
                    nodes[0].addSuccessor(nodes[1])
                    self.__nodes = nodes
            else : 
                raise ValueError("nodes must be a list of 2 objects node")
        else:
            raise TypeError("nodes must be a list of 2 objects node")
    
    @property 
    def name(self): 
        return self.__name

    @name.setter 
    def name(self,name): 
        self.__name = name
    
    @property 
    def id(self): 
        return self.__id

    @id.setter 
    def id(self,id): 
        if type(id) is type(1):
            if id >= 0:
                self.__id = id
            else :
                raise ValueError("id must be a positive integer")
        else :
            raise TypeError("id must be a positive integer")




class Queue:
    def __init__(self, queue = []):
        self.__queue = queue

    @property 
    def queue(self): 
        return self.__queue

    @queue.setter 
    def queue(self,queue): 
        self.__queue = queue
    
    def remove(self):
        element = self.__queue[0]
        del self.__queue[0]
        return element
    def emptyQueue(self):
        return self.queue == []
    def appendQueue(self,object):
        return self.queue.append(object)

#petits tests

# node1 = Node(name = "node1")
# node2 = Node(name = "node2")
# node3 = Node(name = "node3").append(
# node4 = Node(name = "node4")
# node1.successors = [node2,node4]         
# node2.successors = [node1,node3]
# node3.successors = [node                for edge in self.edges:
# node4.successors = [node1,node3]
# graphNonOriente = Graph([node1,node2,node3,node4])
# adjacenceMatrix = graphNonOriente.adjencyMatrix()
# distancenode1NonOriente, cheminsNonOriente = graphNonOriente.widthSearch(node1)

# node1o = Node(name = "node1o")
# node2o = Node(name = "node2o")
# node3o = Node(name = "node3o")
# node4o = Node(name = "node4o")
# node5o = Node(name = "node5o")
# node6o = Node(name = "node6o")
# node1o.successors = [node2o]         
# node2o.successors = [node3o, node5o]
# node3o.successors = [node4o]
# node4o.successors = [node1o]
# node5o.successors = [node6o]
# node6o.successors = [node3o]
# graphOriente = Graph([node1o,node2o,node3o,node4o,node5o,node6o])
# adjacenceMatrix = graphOriente.adjencyMatrix()
# distancenode1Oriente, cheminsOriente, bouclesOriente = graphOriente.widthSearch(node1o)
# L = [node1o.id, node2o.id, node3o.id, node4o.id, node5o.id, node6o.id]
# graphOriente.print()
# print(L)
# graphOriente.delNode(3)
# graphOriente.print()
# print(L)
# node3o = Node(name = "node3o")
# node3o.successors = [node4o]
# graphOriente.appendNode(node3o)
# graphOriente.print()
# print(L)


# print(adjacenceMatrix)
# print(distancenode1Oriente)
# print(cheminsOriente)
# print(bouclesOriente)