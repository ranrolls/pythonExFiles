Python 3.6.0a4 (v3.6.0a4:017cf260936b, Aug 16 2016, 00:45:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("hell")
hell
>>> m = 1
>>> isinstance(m,int)
True
>>> type(m)
<class 'int'>
>>> <class 'int'>
SyntaxError: invalid syntax
>>> m = 5
>>> n = `1
SyntaxError: invalid syntax
>>> n = 12
>>> m + n
17
>>> n / m
2.4
>>> n/m
2.4
>>> n = 12.0
>>> n/m
2.4
>>> n//m
2.0
>>> a = k
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a = k
NameError: name 'k' is not defined
>>> a = 2
>>> b = "2"
>>> a == b
False
>>> a === b
SyntaxError: invalid syntax
>>> b = 2
>>> a === b
SyntaxError: invalid syntax