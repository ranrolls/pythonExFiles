from classOne import Time
t1 = Time()
print "t1.hour: ",t1.hour," t1.min: ",t1.min,"  t1.sec: ",t1.sec
t1.printMilitary()
t1.hour = 25
t1.printMilitary()

print Time.__bases__
print Time.__dict__
print Time.__doc__
print Time.__name__
print t1.__class__
