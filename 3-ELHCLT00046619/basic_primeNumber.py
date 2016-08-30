Python 3.6.0a4 (v3.6.0a4:017cf260936b, Aug 16 2016, 00:45:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #sample program for nested loops finding prime number
>>> for n in range(2,10):
	for i in range(2,n):
		if n % i == 0:
			print("%s equals %x\n"%(n,i))
			break
else:
	print (n, 'is a prime nuumber')

	
4 equals 2

6 equals 2

8 equals 2

9 equals 3

9 is a prime nuumber
>>> 
