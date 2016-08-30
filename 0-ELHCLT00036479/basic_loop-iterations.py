Python 3.6.0a4 (v3.6.0a4:017cf260936b, Aug 16 2016, 00:45:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
a=2
>>> if a<10
SyntaxError: invalid syntax
>>> if a<10:
	print('a is less')

	
a is less
>>> if a<10:
	print('a less')
	elif a>10:
		
SyntaxError: invalid syntax
>>> if a<10:
	print(' a less')

	
 a less
>>> if a<10:
	print('less')
elif a > 10:
	print('more')
else:
	print('equal')

	
less
>>> for i in range(10):
	if i<5:
		pass
	if i == 5
	
SyntaxError: invalid syntax
>>> for i in range(10):
	if i<5:
		pass
	elif i==6:
		break

	
>>> 
>>> 
