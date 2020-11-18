import numpy as np
import matplotlib.pyplot as plt
class Resolve:
    #pour utiliser une telle méthode il faut s'assurer que l'on ait suffisament proche de la solution et que abs(g'(solution)+relaxation)<abs(1+relaxation)
    def fixePointResolution(g, X0, relaxation = 0, seuil = 0.0001, iterationMax = 100): #g est la fonction du point fixe g(x) = x
        iteration = 0
        Xn = X0
        Xn1 = X0+1
        while iteration < iterationMax and abs(Xn1 - Xn) > seuil :
            Xn = Xn1
            Xn1 = (g(Xn) + relaxation * Xn)/ (1 + relaxation)
            iteration += 1
        if iteration == iterationMax :
            raise ValueError("don't converge")
        else :
            return Xn1
    fixePointResolution = staticmethod(fixePointResolution)


class DataAnalysis :
    #la méthode interpolation permet de transformer un nuage de point en fonction par interpolation.
    def interpolation(X, Y, method = 'linear') :
        ind = np.lexsort((Y,X)) #Permet de récupérer les indices dans lequel rangé les listes X et Y  pour mettre l'axe X dans l'ordre croissant
        Xsorted = [X[i] for i in ind]
        Ysorted = [Y[i] for i in ind]
        def linearInterpollation(x):
            absN = Xsorted[0]
            i = 0
            if x < float(Xsorted[0]) or x > float(Xsorted[-1]):
                raise ValueError('x en dehors du domaine de définition')
            for absN1 in Xsorted[1:] :
                if x > float(absN) and x <= float(absN1) :
                    relativePosition = (x - absN) / (absN1 - absN)
                    return Ysorted[i] * (1 - relativePosition) + Ysorted[i+1] * relativePosition #interpollation linéaire
                absN = absN1
                i+=1
        if method == 'linear':
            return linearInterpollation
    
    interpolation = staticmethod(interpolation)
            
            

#test

def g(x):
    return (0.8*x)

zeroG = Resolve.fixePointResolution(g,0.9,-0.7)

X = [4, 1, 3, 5, 7, 2]
Y = [12, 20, 40, 80, 12, 17]

interpolationXY = DataAnalysis.interpolation(X,Y)
print(interpolationXY(3.5))

