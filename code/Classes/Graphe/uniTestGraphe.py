import unittest
from Graphe import Graph, Node, Edge


class TestGraphe(unittest.TestCase):

    def test_init(self):
        print('\n' + 'test_init')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")

        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)

        edge1 = Edge("edge1", [node1, node2])
        
        graph = Graph([node2, node3],[edge1])
        graph.print()
        self.assertTrue(graph.graphCoherency())

    def test_setNodes(self):
        print('\n' + 'test_setNodes')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")

        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)

        edge1 = Edge("edge1", [node1, node2])

        graph = Graph([node2, node3, node3],[])
        graph.print()
        self.assertTrue(graph.graphCoherency())

    def test_setEdges(self):
        print('\n' + 'test_setEdges')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")

        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)

        edge1 = Edge("edge1", [node1, node2])
        edge2 = Edge("edge2", [node3, node4])

        graph = Graph([],[edge1, edge2])

        graph.print()
        self.assertTrue(graph.graphCoherency())

    def test_appendnode(self):
        print('\n' + 'appendnode')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")
        node6 = Node(name = "node6")
        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)
        node6.addSuccessor(node1)

        edge1 = Edge("edge1", [node1, node2])

        graph = Graph([node2, node3],[edge1])

        graph.appendNode(node5)
        graph.appendNode(node6)
        graph.print()
        self.assertTrue(graph.graphCoherency())

    def test_newEdge(self):
        print('\n' + 'newedge')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")
        node6 = Node(name = "node6")
        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)

        edge1 = Edge("edge1", [node1, node2])

        graph = Graph([node2, node3],[edge1])


        graph.newEdge(node5,node2,'edge3')
        graph.newEdge(node1,node3,'edge4')
        graph.newEdge(node5,node6,'edge5')
        graph.newEdge(node2,node3,'edge6')
        graph.print()
        self.assertTrue(graph.graphCoherency())
    def test_delEdge(self):
        print('\n' + 'delEdge')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")
        node6 = Node(name = "node6")
        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)

        edge1 = Edge("edge1", [node1, node2])

        graph = Graph([node2, node3],[edge1])
        graph.delEdge([node2,node3],by = 'node')
        graph.print()
        self.assertTrue(graph.graphCoherency())
    def test_delNode(self):
        print('\n' + 'delNode')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")
        node6 = Node(name = "node6")
        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)

        edge1 = Edge("edge1", [node1, node2])

        graph = Graph([node2, node3],[edge1])

        graph.delNode(node2, by = 'node')
        graph.print()
        self.assertTrue(graph.graphCoherency())
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")
        node6 = Node(name = "node6")
        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)

        edge1 = Edge("edge1", [node1, node2])

        graph = Graph([node2, node3],[edge1])

        graph.delNode(node3, by = 'node')
        graph.print()
        self.assertTrue(graph.graphCoherency())
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")
        node6 = Node(name = "node6")
        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)

        edge1 = Edge("edge1", [node1, node2])

        graph = Graph([node2, node3],[edge1])

        graph.delNode(node1, by = 'node')
        graph.print()
        self.assertTrue(graph.graphCoherency())

    def test_searchEdgesByNodes(self):
        print('\n' +  'searchByNodes')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")
        node6 = Node(name = "node6")
        node1.addSuccessor(node2)
        node2.addSuccessor(node3)
        edge1 = Edge('edge1',[node1,node2])
        edge2 = Edge('edge2', [node2,node3])
        graph = Graph(nodes = [], edges = [edge1,edge2])
        edges = graph.searchEdgesByNodes(node2)
        for edge in edges:
            print(edge[0].name)
            print(edge[1])
        graph.print()
        
        edge = graph.searchEdgesByNodes([node1, node2])
        self.assertEqual(edge,edge1)
    
    def test_widthSearch(self):
        print('\n' +  'searchByNodes')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")
        node6 = Node(name = "node6")
        node7 = Node(name = "node7")

        edge1 = Edge('edge1',[node1,node2])
        edge2 = Edge('edge2',[node2,node3])
        edge3 = Edge('edge3',[node3,node4])
        edge4 = Edge('edge4',[node4,node5])
        edge5 = Edge('edge5',[node2,node5])
        edge6 = Edge('edge6',[node5,node6])
        edge7 = Edge('edge7',[node6,node1])
        edge8 = Edge('edge8',[node6,node7])
        edge9 = Edge('edge9',[node7,node1])
        graph = Graph(nodes = [], edges = [edge1,edge2,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9])
        graph.print()
        distance, chemins, boucles = graph.widthCourse(node1)
        print(distance)
        print(chemins)
        print(boucles)

    def test_loops(self):
        print('\n' +  'loop')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")
        node6 = Node(name = "node6")
        node7 = Node(name = "node7")

        edge1 = Edge('edge1',[node1,node2])
        edge2 = Edge('edge2',[node2,node3])
        edge3 = Edge('edge3',[node3,node4])
        edge4 = Edge('edge4',[node4,node5])
        edge5 = Edge('edge5',[node2,node5])
        edge6 = Edge('edge6',[node5,node6])
        edge7 = Edge('edge7',[node6,node1])
        edge8 = Edge('edge8',[node6,node7])
        edge9 = Edge('edge9',[node7,node1])
        graph = Graph(nodes = [], edges = [edge1,edge2,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9])
        graph.print()
        loopsByEdges = graph.loops(node1)
        loopsByNodes = graph.loops(node1, 'nodes')
        N = len(loopsByEdges)
        for i in range(N):
            print("loop number :"+ str(i))
            loopByEdges = loopsByEdges[i]
            loopByNodes = loopsByNodes[i]
            edges = []
            nodes = []
            for edge in loopByEdges:
                edges.append(edge.name)
            for node in loopByNodes:
                nodes.append(node.name)
            print('By edges :')
            print(edges)
            print('by nodes :')
            print(nodes)
                

if __name__ == '__main__':
    unittest.main()