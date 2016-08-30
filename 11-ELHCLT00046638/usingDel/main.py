from Employee import Employee

print "Number of empl before init %s",Employee.count

e1 = Employee("susan","Baker")
e2 = Employee("Robert", "Jones")
e3 = e1

print "Number of emp after init ", e1.count

del e1
del e2
del e3

print "Number of emp after del is ", Employee.count