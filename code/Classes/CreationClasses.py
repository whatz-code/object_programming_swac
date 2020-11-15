
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

            #On remplace ici les , par des . pour lire les nombres en python 
            L = len(row[1])
            for iterate in range(L):
                if row[1][iterate] == ",":
                    row[1] = row[1].replace(",",".")
            fichier.write(","+row[0]+" = "+row[1])

        fichier.write(") : \n")
        #initialisation des arguments de la fonction
        for row in attributes :
            fichier.write("    {}\n".format("self."+"__"+row[0]+" = "+row[0]))

#test

pathToAttributes = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Fluid/Fluid_v_0.csv'
pathToInitClass = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/code/Classes/Fluid/InitFluid.py'

writeClass(pathToAttributes,pathToInitClass)





