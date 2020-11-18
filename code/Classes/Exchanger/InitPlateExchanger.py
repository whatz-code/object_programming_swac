#l'initialisation de la classe : 
def __init__(self,length = 2.5,width = 1.0,plateNumber = 385.0,passeNumber = 1.0,plateThickness = 0.5,plateGap = 3.0,angle = 45.0,streakWaveLength = None) : 
   self.__length = length
   self.__width = width
   self.__plateNumber = plateNumber
   self.__passeNumber = passeNumber
   self.__plateThickness = plateThickness
   self.__plateGap = plateGap
   self.__angle = angle
   self.__streakWaveLength = streakWaveLength

@property 
def length(self): 
    return self.__length

@length.setter 
def length(self,length): 
    self.__length = length

@property 
def width(self): 
    return self.__width

@width.setter 
def width(self,width): 
    self.__width = width

@property 
def plateNumber(self): 
    return self.__plateNumber

@plateNumber.setter 
def plateNumber(self,plateNumber): 
    self.__plateNumber = plateNumber

@property 
def passeNumber(self): 
    return self.__passeNumber

@passeNumber.setter 
def passeNumber(self,passeNumber): 
    self.__passeNumber = passeNumber

@property 
def plateThickness(self): 
    return self.__plateThickness

@plateThickness.setter 
def plateThickness(self,plateThickness): 
    self.__plateThickness = plateThickness

@property 
def plateGap(self): 
    return self.__plateGap

@plateGap.setter 
def plateGap(self,plateGap): 
    self.__plateGap = plateGap

@property 
def angle(self): 
    return self.__angle

@angle.setter 
def angle(self,angle): 
    self.__angle = angle

@property 
def streakWaveLength(self): 
    return self.__streakWaveLength

@streakWaveLength.setter 
def streakWaveLength(self,streakWaveLength): 
    self.__streakWaveLength = streakWaveLength

