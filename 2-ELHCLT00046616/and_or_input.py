Python 3.6.0a4 (v3.6.0a4:017cf260936b, Aug 16 2016, 00:45:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #comment
>>> ^z
SyntaxError: invalid syntax
>>> ^Z
SyntaxError: invalid syntax
>>> # use blank between funcs and space between operators
>>> print "welcom",
SyntaxError: Missing parentheses in call to 'print'
>>> print "welcom", print " to python"
SyntaxError: Missing parentheses in call to 'print'
>>> print ("welcom"),
welcom
(None,)
>>> print ("welcome "),print("to python")
welcome 
to python
(None, None)
>>> print("wel"), print("k")
wel
k
(None, None)
>>> # \n \t \r \n \a \\ \" \'
>>> print("welcome \n to \n \r python")
welcome 
 to 
  python
>>> # raw_input used to take input from user
>>> i1 = raw_input("Enter:\n") #read string
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    i1 = raw_input("Enter:\n") #read string
NameError: name 'raw_input' is not defined
>>> int1 = raw_input("enter ")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int1 = raw_input("enter ")
NameError: name 'raw_input' is not defined
>>> print """this string has "double quotes" and 'single quotes'.
You can even do multiple lines."""
SyntaxError: Missing parentheses in call to 'print'
>>> print("""this string has "double quotes" and 'single quotes'.
You can even do multiple line.""")
this string has "double quotes" and 'single quotes'.
You can even do multiple line.
>>> print ('''this string "double" and 'single' quotes.''')
this string "double" and 'single' quotes.
>>> iv = 2345
>>> print("integer",iv)
integer 2345
>>> print ('decimal integer %d'%iv)
decimal integer 2345
>>> print('hex int %x\n'%iv)
hex int 929

>>> fv = 1234.1234
>>> print('float',fv)
float 1234.1234
>>> print('default %f'%fv)
default 1234.123400
>>> print ('default exponential %e\n'%fv)
default exponential 1.234123e+03

>>> marks = 50
>>> if marks < 0 or marks > 100:
	print('in')
elif marks == 2
SyntaxError: invalid syntax
>>> # or and
>>> v1 = 3
>>> if v1 & v1 == 3:
	print(v1)

	
3
>>> if v1 | v1 != 4:
	print(v1)

	
3
>>> #common keywords in python
>>> # and assert break class elif continue def del while finally else except exec if print for from global raise lambda import in is return not or pass try
>>> try: input = raw_input
except NameError: pass
print("Hi " + input("Say something: "))
SyntaxError: invalid syntax
>>> print("hi " + input("say some "))
say some e
hi e
>>> # raw_input is changed to input in python 2 and 3
>>> int1 = input("first int:\n")
first int:
4
>>> int1 = int(int1)
>>> int1
4
>>> # string value show in black color and int value shows in blue color
>>> # python language update change from
>>> # string methods added, regular exp, garbage collection, generators, unicode, multiprocessing
>>> # in version 3, removed backward compatible, change in commands such as print, reduce, unicode, annotation, integer division
>>> 
