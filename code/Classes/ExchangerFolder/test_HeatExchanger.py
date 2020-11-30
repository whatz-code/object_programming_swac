import unittest
from HeatExchanger import HeatExchanger, PlateExchanger
import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole") 
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid") 
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes") 
from Dipole import Pole
from HydraulicThermicCalculus import HydraulicThermicCalculus
from Flow import Flow

from Fluid import Fluid
class TestHeadExchanger(unittest.TestCase):
    def setUp(self):

        self.heatExchanger1 = PlateExchanger(streakWaveLength=1.0)
        self.heatExchanger2 = PlateExchanger(streakWaveLength = 1.0)
        self.heatExchanger1.hydraulicDipole1.flow.flowRate = 0.23
        self.heatExchanger1.hydraulicDipole2.flow.flowRate = 0.28
  
    def test_attributes_getter(self):
        #materialConductivity
        self.assertEqual(self.heatExchanger1.materialConductivity, 22)
        self.assertEqual(self.heatExchanger2.materialConductivity,21.9)
        #exchangerSurface
        self.assertEqual(self.heatExchanger1.exchangeSurface, 700)
        self.assertEqual(self.heatExchanger2.exchangeSurface,600)
        #hydraulicDipole1
        self.assertEqual(self.heatExchanger1.hydraulicDipole1.length, self.heatExchanger1.length)
        self.assertEqual(self.heatExchanger2.hydraulicDipole1.length, self.heatExchanger2.length)
        #globalThermicCoefficient
        self.assertEqual(self.heatExchanger1.globalThermicCoefficient, 6000)
        self.assertEqual(self.heatExchanger2.globalThermicCoefficient, 5000)
        #width
        self.assertEqual(self.heatExchanger1.width, 2)
        self.assertEqual(self.heatExchanger2.width,1)
        #plateNumber
        self.assertEqual(self.heatExchanger1.plateNumber, 388)
        self.assertEqual(self.heatExchanger2.plateNumber,385)
        #passeNumber
        self.assertEqual(self.heatExchanger1.passeNumber, 4)
        self.assertEqual(self.heatExchanger2.passeNumber,1)
        #plateThickness
        self.assertEqual(self.heatExchanger1.plateThickness, 0.8)
        self.assertEqual(self.heatExchanger2.plateThickness, 0.5)
        #plateGap
        self.assertEqual(self.heatExchanger1.plateGap, 4)
        self.assertEqual(self.heatExchanger2.plateGap, 3)
        #angle
        self.assertEqual(self.heatExchanger1.angle, 56)
        self.assertEqual(self.heatExchanger2.angle, 45)
        #streakWaveLength
        self.assertEqual(self.heatExchanger1.streakWaveLength, 1.5)
        self.assertEqual(self.heatExchanger2.streakWaveLength, 1)
    
    def test_thermicTransfertCoefficient(self):
        eau = Fluid()
        reynolds1 = 1000000.0
        reynolds2 = 100000.0
        Prandtl = HydraulicThermicCalculus.prandtl()
        print(self.heatExchanger1.thermicTransfertCoefficient(reynolds1,Prandtl,reynolds2,Prandtl,eau,eau))
        print(self.heatExchanger2.thermicTransfertCoefficient(reynolds1,Prandtl,reynolds2,Prandtl,eau,eau))

    def test_outletTemperatureCalcul(self):
        self.heatExchanger1.hydraulicDipole1.flow.entryTemperature = 17.0
        self.heatExchanger1.hydraulicDipole2.flow.entryTemperature = 22.0
        averagePressure = 100000.0
        estimationOutletTemperature1 = 17.0
        estimationOutletTemperature2 = 21.0 
        print(self.heatExchanger1.outletTemperatureCalcul(estimationOutletTemperature1=estimationOutletTemperature1, estimationOutletTemperature2=estimationOutletTemperature2, averagePressure1=averagePressure, averagePressure2=averagePressure))



if __name__ == '__main__':
    unittest.main()