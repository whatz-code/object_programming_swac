#importation du module numpy qui permet de travailler avec des arrays
#importation du module panda qui permet de lire des fichiers csv
import numpy as np  
import pandas as pd
import os.path as os


def extraction(path) :
    tableau = pd.read_csv(path)
    matrice = tableau.to_numpy()
    return matrice








path = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Fluid/Fluid_v_0.csv'
