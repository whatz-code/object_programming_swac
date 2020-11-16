import sys
sys.path.append("/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes")
from CreationClasses import writeClass
pathToAttributes = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Fluid/Fluid_v_0.csv'
pathToInitClass = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid/InitFluid.py'

writeClass(pathToAttributes,pathToInitClass)
