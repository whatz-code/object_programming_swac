from matplotlib import numpy as np
class Graph:
    """The Graph class is used to represent a graph constituted of edges and 
        Nodes.

        Attributes:
            Nodes(type:list of :obj: Node):
            Edges(type:list of :obj: Node):
        

        """
    def __init__(self, nodes = [], edges = []) : 
        nodes = []
        """The __init__ method of the class allows the graph 
        to initialise his attributes

        Args:
            Nodes(type:list of :obj: Node):
            Edges(type:list of :obj: Node):
        
        Raises: 
            If the types don't match.

        """

        #raising exceptions :
        if type(nodes) is not list:
            raise TypeError("nodes must be a list of nodes")
        for node in nodes :
            if not(isinstance(node,Node)):
                raise TypeError("nodes must be a list of nodes")

        if type(edges) is not list:
            raise TypeError("edges must be a list of edges")
        for edge in edges :
            if not(isinstance(edge,Edge)):
                raise TypeError("edges must be a list of edges")
        

        #first we add the nodes of edges
        for edge in edges:
            if edge.nodes[1] not in edge.nodes[0].successors:
                edge.nodes[0].addSuccessor(edge.nodes[1])
            for node in edge.nodes:
                if node not in nodes:
                    nodes.append(node)

        #next we clean all the successors of nodes
        #which are out of the graph.
        self.delSuccessorsOut(nodes)

        #new edges are created if there is 
        #successor correspondant.
        for node in nodes:
            for successor in node.successors:
                newEdge = True
                for edge in edges:
                    if edge.nodes[0] == node and edge.nodes[1] == successor:
                        newEdge = False
                if newEdge:
                    edge = Edge(name = "newedge", nodes = [node, successor])
                    edges.append(edge)
                    if node not in nodes:
                        nodes.append(node)
                    if successor not in nodes:
                        nodes.append(successor)
        
        #suppr of the doublons :
        nodes = list(set(nodes))
        edges = list(set(edges))

        #assign a unique id to all edges and nodes
        #such as self.nodes[i] = self.nodes.id
        # and self.edges[i] = self.edges.id
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
        """ get and set of the private attribute nodes """
        return self.__nodes

    @nodes.setter 
    def nodes(self,nodes): 
        self.__init__(nodes = nodes, edges = [])


    @property 
    def edges(self): 
        """ get and set of the private attribute edges """
        return self.__edges

    @edges.setter 
    def edges(self,edges):
        self.__init__(nodes = [], edges = edges)


    def appendNode(self,node):
        """"To add a node to the graph"""
        if not(isinstance(node,Node)):
            raise TypeError("node must be a node object")
        if node not in self.nodes :
            node.id = len(self.nodes)
            self.nodes.append(node)
            for nodeTo in node.successors:
                self.newEdge(node, nodeTo)
            self.delSuccessorsOut(self.nodes)
    
    def appendEdge(self, edge):
        """ To add a edge to the graph """
        if edge not in self.edges:
            appendEdge = True
            node1 = edge.nodes[0]
            node2 = edge.nodes[1]
            for edgei in self.edges:
                node1i = edgei.nodes[0]
                node2i = edgei.nodes[1]
                if node1 == edge.nodes[0] and node2 == self.nodes[1]:
                    appendEdge = False
            if appendEdge:
                edge.id = len(self.edges)
                self.edges.append(edge)
                self.appendNode(node1)
                self.appendNode(node2)
                return True
            


    def newEdge(self, node1, node2, name = None):
        """ To create newEdge with between to nodes """
        if not(isinstance(node1,Node)) or not(isinstance(node2,Node)):
            raise TypeError("nodes schould be node objects")
        
        if edge not in self.edges:
            newEdge = True
            for edge in self.edges:
                if edge.nodes[0] == node1 and edge.nodes[1] == node2:
                    newEdge = False
            if newEdge:
                edge = Edge(name, [node1, node2])
                if node2 not in node1.successors:
                    node1.addSuccessor(node2)
                edge.id = len(self.edges)
                self.edges.append(edge)
                if node1 not in self.nodes:
                    node1.id = len(self.nodes)
                    self.nodes.append(node1)
                if node2 not in self.nodes:
                    node2.id = len(self.nodes)
                    self.nodes.append(node2)

            self.delSuccessorsOut(self.nodes)

    def delNode(self, var, by = 'id', delEdge = True):
        """ To suppr a node """
        N = len(self.nodes)
        newVar = -1
        edges = self.edges[:]
        if by == 'name':
            for j in range(N):
                if self.nodes[j].name == var:
                    newVar = j
        if by == 'node':
            for j in range(N):
                if self.nodes[j] == var:
                    newVar = j
        
        var = newVar
        if newVar >= 0 and newVar < N :
            if delEdge :
                for edge in edges:
                    if edge.nodes[0].id == var or edge.nodes[1].id == var :
                        self.delEdge(edge, by = 'edge', delNode = False)
            del self.nodes[var]
            for i in range(len(self.nodes)):
                self.nodes[i].id = i

    def delEdge(self, var, by = 'id', delNode = False):
        """ To suppr a edge """
        N = len(self.edges)

        newVar = -1
        if by == 'name':
            for j in range(N):
                if self.edges[j].name == var:
                    newVar = j

        if by == 'edge':
            for j in range(N):
                if self.edges[j] == var:
                    newVar = j

        if by == 'nodes':
            if type(var) is not list:
                raise TypeError('var must be a list of 2 nodes')
            if len(var) != 2 :
                raise TypeError('var must be a list of 2 nodes')
            if not(isinstance(var[0],Node)) or not(isinstance(var[1],Node)) :
                raise TypeError('var must be a list of 2 nodes')
            for j in range(N):
                if self.edges[j].nodes[0] == var[0] and self.edges[j].nodes[1] == var[1]:
                    newVar = j
        var = newVar
        if newVar >= 0 and newVar < N :
            for edge in self.edges:
                if edge.id == var :
                    if delNode : 
                        self.delNode(edge.nodes[0].id, delEdge = False)
                        self.delNode(edge.nodes[1].id, delEdge = False)
                    edge.nodes[0].delSuccessor(edge.nodes[1], by = 'node')
            del self.edges[var]
            for i in range(len(self.edges)):
                self.edges[i].id = i


    def delSuccessorsOut(self, nodes):
        """ To clean successors that are not in the graph """
        if type(nodes) is not list:
            raise TypeError("nodes must be a list of nodes")
        for node in nodes :
            if not(isinstance(node,Node)):
                raise TypeError("nodes must ba list of nodes")
        for node in nodes:
            for successor in node.successors:
                if successor not in nodes:
                    node.delSuccessor(successor, by = 'node')

        
    def print(self):
        """ To print the propreties of the graph """
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
        """ To create an adjancy matrix """
        N = len(self.nodes)
        MAdjency = np.zeros((N,N))
        for edge in self.edges:
            lign = edge.nodes[0].id
            column = edge.nodes[1].id
            MAdjency[lign, column] = 1
        return MAdjency

    def searchNodeByName(self, name):
        """ to search a node by name """
        for node in self.nodes:
            if node.name == name:
                return(node)
            raise ValueError("there is no node called by this name")
    
    def widthCourse(self, node): 
        """ To travel in width """
        if not(isinstance(node,Node)):
            raise TypeError('node must be node type')
        distance = {node0.id : [] for node0 in self.nodes}
        chemins = {node0.id : [] for node0 in self.nodes}   
        cheminsName = {node0.name : [] for node0 in self.nodes}  
        boucles = [] 
        def exploration(node, queue, distance, chemins,boucles): 
            for successor in node.successors:
                id0 = node.id
                name0 = node.name
                id = successor.id
                name = successor.name
                distance[id].append(distance[id0][-1]+1)
                boucle = False
                chemin = chemins[id0][-1]
                cheminName = cheminsName[name0][-1]
                newChemin = chemin + [id]
                newCheminName = cheminName + [name]
                chemins[id].append(newChemin)
                cheminsName[name].append(newCheminName)
                if id in chemin :
                    boucle = True
                    boucles.append(newChemin)
                if not(boucle):
                    queue.appendQueue(successor.id)
        queue = Queue([node.id]) 
        distance[node.id].append(0)
        chemins[node.id].append([node.id])
        cheminsName[node.name].append([node.name])
        while queue.emptyQueue() == False:
            id0 = queue.remove()
            toNotFollow = id0
            node = self.nodes[id0]
            exploration(node, queue, distance,chemins,boucles)
        return(distance, chemins, boucles)

    def loops(self, node):
        """ To travel in depth """
        if not(isinstance(node,Node)):
            raise TypeError('node must be node type')
 
        #creating a function which identifies the first loop
        #it can be find and modify the graph to search another.
        def loopIdentification(id, graphByIds, loops):
            pile = [id]
            test_loop = False
            loop = []
            ascent = False
            while not ascent :
                id = pile[-1]
                successors = graphByIds[id]
                if len(successors) != 0:
                    if successors[0] in pile:
                        id0 = successors[0]
                        pile2 = pile[:]
                        loop.append(id0)
                        id = None
                        while id!=id0:
                            id = pile2.pop()
                            loop.append(id)
                        loops.append(loop)
                        test_loop = True
                        ascent = True
                    else :
                        pile.append(successors[0])
                else : 
                    pile.pop()
                    ascent = True
            newGraph = False
            while not newGraph and len(pile) > 0:
                id = pile[-1]
                successors = graphByIds[id]
                if len(successors) > 1:
                    successors.pop(0)
                    newGraph = True
                pile.pop()
            return test_loop, newGraph

        nodes = self.nodes
        graphByIds = {}
        #starting by creating an another representation of the graph
        #to not affect the class
        for node in nodes:
            id = node.id
            successors = []
            for successor in node.successors:
                successors.append(successor.id)
            successors = list(set(successors))
            graphByIds[id] = successors

        loops = []
        id = node.id
        test_loop = True
        newGraph = True
        while test_loop and newGraph:
            test_loop, newGraph = loopIdentification(id, graphByIds, loops)
        loopsByEdges = []
        for loop in loops:
            loopByEdges = []
            N = len(loop)
            nodes = self.nodes
            loop.reverse()
            for j in range(1,N):
                loopByEdges.append(self.searchEdgesByNodes([nodes[loop[j-1]], 
                                                            nodes[loop[j]]]))
            loopsByEdges.append(loopByEdges)

        return loopsByEdges        


    def distance(node1,node2):
        """ give the distance between 2 nodes """
        if not(isinstance(node1,Node)) or not(isinstance(node2,Node)):
            raise TypeError('node must be node type')
        distancesToNode1, chemins, boucles = self.widthCourse(node1)
        distancesToNode2 = distancesToNode1[node2.id]
        
    def searchEdgesByNodes(self, nodes):
        """ give all the edges for given nodes :
            Args:
                nodes(:obj: Node or list of 2 Node):
            Returns:
                If 2 nodes :
                    The edge if it is connected by the two nodes
                If 1 node :
                    list [[edge, +-1], ...] : it forms a list for all the 
                    edges connected to the node, if the edge TO the node, it
                    gives the coefficient +1, if not, it gives the coefficient
                    -1. 
                     
                     """
        if type(nodes) is  list:
            if not(len(nodes) == 2):
                raise TypeError("nodes must be a node or a list of 2 nodes")
            for node in nodes:
                    if not(isinstance(node,Node)) :
                        raise TypeError("nodes must be a node or a list of 2 nodes")
            for edge in self.edges:
                if edge.nodes[0] == nodes[0] and edge.nodes[1] == nodes[1]:
                    return edge
        else:
            if not(isinstance(nodes,Node)):
                raise TypeError("nodes must be a node or a list of 2 nodes")
            edges = []
            for edge in self.edges:
                if edge.nodes[0] == nodes:
                    edges.append([edge,1])
                if edge.nodes[1] == nodes:
                    edges.append([edge,-1])
            return edges


    def graphCoherency(self):
        """ returns false if the graph is not coherent """
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
        nodesInEdges = set(nodesInEdges)
        setOfNodes = set(nodes)

        for node in nodes:
            id = node.id
            if set(node.successors) != successorsInEdges[id]:
                return False
        return True


        return False

    def openGraph(self):
        """ return True if the graph is open. """
        open = False
        for node in self.nodes:
            if node.successors == []:
                return True
        return open

    





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
                if not(isinstance(successor,Node)):
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
                if not(isinstance(successor,Node)) :
                    raise TypeError("successors must be a list of nodes")
            self.__successors = list(set(successors))
        else :
            raise TypeError("successors must be a list of nodes")

    def addSuccessor(self, *nodes):
        for node in nodes:
            if isinstance(node,Node):
                if node not in self.__successors:
                    self.__successors.append(node)
            else :
                raise TypeError("successor must be a node")

    def delSuccessor(self, var, by = 'id'):
        N = len(self.successors)
        if by == 'id':
            for j in range(N-1):
                if self.successors[j].id == var:
                    del self.__successors[j]
                if self.successors[-1].id == var:
                    del self.__successors[-1]
        if by == 'name':
            for j in range(N-1):
                if self.successors[j].name == var:
                    del self.__successors[j]
                if self.successors[-1].name == var:
                    del self.__successors[-1]
        if by == 'node':
                self.__successors.remove(var)




class Edge:
    def __init__(self, name = None, nodes = None, id = 0):
        self.__name = name
        node = Node()
        if type(nodes) is type([]):
            if len(nodes) == 2:
                for node in nodes:
                    if not(isinstance(node,Node)):
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
                    if not(isinstance(node,Node)):
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
