#importation du module numpy qui permet de travailler avec des arrays
#importation du module panda qui permet de lire des fichiers csv
import numpy as np  
import pandas as pd
import os.path as os


def extraction(path) :
    if path[-3:] == 'csv':
        tableau = pd.read_csv(path)
    if path[-4:] == 'xlsx' or path[-5:] == 'xlsxm' or path[-3:] == 'ods' :
        tableau = pd.read_excel(path)
    matrice = tableau.to_numpy()
    return matrice





#test


path = '/home/raphael/Documents/Stage-application/Synthese-objet/Python/InformationsClasses/AttributsClasses/Exchanger/Exchanger_v_0.ods'
print(extraction(path))