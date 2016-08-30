import sys
try:
    file = open("clients.dat", "w")
except IOError,message:
    print >> sys.stderr,"Unable to open file"
    sys.exit(1)
print "Enter the account, name and balance"
print "Enter end-of-file to end input."
# k = raw_input("Enter your int")
# print "Given value for k is : ",k
while 1:
    try:
        accountLine = raw_input("? ")
        try:
            if int(accountLine) == 3:
                break
        except ValueError:
            print >> file, accountLine
            pass
    except EOFError:
        break

file.close()
print "file closed after writing"

file = open("clients.dat","r")
records = file.readlines()

print "\n"
print "Account".ljust(10),"Name".ljust(10),"Balance".ljust(10)

for r in records:
    fields = r.split()
    print fields[0].ljust(10),
    print fields[1].ljust(10),
    print fields[2].ljust(10)
file.close()