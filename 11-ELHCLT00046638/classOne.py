class Time:
    def __init__(self):
        self.hour = 0   # 0 - 23
        self.min = 0    # 0 - 59
        self.sec = 0    # 0 - 59
    
    def printMilitary(self):    # self is always passed as obj self reference
        print "%.2d:%.2d:%.2d"%(self.hour,self.min,self.sec)