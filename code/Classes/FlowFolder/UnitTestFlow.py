import unittest
import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes")



from Flow import Flow
from FluidFolder.Fluid import Fluid

class TestFlow(unittest.TestCase):
    def setUp(self):
        eau = Fluid()
        self.default = Flow()
        self.flow = Flow(1.0,1.0,1.0,1.0,1.0,eau)

    def test_init(self):
        with self.assertRaises(TypeError):
            self.initTest = Flow(flowRate=1)
            self.initTest = Flow(pressureDifference=1)
            self.initTest = Flow(inputTemperature=1)
            self.initTest = Flow(averageTemperature=1)
            self.initTest = Flow(outletTemperature=1)
            self.initTest = Flow(fluid=1)

    def test_getter(self):
        self.assertEqual(self.default.flowRate, None)
        self.assertEqual(self.flow.flowRate, 1.0)

        self.assertEqual(self.default.pressureDifference, None)
        self.assertEqual(self.flow.pressureDifference, 1.0)

        self.assertEqual(self.default.inputTemperature, None)
        self.assertEqual(self.flow.inputTemperature, 1.0)

        self.assertEqual(self.default.averageTemperature, None)
        self.assertEqual(self.flow.averageTemperature, 1.0)

        self.assertEqual(self.default.outletTemperature, None)
        self.assertEqual(self.flow.outletTemperature, 1.0)

        self.assertEqual(self.default.fluid.name, 'eau')
        self.assertEqual(self.flow.fluid.name, 'eau')
    
    def test_setter(self):
        eau = Fluid()
        self.default.flowRate = 1.0
        self.default.pressureDifference = 1.0
        self.default.inputTemperature = 1.0
        self.default.averageTemperature = 1.0
        self.default.outletTemperature = 1.0
        self.default.fluid = eau

        self.assertEqual(self.default.flowRate, 1.0)
        self.assertEqual(self.default.pressureDifference, 1.0)
        self.assertEqual(self.default.inputTemperature, 1.0)
        self.assertEqual(self.default.averageTemperature, 1.0)
        self.assertEqual(self.default.outletTemperature, 1.0)
        self.assertEqual(self.default.fluid, eau)
        
        with self.assertRaises(TypeError):
            self.default.flowRate = 1
            self.default.pressureDifference = 1
            self.default.inputTemperature = 1
            self.default.averageTemperature = 1
            self.default.outletTemperature = 1
            self.default.fluid = 1
    


        






if __name__ == '__main__':
    unittest.main()