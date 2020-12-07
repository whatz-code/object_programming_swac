import unittest
import sys
sys.path.append("./Modules") 
from GraphModule import Graph, Edge, Node


class TestGraph(unittest.TestCase):

    def test_loop2_graph_1(self):
        node_1 = Node("n 1")
        node_2 = Node("n 2")
        node_3 = Node("n 3")
        node_4 = Node("n 4")
        node_5 = Node("n 5")
        node_6 = Node("n 6")
        node_1.addSuccessor(node_2)
        node_2.addSuccessor(node_3)
        node_3.addSuccessor(node_4)
        node_4.addSuccessor(node_2, node_1, node_5)
        node_5.addSuccessor(node_6)
        node_6.addSuccessor(node_1)
        graph = Graph(nodes = [node_1,node_2, node_3, node_4, node_5,node_6])
        loops = graph.loops_2(node_1)
        print("graph 1", loops)
    def test_loop2_graph_2(self):
        nodes = {i : Node("n "+str(i)) for i in range(1,8)}
        nodes[1].addSuccessor(nodes[2])
        nodes[2].addSuccessor(nodes[3], nodes[4])
        nodes[3].addSuccessor(nodes[5])
        nodes[4].addSuccessor(nodes[5])
        nodes[5].addSuccessor(nodes[6])
        nodes[6].addSuccessor(nodes[7])
        nodes[7].addSuccessor(nodes[1])
        list_nodes = [nodes[i] for i in range(1,8)]
        graph = Graph(nodes = list_nodes)
        loops = graph.loops_2(nodes[1])
        print("graph 2", loops)
    def test_loop2_graph_3(self):
        nodes = {i : Node("n "+str(i)) for i in range(1,5)}
        edges_1 = Edge("e 1", [nodes[1], nodes[2]])
        edges_2 = Edge("e 2", [nodes[2], nodes[3]])
        edges_3 = Edge("e 3", [nodes[3], nodes[4]])
        edges_4 = Edge("e 4", [nodes[4], nodes[1]])
        graph = Graph(edges = [edges_1, edges_2, edges_3, edges_4])
        loops = graph.loops_2(nodes[1])
        for loop in loops:
            print("loop :")
            for edge in loop:
                print(edge.name)
if __name__ == '__main__':
    unittest.main()