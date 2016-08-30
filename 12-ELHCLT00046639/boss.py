from emp import Emp

class Boss(Emp):
    def __init__(self,first,last,salary):
        Emp.__init__(self,first,last)
        self.weeklySalary = self._checkPositive(float(salary))
        
    def earnings(self):
        return self.weeklySalary
    
    def __str__(self):
        return "%17s: %s"%("Boss ", Emp.__str__(self))
    