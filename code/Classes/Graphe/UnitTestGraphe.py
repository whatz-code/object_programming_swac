import unittest
from Graphe import Graph, Node, Edge


class TestNode(unittest.TestCase):
    def setUp(self):
        self.default = Node()
        self.node = Node(name = 1,id = 1,successors = [self.default])

    def test_init(self):
        with self.assertRaises(TypeError):
            self.initTest = Node(id = 0.1)
            self.initTest = Node(successors=1)
            self.initTest = Node(successors=[1])
        with self.assertRaises(ValueError):
            self.initTest = Node(id = -1)
            

    def test_getter(self):
        self.assertEqual(self.default.name, None)
        self.assertEqual(self.node.name, 1)

        self.assertEqual(self.default.id, 0)
        self.assertEqual(self.node.id, 1)

        self.assertEqual(self.default.successors, [])
        self.assertEqual(self.node.successors[0].successors, [])
    
    def test_setter(self):
        default = Node()
        self.default.name = 1.0
        self.default.id = 1
        self.default.successors = [default]

        self.assertEqual(self.default.name, 1.0)
        self.assertEqual(self.default.id, 1)
        self.assertEqual(self.default.successors, [default])

        
        with self.assertRaises(TypeError):
            self.default.id = 1.0
            self.default.successors = 1
            self.default.successors = [1]
        with self.assertRaises(ValueError):
            self.default.id = -1
    


class TestEdge(unittest.TestCase):
    def setUp(self):
        self.node1 = Node(name = "node1")
        self.node2 = Node(name = "node2")
        print(type(self.node1))
        self.defaultEdge = Edge(nodes = [self.node1, self.node2])
        self.edge = Edge(name = 1,id = 1,nodes = [self.node1, self.node2])


    def test_init(self):
        with self.assertRaises(TypeError):
            self.initTest = Edge(id = 0.1)
            self.initTest = Edge(nodes=1)
            self.initTest = Edge(nodes=[1,2])

        with self.assertRaises(ValueError):
            self.initTest = Edge(nodes=[1])
            self.initTest = Edge(nodes=[self.node1])
            self.initTest = Edge(id = -1)
        self.assertEqual(self.defaultEdge.nodes[0].successors, [self.node2])
        self.assertEqual(self.defaultEdge.nodes[1].successors, [])
            

    def test_getter(self):
        self.assertEqual(self.defaultEdge.name, None)
        self.assertEqual(self.edge.name, 1)

        self.assertEqual(self.defaultEdge.id, 0)
        self.assertEqual(self.edge.id, 1)

        self.assertEqual(self.defaultEdge.nodes, [self.node1, self.node2])
        self.assertEqual(self.edge.nodes, [self.node1, self.node2])
    
    def test_setter(self):
        self.node3 = Node(name = "node3")
        self.defaultEdge.name = 1.0
        self.defaultEdge.id = 1
        self.defaultEdge.nodes = [self.node1, self.node3]

        self.assertEqual(self.defaultEdge.name, 1.0)
        self.assertEqual(self.defaultEdge.id, 1)
        self.assertEqual(self.defaultEdge.nodes[0].successors, [self.node3])
        self.assertEqual(self.defaultEdge.nodes[1].successors, [])

        
        with self.assertRaises(TypeError):
            self.defaultEdge.id = 1.0
            self.defaultEdge.nodes = 1
            self.defaultEdge.nodes = [1,2]
        with self.assertRaises(ValueError):
            self.defaultEdge.id = -1
            self.defaultEdge.nodes = [1]
            self.defaultEdge.nodes = [self.node2]






if __name__ == '__main__':
    unittest.main()