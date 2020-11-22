import unittest
from Graphe import Graph, Node, Edge


class TestNode(unittest.TestCase):
    def setUp(self):
        self.default = Node(successors=[])
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
        self.default.successors = []

        self.assertEqual(self.default.name, 1.0)
        self.assertEqual(self.default.id, 1)
        self.assertEqual(self.default.successors, [])

        
        with self.assertRaises(TypeError):
            self.default.id = 1.0
            self.default.successors = 1
            self.default.successors = [1]
        with self.assertRaises(ValueError):
            self.default.id = -1
    
    def test_addSuccessor(self):
        node1 = Node()
        node2 = Node()
        print(node2)
        node1.addSuccessor(node2)
        self.assertEqual(node1.successors, [node2])
        print(node2)
        with self.assertRaises(TypeError):
            node1.addSuccessor(1)

    def test_delSuccessor(self):
        node1 = Node(name = 'a')
        node2 = Node(name = 'b', id = 1)
        node1.addSuccessor(node2, node1)
        node1.delSuccessor(0)
        self.assertEqual(node1.successors,[node2])
        node1.addSuccessor(node1)
        node1.delSuccessor('b', by = 'name')
        self.assertEqual(node1.successors, [node1])
        node1.addSuccessor(node2)
        node1.delSuccessor(node1, by = 'node')
        self.assertEqual(node1.successors, [node2])



if __name__ == '__main__':
    unittest.main()