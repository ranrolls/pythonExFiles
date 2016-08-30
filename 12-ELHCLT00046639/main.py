from emp import Emp
from boss import Boss
from commissionWorker import CommissionWorker
from pieceWorker import PieceWorker
from hourlyWorker import HourlyWorker

employees = [Boss("John","Smith",800.00),
             CommissionWorker("Sue","Jones",200.0,3.0,150),
             PieceWorker("Bob","Lewis",2.5,200),
             HourlyWorker("Karen","Price",13.75,40)]

for emp in employees:
    #print ("%s earned $"%(emp)), print ("%.2f" %emp.earnings())
    print ("%s earned $%.2f"%(emp, emp.earnings()))