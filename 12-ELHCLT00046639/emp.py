class Emp:    
    def __init__(self,first,last):
        if self.__class__ == Emp:
            raise NotImplementedError + "Cannot create obj of class Emp"
        self.firstName = first
        self.lastName = last
        
    def __str__(self):
        return "%s %s" %(self.firstName, self.lastName)
        
    def _checkPositive(self, value):
        if value < 0:
            print(value)
            raise ValueError + "Attrib value must be positive"
        else:
            return value
        
    def earnings(self):
       raise NotImplementedError + "Cannot call abstract method"    