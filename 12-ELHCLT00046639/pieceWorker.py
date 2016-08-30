from emp import Emp

class PieceWorker(Emp):
    
    def __init__(self,first,last,wage,quantity):
        Emp.__init__(self,first,last)
        self.wagePerPiece = self._checkPositive(float(wage))
        self.quantity = self._checkPositive(quantity)
        
    def earnings(self):
        return self.quantity * self.wagePerPiece
    
    def __str__(self):
        return "%17s: %s"%("Piece Worker ", Emp.__str__(self))        
    