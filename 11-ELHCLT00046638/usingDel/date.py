class Date:

    daysPerMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        
    def display(self):
        return "%d - %d - %d" % (self.day,self.mon,self.yr)
        
    def checkDay(self,testDay):
        if 0 < testDay <= Date.daysPerMonth[self.mon]:
            return testDay
        elif self.mon == 2 and testDay == 29:
            return testDay
        else:
            raise ValueError," invalid day %d for mon: %d"%(testDay, self.mon)

    def __init__(self,mon,day,yr):
        if 0 < mon <= 12:                  #validate mon
            self.mon = mon
        else:
            raise ValueError,"Invalid value for mon: %d" %mon
        if yr >= 0:                         #validate yr
            self.yr = yr
        else:
            raise ValueError,"Invalid value yr %d"%yr
        
        self.day = self.checkDay(day)
        #validate day
        
        print "Date: ", self.display()
        
    def __del__(self):
        print "date obj about to destroyed : ", self.display()
