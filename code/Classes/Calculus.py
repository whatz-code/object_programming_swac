class Resolve:
    #pour utiliser une telle méthode il faut s'assurer que l'on ait suffisament proche de la solution et que abs(g'(solution)+relaxation)<abs(1+relaxation)
    def fixePointResolution(g, X0, relaxation = 0, seuil = 0.0001, iterationMax = 100): #g est la fonction du point fixe g(x) = x
        iteration = 0
        Xn = X0
        Xn1 = X0+1
        while iteration < iterationMax and abs(Xn1 - Xn) > seuil :
            print(Xn)
            Xn = Xn1
            Xn1 = (g(Xn) + relaxation * Xn)/ (1 + relaxation)
            iteration += 1
        if iteration == iterationMax :
            raise ValueError("don't converge")
        else :
            return Xn1
    fixePointResolution = staticmethod(fixePointResolution)


#test

def g(x):
    return (0.8*x)

zeroG = Resolve.fixePointResolution(g,0.9,-0.7)
print(zeroG)