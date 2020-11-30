import numpy as np
def typeErrorAtEntering( variableToEnter, Types = [float], Classes = [np.float64], message = None):
    if type(Types) is not list or type(Classes) is not list:
        raise TypeError("Types and Classes must be a list")
    typeVerification = True
    for Type in Types:
        if type(variableToEnter) is not Type:
            typeVerification = False
    instanceVerification = True
    if Classes[0] != None:
        for Classe in Classes:
            if not(isinstance(variableToEnter,Classe)):
                typeVerification = False
    if not(typeVerification or instanceVerification):
        raise TypeError(message)
