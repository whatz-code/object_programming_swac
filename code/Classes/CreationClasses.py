
from CSVtoArray import extraction

#Cette fonction va permettre d'écrire l'initialisation d'une classe automatiquement en ayant remplie 
#préalablement un tableau avec les attributs.

def writeClass(pathToAttributes, pathToInitClass):
    attributes = extraction(pathToAttributes)
    with open(pathToInitClass,"w") as InitClass:        
        fichier = open(pathToInitClass,"w")
        fichier.write("#l'initialisation de la classe : \n")
        fichier.write("def __init__(self")
        #écriture des arguments de la fonction __init__
        for row in attributes : 
            if isinstance(row[1],str) : 
                L = len(row[1])
                for iterate in range(L):
                    if row[1][iterate] == ",": #On remplace ici les , par des . pour lire les nombres en python 
                        row[1] = row[1].replace(",",".")
                if row[1].replace('.','').isdigit() :
                    fichier.write(","+row[0]+" = "+row[1])
                else : 
                    if row[1]=="None" or row[1]=="none" or row[1]=="True" or row[1]=="true" or row[1]=="False" or row[1]=="false": #On traite les cas particuliers None, True, False
                        if row[1]=="None" or row[1]=="none":
                            fichier.write(","+row[0]+" = None")
                        if row[1]=="True" or row[1]=="true":
                            fichier.write(","+row[0]+" = True")
                        if row[1]=="False" or row[1]=="false":
                            fichier.write(","+row[0]+" = False")                    
                    else :
                        fichier.write(","+row[0]+" = "+"'"+row[1]+"'")
            else :
                fichier.write(","+row[0]+" = "+str(row[1]))

        fichier.write(") : \n")
        #initialisation des arguments de la fonction
        for row in attributes :
            fichier.write("   {}\n".format("self."+"__"+row[0]+" = "+row[0]))
        fichier.write("\n")

        #getters and setters
        for row in attributes :
            #getters
            fichier.write("@property \n")
            fichier.write("def "+row[0]+"(self): \n")
            fichier.write("    return self.__"+row[0]+"\n")
            fichier.write("\n")
            #setters
            fichier.write("@"+row[0]+".setter \n")
            fichier.write("def "+row[0]+"(self,"+row[0]+"): \n")
            fichier.write("    self.__"+row[0]+" = "+row[0] + "\n")
            fichier.write("\n")


#creation de l'initialisation de la classe Fluid

pathToAttributes = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Fluid/Fluid_v_0.csv'
pathToInitClass = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid/InitFluid.py'

writeClass(pathToAttributes,pathToInitClass)

#creation de l'initialisation de la classe Dipole

pathToAttributes = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Dipole/Dipole_v_0.csv'
pathToInitClass = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole/InitDipole.py'

writeClass(pathToAttributes,pathToInitClass)

#creation de l'initialisation de la classe HeatExchanger

pathToAttributes = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Exchanger/Exchanger_v_0.ods'
pathToInitClass = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Exchanger/InitHeatExchanger.py'

writeClass(pathToAttributes,pathToInitClass)

#creation de l'initialisation de la classe PlateExchanger

pathToAttributes = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Exchanger/PlateExchanger_v_0.ods'
pathToInitClass = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Exchanger/InitPlateExchanger.py'

writeClass(pathToAttributes,pathToInitClass)


#creation de l'initialisation de la classe Flow

pathToAttributes = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Flow/Flow_v_0.ods'
pathToInitClass = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Flow/InitFlow.py'

writeClass(pathToAttributes,pathToInitClass)

#creation de l'initialisation de la classe Flow

pathToAttributes = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Dipole/IdealPump_v_0.ods'
pathToInitClass = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Dipole/InitIdealPump.py'

writeClass(pathToAttributes,pathToInitClass)


#creation de l'initialisation de la classe Flow

pathToAttributes = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Graphe/Graphe.ods'
pathToInitClass = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Graphe/InitGraphe.py'

writeClass(pathToAttributes,pathToInitClass)

#creation de l'initialisation de la classe Flow

pathToAttributes = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Graphe/Node.ods'
pathToInitClass = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Graphe/InitNode.py'

writeClass(pathToAttributes,pathToInitClass)

