import sys
import logging
# logger.debug("The product %s is about to be added to the database.", product.id)   
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

def shouldDisplay(accountType, balance):
    if accountType == 2 and balance < 0:
        return 1
    elif accountType == 3 and balance > 0:
        return 1
    elif accountType == 1 and balance == 0:
        return 1
    elif accountType == 0:
        return 1
    else:
        return 0

def outputLine(account, name, balance):
    print account.ljust(10), name.ljust(10), balance.ljust(10)

# file data entry starts here
def enterData():
    try:
        file = open("clients.dat", "w")
    except IOError,message:
        print >> sys.stderr,"Unable to open file"
        sys.exit(1)
    while 1:
        try:
            accountLine = raw_input("")
            try:
                if int(accountLine) == 3:       # trigger loop break
                    print "break accountLine input"
                    break
            except ValueError:
                print >> file, accountLine
                pass
        except EOFError:
            break
    file.close()
    print "file closed after writing"

#   file read and data formatting starts here
    
def readData():
    try:
        file = open("clients.dat","r")
    except IOError:
        print >> sys.stderr,"File could not be opened"
        sys.exit(1)
    print "\n Enter request:"
    print "0 - List all accounts"
    print "1 - List accounts with zero balances"
    print "2 - List accounts with credit balances"
    print "3 - List accounts with debit balances"
    print "4 - End of run"
    
    accountLine = raw_input("")
    accountLine = int(accountLine)
    
    records = file.readlines()
    #     print "\n"
    print "Account".ljust(10),"Name".ljust(10),"Balance".ljust(10)
    for r in records:
        account,name,balance = r.split()
        balance = float(balance)
        if shouldDisplay(accountLine, balance) == 1:
            outputLine(account,name,str(balance))
    file.seek(0,0)
    print "\nEnd of run"
    file.close()
    
def readMoreData():
    opt = raw_input("read more data opt: ")
    if int(opt) == 1:
        readData()
    
enterData()
readData()
readMoreData()