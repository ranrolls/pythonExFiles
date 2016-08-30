Python 3.6.0a4 (v3.6.0a4:017cf260936b, Aug 16 2016, 00:45:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
t = 1,2,3,4
>>> t
(1, 2, 3, 4)
>>> t1 = (5,6,7)
>>> t1
(5, 6, 7)
>>> t1[1]
6
>>> t[1]
2
>>> len(t)
4
>>> len(t1)
3
>>> // tuple are immutable ( their content and size cannot be changed )
SyntaxError: invalid syntax
>>> // tuples can also contain lists and dictionaries in it
SyntaxError: invalid syntax
>>> myList = [1,2,3]
>>> myDict = {'ht':1,'ti':2,'nt':3}
>>> myTuple = (100,myList,myDict,300,'item')
>>> myTuple
(100, [1, 2, 3], {'ti': 2, 'ht': 1, 'nt': 3}, 300, 'item')
>>> len(myTuple)
5
>>> 
