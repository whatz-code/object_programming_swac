import unittest
import sys
sys.path.append("./Modules") 
from DipoleModule import Dipole, Pole, Pipe, IdealPump, PlateHeatExchangerSide
from FlowModule import Flow
from FluidModule import Fluid
from HydraulicCircuitModule import HydraulicCircuit
class TestHeadExchanger(unittest.TestCase):

    def test_fonctionnement(self):
        poles = { i : Pole(name = "pole " + str(i)) for i in range(1,8)}
        #On commence par créer la pompe, avec un débit totale de 150 m³/h
        pompe = IdealPump(name = "Pompe", flowRate = 150 / 3600, downstreamPole = poles[1], upstreamPole = poles[2])
        #On crée un dipole hauteur où l'on fixe la différence de pression correspondant à une hauteur de 10m:
        h = 10.0
        masse_volumique_air = 1.2
        g = 9.81
        hauteur = Dipole(name = "altitude", variables = [True, False, True, True], downstreamPole = poles[2], 
                        upstreamPole = poles[3])
        hauteur.flow.pressureDifference = - (hauteur.flow.fluid.volumetricMass - masse_volumique_air) * g * h
        print(hauteur.flow.pressureDifference)
        #On crée chacun des conduits, on fera varier le diamètre du conduit 3 plus tard :
        conduit_1 = Pipe("conduit 1", pipeDiameter = 0.3, downstreamPole = poles[3], upstreamPole = poles[4] )
        conduit_2 = Pipe("conduit 2", pipeDiameter = 0.2, downstreamPole = poles[5], upstreamPole = poles[7] )
        conduit_3 = Pipe("conduit 3", pipeDiameter = 0.1, downstreamPole = poles[6], upstreamPole = poles[7] )
        #enfin on crée les dipoles avec les différences de pressions fixées à 0 pour conneter les poles restants 
        #et fermer le circuit
        dipole_01 = Dipole(name = "dipole_1", variables = [True, False, True, True], downstreamPole = poles[4], upstreamPole = poles[5])
        dipole_01.flow.pressureDifference = 0.0
        dipole_02 = Dipole(name = "dipole_2",variables = [True, False, True, True], downstreamPole = poles[4], upstreamPole = poles[6])
        dipole_02.flow.pressureDifference = 0.0
        dipole_03 = Dipole(name = "dipole_3",variables = [True, False, True, True], downstreamPole = poles[7], upstreamPole = poles[1])
        dipole_03.flow.pressureDifference = 0.0

        circuit_hydraulique = HydraulicCircuit(dipoles = [pompe, hauteur, conduit_1, conduit_2, conduit_3, 
                                                        dipole_01, dipole_02, dipole_03])
        #print permet de visualiser tout les dipoles et poles du circuit:
        circuit_hydraulique.print()
        loops = circuit_hydraulique.loops(poles[1])
        for loop in loops:
            print("\n"+"loop")
            for dipole in loop:
                print(dipole.name)
        #calculons le point foncitonnement du circuit pour les caractéristiques précédentes :

        circuit_hydraulique.resolutionFonctionnement(flowRateMagnitude = 150 / 3600, pressureMagnitude = 100000)
        print("conduit 1", conduit_1.flow.flowRate)
        print("conduit 2", conduit_2.flow.flowRate)
        print("conduit 3", conduit_3.flow.flowRate)
        print("dipole_01", dipole_01.flow.flowRate)
        print("dipole_02", dipole_02.flow.flowRate)
        print("dipole_03", dipole_03.flow.flowRate)
        print("hauteur", hauteur.flow.flowRate)
        print("pompe", pompe.flow.pressureDifference)

        

    def test_pointfunctionnement2(self):
        print('\n' + 'test hydraulic system')
        pole1 = Pole("pole1")
        pole2 = Pole("pole2")
        pole3 = Pole("pole3")
        pole4 = Pole("pole4")
        pole5 = Pole("pole5")
        pump = IdealPump("ideal pump", flowRate=0.233, downstreamPole=pole1,upstreamPole=pole2, inputTemperature=20.0)
        pipe1 = Pipe("pipe1",downstreamPole=pole2, upstreamPole=pole5)
        pipe2 = Pipe("pipe2", downstreamPole=pole5, upstreamPole= pole1)
        pipe3 = Pipe("pipe3", downstreamPole=pole3, upstreamPole=pole4)
        flowOfblanck = Flow(pressureDifference=0.0)
        blanck1 = Dipole("blanck1", flow = flowOfblanck, downstreamPole=pole2, upstreamPole=pole3, variables=[True, False, False, False])
        blanck2 = Dipole("blanck2", flow = flowOfblanck, downstreamPole=pole4, upstreamPole=pole5, variables=[True, False, False, False] )
        hydraulicCircuit = HydraulicCircuit(dipoles = [pump, pipe1, pipe2, pipe3, blanck1, blanck2])
        hydraulicCircuit.print()
        f, M = hydraulicCircuit.nodesLaw()
        hydraulicCircuit.resolutionFonctionnement(flowRateMagnitude = 0.2, pressureMagnitude = 10000)
        print(pipe1.flow.flowRate)
if __name__ == '__main__':
    unittest.main()