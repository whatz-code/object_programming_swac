import unittest
from Graphe import Graph, Node, Edge


class TestEdge(unittest.TestCase):

    def test_init(self):
        node1 = Node(name = "node1",id = 0,successors=[])
        node2 = Node(name = "node2")
        node3 = Node()
        with self.assertRaises(TypeError):
            initTest = Edge(id = 0.1)
            initTest = Edge(nodes=1)
            initTest = Edge(nodes=[1,2])

        with self.assertRaises(ValueError):
            initTest = Edge(nodes=[1])
            initTest = Edge(nodes=[node1])
            initTest = Edge(id = -1)
            

    def test_getter(self):
        node1 = Node(name = "node1",id = 0,successors=[])
        node2 = Node(name = "node2")
        node3 = Node()
        default = Edge(nodes = [node1, node2])
        edge = Edge(name = 1, id = 1, nodes = [node1, node3])

        self.assertEqual(default.name, None)
        self.assertEqual(edge.name, 1)

        self.assertEqual(default.id, 0)
        self.assertEqual(edge.id, 1)

        self.assertEqual(default.nodes, [node1, node2])
        self.assertEqual(edge.nodes, [node1, node3])
    
    def test_setter(self):
        node1 = Node(name = "node1",id = 0,successors=[])
        node2 = Node(name = "node2")
        
        default = Edge(nodes = [node1, node2])

        node3 = Node(name = "node3")
        default.name = 1.0
        default.id = 1
        default.nodes = [node1, node3]

        self.assertEqual(default.name, 1.0)
        self.assertEqual(default.id, 1)
        self.assertEqual(default.nodes[0].successors, [node3])
        self.assertEqual(default.nodes[1].successors, [])

        
        with self.assertRaises(TypeError):
            default.id = 1.0
            default.nodes = 1
            default.nodes = [1,2]
        with self.assertRaises(ValueError):
            default.id = -1
            default.nodes = [1]
            default.nodes = [node2]
            edge = Edge(nodes = [node1, node3])





if __name__ == '__main__':
    unittest.main()