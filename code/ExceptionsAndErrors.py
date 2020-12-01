import numpy as np

def typeErrorAtEntering( variableToEnter, Types = [float], Classes = [np.float64], message = None):
    """typeErrorAtEntering : It verifies if the variableToEnter is in one of the types mentionned
                            in the Types variable or one of a instance of the classes mentionned
                            in the Classses variable. If it's not verified, it raises a TypeError
                            exception.

    Args:
        variableToEnter (no type in particular): The variable to test.

        Types(list): The list Types includes the types that we want to test. 
        Example of test : type(varibaleToEnter) is type

        Classes(list): the list Classes includes the classes that we want to
        test if the variableToEnter is an instance of it.
        Example of test : isinstance(varibaleToEnter, classe)

        message : It's the message to raise if the exception is raised.

    Raises :
        TypeError : If Types or Classes or not a list.
        TypeError : If all of the types in Types and all of the classes in 
                    Classes don't match with variableToEnter.
        

    """

    if type(Types) is not list or type(Classes) is not list:
        raise TypeError("Types and Classes must be a list")

    typeVerification = True
    if len(Types) > 0 :
        for Type in Types:
            if type(variableToEnter) is not Type:
                typeVerification = False

    instanceVerification = True
    if len(Classes) > 0 :
        for Classe in Classes:
            if not(isinstance(variableToEnter,Classe)):
                typeVerification = False

    if not(typeVerification or instanceVerification):
        raise TypeError(message)
