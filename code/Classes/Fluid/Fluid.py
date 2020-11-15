from CSVtoArray import extraction

#ce chemmin permet d'accéder à la description des attributs de la classe à créer.
path = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Fluid/Fluid_v_0.csv'
fluidAttributes = extraction(path) #matrice (première colonne les attributs, seconde colonne leur valeur par défaut.)
fluid = 


class Fluid():
    def __init__(self, ): 
        for row in fluidAttributes:
            attribute = row[0]
            default = row[1] 
            self.attribute = default

        