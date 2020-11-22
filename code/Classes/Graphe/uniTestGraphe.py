import unittest
from Graphe import Graph, Node, Edge


class TestGraphe(unittest.TestCase):

    def test_init(self):
        print('test_init')
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
        print('test_setNodes')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")

        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)

        edge1 = Edge("edge1", [node1, node2])

        graph = Graph([node2, node3],[edge1])
        graph.nodes = [node2, node3, node4]
        graph.print()
        self.assertTrue(graph.graphCoherency())

    def test_setEdges(self):
        print('test_setEdges')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")

        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)

        edge1 = Edge("edge1", [node1, node2])

        edge2 = Edge("edge2", [node3, node4])
        graph = Graph([node2, node3],[edge1])
        graph.edges = [edge1, edge2]

        graph.print()
        self.assertTrue(graph.graphCoherency())

    def test_appendnode(self):
        print('appendnode')
        node1 = Node(name = "node1")
        node2 = Node(name = "node2")
        node3 = Node(name = "node3")
        node4 = Node(name = "node4")
        node5 = Node(name = "node5")

        node1.addSuccessor(node2)
        node2.addSuccessor(node3,node4)

        edge1 = Edge("edge1", [node1, node2])

        graph = Graph([node2, node3],[edge1])
        graph.appendNode(node5)
        self.assertEqual(graph.nodes[-1], node5)
        self.assertTrue(graph.graphCoherency())
        graph.print()

    

if __name__ == '__main__':
    unittest.main()