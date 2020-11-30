import unittest
import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid") 
from Fluid import Fluid
class TestFluid(unittest.TestCase):
    def setUp(self):
        self.eau = Fluid()
        self.fluid = Fluid('quelconque',100.0, 0.02,42.0,0.8)
    def test_init(self):
        with self.assertRaises(TypeError):
            self.initTest = Fluid(volumetricMass=1)
            self.initTest = Fluid(dynamicViscosity=1)
            self.initTest = Fluid(thermicCapacity=1)
            self.initTest = Fluid(thermicConductivity=1)
    def test_getter(self):
        self.assertEqual(self.eau.name, 'eau')
        self.assertEqual(self.fluid.name, 'quelconque')

        self.assertEqual(self.eau.volumetricMass, float(1000))
        self.assertEqual(self.fluid.volumetricMass, 100.0)
        
        self.assertEqual(self.eau.dynamicViscosity, 0.001)
        self.assertEqual(self.fluid.dynamicViscosity, 0.02)
        
        self.assertEqual(self.eau.thermicCapacity, float(4150))
        self.assertEqual(self.fluid.thermicCapacity, 42.0)
        
        self.assertEqual(self.eau.thermicConductivity, 0.6)
        self.assertEqual(self.fluid.thermicConductivity, 0.8)
    
    def test_setter(self):
        self.eau.name = 'blue'
        self.eau.volumetricMass = float(1)
        self.eau.dynamicViscosity = float(1)
        self.eau.thermicCapacity = float(1)
        self.eau.thermicConductivity = float(1)
        self.assertEqual(self.eau.name, 'blue')
        self.assertEqual(self.eau.volumetricMass, float(1))
        self.assertEqual(self.eau.dynamicViscosity, float(1))
        self.assertEqual(self.eau.thermicCapacity, 1.0)
        self.assertEqual(self.eau.thermicConductivity, 1.0)
        
        with self.assertRaises(TypeError):
            self.eau.volumetricMass = 1
            self.eau.dynamicViscosity = 1
            self.eau.thermicCapacity = 1
            self.eau.thermicConductivity = 1
    
    def test_volumetricMassEvolutionDefinition(self):
        def realDependancy(temperature, pressure):
            if temperature < 1000:
                raise ValueError('pas dans le domaine de définition')
        def falseDepdendancy(temp=1):
            pass
        with self.assertRaises(ValueError):
            self.eau.volumetricMassEvolutionDefinition(realDependancy)
        with self.assertRaises(TypeError):
            self.eau.volumetricMassEvolutionDefinition(1)
            self.eau.volumetricMassEvolutionDefinition(falseDependancy)

        






if __name__ == '__main__':
    unittest.main()