class Time: # private class
    
    
    #def __init__(self,hour=0,min=0,sec=0):  to init vars with default values
    def __init__(self):
        self._hour = 0   # 0 - 23   private data member
        self._min = 0    # 0 - 59   private data member
        self._sec = 0    # 0 - 59   private data member
    
    def setHour(self, hour):
        if 0 <= hour < 24:
            self._hour = hour
        else:
            raise ValueError, ' Invalid hour value: %d '%hour
        
    def setMin(self, min):
        if 0 <= min < 60:
            self._min = min
        else:
            raise ValueError, ' Invalid min value: %d '%min
        
    def setSec(self, sec):
        if 0 <= sec < 60:
            self._sec = sec
        else:
            raise ValueError, ' Invalid sec value: %d '%sec
        
    def setTime(self,hour,min,sec):
        self.setHour(hour)
        self.setMin(min)
        self.setSec(sec)
        
    def getHour(self):
        return self._hour
    
    def getMin(self):
        return self._min
    
    def getSec(self):
        return self._sec
    
    def printMilitary(self):    # self is always passed as obj self reference
        print "%.2d:%.2d:%.2d"%(self._hour,self._min,self._sec)
        
    def printStandard(self):
        standardTime = ""
        if self._hour == 0 or self._hour == 12:
            standardTime += "12:"
        else:
            standardTime += "%d:" %(self._hour % 12)
        standardTime += "%.2d:%.2d" % (self._min, self._sec)
        if self._hour < 12:
            standardTime += " AM"
        else:
            standardTime += " PM"
        print standardTime 