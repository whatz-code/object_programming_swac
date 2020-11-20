from matplotlib import numpy as np
class Graph:
#l'initialisation de la classe : 
    def __init__(self, nodes = None, edges = None, definedBy = "nodes") : 
        if definedBy == "nodes":
            i = 0
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
            
        if definedBy == "edges":
            i = 0
            for edge in edges:
                edge.id = i
                i += 1
            nodes = []
            for edge in edges:
                for node in edge.nodes:
                    if not(node in nodes):
                        nodes.append(node)
            i = 0
            for node in nodes:
                node.id = i
                i += 1
    
        self.__nodes = nodes
        self.__edges = edges

    @property 
    def nodes(self): 
        return self.__nodes

    @nodes.setter 
    def nodes(self,nodes): 
        i = 0
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
        i = 0
        for edge in edges:
            edge.id = i
            i += 1
        nodes = []
        for edge in edges:
            for node in edge.nodes:
                if not(node in nodes):
                    nodes.append(node)
        i = 0
        for node in nodes:
            node.id = i
            i += 1
        self.__edges = edges
        self.__nodes = nodes

    def appendNode(self,node):
        node.id = len(self.nodes)
        self.nodes.append(node)
        for node1 in node.successors:
            self.newEdge(node, node1)

    def newEdge(self, node1, node2, name = None):
        edge = Edge(name, nodes = [node1, node2])
        edge.id = len(self.edges)
        self.edges.append(edge)
    def delNode(self, var, by = 'id', delEdge = True):
        N = len(self.nodes)
        if by == 'id':
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
        if by == 'name':
            for node in self.nodes:
                node.delSuccessor(var, by = 'name')
            if delEdge :
                for edge in self.edges:
                    if edge.nodes[0].name == var or edge.nodes[1].name == var :
                        self.delEdge(edge, 'edge', delNode = False)
            suppr = False
            for j in range(N):
                if suppr == True:
                    if j < N:
                        self.nodes[j-1].id -= 1
                if j < N-1:
                    if self.nodes[j].name == var:
                        del self.__nodes[j]
                        suppr = True
        if by == 'node':
            for node in self.nodes:
                node.delSuccessor(var, by = 'node')
            if delEdge :
                for edge in self.edges:
                    if edge.nodes[0] == var or edge.nodes[1] == var :
                        self.delEdge(edge, 'edge', delNode = False)
            suppr = False
            for j in range(N):
                if suppr == True:
                    if j < N:
                        self.nodes[j-1].id -= 1
                if j < N-1:
                    if self.nodes[j] == var:
                        del self.__nodes[j]
                        suppr = True
    def delEdge(self, var, by = 'id', delNode = True):
        N = len(self.edges)
        if by == 'id':
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


    def print(self, by = 'id'):
        Nodeids = []
        Edgeids = []
        for node in self.nodes:
            Nodeids.append(node.id)
        for edge in self.edges:
            Edgeids.append(edge.id)
        print('Nodes id')
        print(Nodeids)
        print('Edge id')
        print(Edgeids)

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

    




class Node:
    #l'initialisation de la classe : 
    def __init__(self, name = None, id = 0, successors = None): 
        self.__name = name
        self.__id = id
        self.__successors = successors

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
        self.__id = id

    @property 
    def successors(self): 
        return self.__successors

    @successors.setter 
    def successors(self,successors): 
        self.__successors = successors

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
                for j in range(N):
                    if j < N-1:
                        if self.successors[j] == var:
                            del self.__successors[j]

class Edge:
    def __init__(self, name = None, nodes = None, id = 0):
        self.__nodes = nodes
        self.__id = id
    @property 
    def nodes(self): 
        return self.__nodes

    @nodes.setter 
    def nodes(self,nodes): 
        self.__nodes = nodes
    
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
        self.__id = id



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

node1o = Node(name = "node1o")
node2o = Node(name = "node2o")
node3o = Node(name = "node3o")
node4o = Node(name = "node4o")
node5o = Node(name = "node5o")
node6o = Node(name = "node6o")
node1o.successors = [node2o]         
node2o.successors = [node3o, node5o]
node3o.successors = [node4o]
node4o.successors = [node1o]
node5o.successors = [node6o]
node6o.successors = [node3o]
graphOriente = Graph([node1o,node2o,node3o,node4o,node5o,node6o])
adjacenceMatrix = graphOriente.adjencyMatrix()
distancenode1Oriente, cheminsOriente, bouclesOriente = graphOriente.widthSearch(node1o)
L = [node1o.id, node2o.id, node3o.id, node4o.id, node5o.id, node6o.id]
graphOriente.print()
print(L)
graphOriente.delNode(3)
graphOriente.print()
print(L)
node3o = Node(name = "node3o")
node3o.successors = [node4o]
graphOriente.appendNode(node3o)
graphOriente.print()
print(L)


# print(adjacenceMatrix)
# print(distancenode1Oriente)
# print(cheminsOriente)
# print(bouclesOriente)