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
    


        






if __name__ == '__main__':
    unittest.main()