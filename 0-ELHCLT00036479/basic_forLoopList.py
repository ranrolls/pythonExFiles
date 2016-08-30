>>> squares = []
>>> for x in range(10)
SyntaxError: invalid syntax
>>> for x in range(10):
	squares.append(x**2)

	
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> for b in squares:
	print("Item in list %d" %squares)

	
Traceback (most recent call last):
  File "<pyshell#120>", line 2, in <module>
    print("Item in list %d" %squares)
TypeError: %d format: a number is required, not list
>>> for b in squares
SyntaxError: invalid syntax
>>> for b in squares
SyntaxError: invalid syntax
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> for b in squares
SyntaxError: invalid syntax
>>> for b in squares:
	print("item in list %d" %b)

	
item in list 0
item in list 1
item in list 4
item in list 9
item in list 16
item in list 25
item in list 36
item in list 49
item in list 64
item in list 81
>>> ----------------------
SyntaxError: invalid syntax
>>> 