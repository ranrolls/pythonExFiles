from emp import Emp

class HourlyWorker(Emp):
    
    def __init__(self,first,last,wage,hours):
        Emp.__init__(self,first,last)
        self.wage = self._checkPositive(float(wage))
        self.hours = self._checkPositive(float(hours))
        
    def earnings(self):
        if self.hours <= 40:
            return self.wage + self.hours
        else:
            return 40 * self.wage + (self.hours - 40) * self.wage * 1.5
            
    def __str__(self):
        return "%17s: %s"%("Hourly Worker", Emp.__str__(self))
    