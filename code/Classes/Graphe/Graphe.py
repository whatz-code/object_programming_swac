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
                    edges.append(Edge([node, successor]))
            
        if definedBy == "edges":
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
        self.__nodes = nodes

    @property 
    def edges(self): 
        return self.__edges

    @edges.setter 
    def edges(self,edges): 
        self.__edges = edges

    def appendNode(self,node):
        node.id = len(self.nodes)
        self.nodes.append(node)

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
            print(queue.queue)
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

class Edge:
    def __init__(self, nodes = None, objectToEdge = None):
        if len(nodes) == 2:
            self.__nodes = nodes
        self.__objectToEdge = objectToEdge
    
    @property 
    def nodes(self): 
        return self.__nodes

    @nodes.setter 
    def nodes(self,nodes): 
        self.__nodes = nodes

    @property 
    def objectToEdge(self): 
        return self.__objectToEdge

    @objectToEdge.setter 
    def objectToEdge(self,objectToEdge): 
        self.__objectToEdge = objectToEdge


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
# node3.successors = [node2,node4]
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

# print(adjacenceMatrix)
# print(distancenode1Oriente)
# print(cheminsOriente)
# print(bouclesOriente)