from matplotlib import numpy as np
class Graph:
#l'initialisation de la classe : 
    def __init__(self,nodes = None) : 
        i = 0
        for node in nodes:
            node.id(i)
            i=i+1
        self.__nodes = nodes
    @property 
    def nodes(self): 
        return self.__nodes

    @nodes.setter 
    def nodes(self,nodes): 
        self.__nodes = nodes

    def adjencyMatrix(self):
        N = len(self.nodes)
        MAdjency = np.zeros(N,N)
        i = 0
        for node in self.nodes:
            ligne = node.id
            for successor in node.successors:
                column = successor.id
                MAdjency[ligne,column] = 1
        return MAdjency

class Node:
    #l'initialisation de la classe : 
    def __init__(self, name = None, id = 0, successors = None): 
        self.__name = name
        self.__id = id
        self.__successors = successors

        return self.__nodes
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


node1 = Node(name = "node1")
print(type(node1))
node2 = Node(name = "node2")
node3 = Node(name = "node3")
node4 = Node(name = "node4")
node1.successors = [node2,node4]         
node2.successors = [node1,node3]
node3.successors = [node2,node4]
node4.successors = [node1,node3]
graph = Graph([node1,node2,node3,node4])
adjacenceMatrix = graph.adjencyMatrix()