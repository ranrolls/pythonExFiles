Python 3.6.0a4 (v3.6.0a4:017cf260936b, Aug 16 2016, 00:45:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # component is container for funcs, classes, modules and packages
>>> # modules user to perform common tasks and eliminate redudancy
>>> def sq(y):
	print(y*y)

	
>>> for x in range(1,11):
	sq(x)

	
1
4
9
16
25
36
49
64
81
100
>>> # modules namespace __name__ ( name of module )
>>> # to alter global variable we should get it again in our func as
>>> #     global var_name
>>> a = 1
>>> def a():
	a = 2
	print(a)

	
>>> def b():
	global a
	a = 3
	print(a)

	
>>> a()
2
>>> b()
3
>>> a
3
>>> # recursive funcs
>>> def fibo(n):
	if n < 0:
		print(n)
	if n == 0 or n == 1:
		return n
	else:
		return fibo(n-1) + fibo(n-2)

	
>>> n = 20
>>> print(fibo(n))
6765
>>> # predefined argument override
>>> def boxVol(l = 1, w = 1, h = 1):
	return l*w*h
print(boxVol())
SyntaxError: invalid syntax
>>> print(boxVol(2))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(boxVol(2))
NameError: name 'boxVol' is not defined
>>> boxVol(2,3,4)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    boxVol(2,3,4)
NameError: name 'boxVol' is not defined
>>> def boxVol(l = 1, w = 1, h = 1):
	return l * w * h

>>> print(boxVol(3,3,3))
27
>>> print(boxVol())
1
>>> print(boxVol(2))
2
>>> 
