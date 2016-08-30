class Employee:
    
    count = 0           # unique variable used as cache for class
    
    def __init__(self, first,last):
        self.firstName = first
        self.lastName = last
        Employee.count += 1             # increment cache variable
        print "Employee constructor for %s, %s" %(self.lastName, self.firstName)
        
    def __del__(self):
        Employee.count -= 1
        print "Employee destruct for %s, %s" %(self.lastName,self.firstName)
        