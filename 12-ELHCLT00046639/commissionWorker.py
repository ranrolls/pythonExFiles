from emp import Emp

class CommissionWorker(Emp):
    
    def __init__(self,first,last,salary,commission,quantity):
        Emp.__init__(self,first,last)
        self.salary = self._checkPositive(float(salary))
        self.commission = self._checkPositive(float(commission))
        self.quantity = self._checkPositive(quantity)
        
    def earnings(self):
        return self.salary + self.commission * self.quantity
    
    def __str__(self):
        return "%17s: %s"%("Commission Worker ", Emp.__str__(self))
    