from date import Date

class EmployeeWithDate:

    def __init__(self,first,last,bMon,bDay,bYr,hMon,hDay,hYr):
        self.birthDate = Date(bMon, bDay, bYr)
        self.hireDate = Date(hMon, hDay, hYr)
        self.lastName = last
        self.firstName = first
        print "Employee constructor for %s, %s" %(self.lastName, self.firstName)
        
    def __del__(self):
        print "Employee destruct for %s, %s" %(self.lastName,self.firstName)
    
    def display(self):
        return self.firstName, self.lastName, " /n Hired: ",self.hireDate.display(), " /n Birth Date: ", self.birthDate.display()