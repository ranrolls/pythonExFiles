from restrictTime import Time

t1 = Time()
#t1 = Time(3)       if default vals provided in class
#t1 = Time(3,5)     if default vals provided in class
#t1 = Time(3,5,55)  if default vals provided in class


t1.printMilitary()
t1.printStandard()

t1.setTime(13,24,4)
t1.printMilitary()

t1.setHour(4)
t1.setMin(3)
t1.setSec(34)

t1.printMilitary()
t1.printStandard()