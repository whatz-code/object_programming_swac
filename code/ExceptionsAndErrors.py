def typeErrorAtEntering(classAttribute, variableToEnter, Type, message = None):
    if type(variableToEnter) is not Type:
        raise TypeError(message)
