import unittest
from Calculus import Resolve

class TestCalculus(unittest.TestCase):

    def test_jacobian(self):
        def f(X):
            return [X[0] ** 2 + X[1],  - X[1]]
        jac = Resolve.estimationJacobian(f, [1,1])
        print(jac)
    def test_NewtonMethod(self):
        def f(X):
            return [X[0], X[1]]
        sol = Resolve.multiDimensionnalNewtonResolution(f, [1,1])
        print(sol)
if __name__ == '__main__':
    unittest.main()