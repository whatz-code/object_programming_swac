import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy.linalg import norm
from scipy.optimize import curve_fit
class Resolve:
    #pour utiliser une telle méthode il faut s'assurer que l'on ait suffisament proche de la solution et que abs(g'(solution)+relaxation)<abs(1+relaxation)
    def fixePointResolution(g, X0, relaxation = 0, seuil = 0.0000001, iterationMax = 100): #g est la fonction du point fixe g(x) = x
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

    def functionToSecante(xmin, xmax, f):
        if xmin >= xman:
            raise ValueError("xmax > xmin")
        a = (f(xmax) - f(xmin)) / (xmax - xmin)
        b = f(xmin) - (f(xmax) - f(xmin)) / (xmax - xmin) * xmin
        return a, b
    functionToSecante = staticmethod(functionToSecante)
    def multiDimensionnalNewtonResolution(F,X0,seuil = 0.0001, iterationMax = 100):
        dimension = len(X0)
        iteration = 0
        Xn = X0
        deltaXn = np.zeros((dimension,1))
        deltaXn[0] = 1
        Fn = F(Xn)
        Fn = np.array(Fn)
        while (norm(deltaXn) > seuil or norm(Fn) > seuil) and iteration <= iterationMax :
            Fn = F(Xn)
            Fn = np.array(Fn)
            jacobian = Resolve.estimationJacobian(F,Xn,dx = 0.00000000001)
            invJacobian = np.linalg.inv(jacobian)
            Xn1 = Xn - np.dot(invJacobian, Fn)
            deltaXn = Xn1 - Xn
            # print('Xn')
            # print(norm(deltaXn))
            # print('Fn')
            # print(norm(Fn))
            iteration +=1
            Xn = Xn1
            print(Fn)
        if iteration == iterationMax:
            raise StopIteration("the Boryden resolution doesn't converge")
        
        return Xn


    def multiDimensionnalBroydenResolution(F,X0,B0 = None, seuil = 0.0001, iterationMax = 100):
        dimensions = X0.shape
        dimension = dimensions[0]
        # if B0 == None:
        #     B0 =  np.eye(dimension)
        # B0[0][0] = 4
        # Bn = B0
        print(X0)
        Bn = Resolve.estimationJacobian(F,X0)
        iteration = 0
        Xn = X0
        deltaXn = np.zeros((dimension,1))
        deltaXn[0] = 1
        Fn = F(Xn)
        Fn = np.array(Fn)
    
        while (norm(deltaXn) > seuil or norm(Fn) > seuil) and iteration <= iterationMax :
            Fn = F(Xn)
            Fn = np.array(Fn)
            deltaXn = np.linalg.solve(Bn,- Fn)
            Xn = np.array(Xn) + deltaXn
            Xn = Xn.astype(type('float', (float,), {}))
            # print('Xn')
            # print(norm(deltaXn))
            # print('Fn')
            # print(norm(Fn))
            Fn1 = F(Xn)
            Fn1 = np.array(Fn1)
            deltaFn = Fn1 - Fn
            Bn = Bn + (deltaFn - Bn.dot(deltaXn)).dot(np.transpose(deltaXn)) / norm(deltaXn) ** 2
            iteration +=1
        if iteration == iterationMax:
            raise StopIteration("the Boryden resolution doesn't converge")
        
        return Xn

    def estimationJacobian(F,X0,dx = 0.000001):
        dimension = len(X0)
        Jacobian = np.zeros((dimension,dimension))
        X0 = np.array(X0)
        X0 = X0.reshape((dimension,1))
        for j in range(dimension):
            Dxj = np.zeros((dimension,1))
            Dxj[j] = dx
            DFDxj = (np.array(F(X0 + Dxj)) -np.array(F(X0 - Dxj))) / (2 * dx)
            for i in range(dimension):
                DfiDxj = DFDxj[i]
                Jacobian[i][j] = DfiDxj
        return Jacobian 







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

    def curveFit(parameters0, boundsParameters, g, Xdata, Ydata, bounds): #dans le cas des échangeurs, Xdata correspond aux débits d'entrées et aux températures d'entrées et Ydata correspond aux valeurs que l'on souhaite atteindre
        return sc.curve_fit(g, Xdata, Ydata, parameters0, boundsParameters)
            
            

#test

