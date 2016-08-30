Python 3.6.0a4 (v3.6.0a4:017cf260936b, Aug 16 2016, 00:45:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('hey')
hey
>>> aL = []
>>> for n in range(1,4):
	aL += [n]

	
>>> aL
[1, 2, 3]
>>> for n in range(5,9):
	aL.append(n)

	
>>> aL
[1, 2, 3, 5, 6, 7, 8]
>>> aL[3]
5
>>> aL[2] = 100
>>> aL
[1, 2, 100, 5, 6, 7, 8]
>>> # tuples now =>
>>> t1 = 1,2,3,4,5
>>> t1
(1, 2, 3, 4, 5)
>>> t1[3]
4
>>> # tuple items cannot be re assigned
>>> t1[3]= 2
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t1[3]= 2
TypeError: 'tuple' object does not support item assignment
>>> t1
(1, 2, 3, 4, 5)
>>> # unpack items for string, list, tuple
>>> aS = "abc"
>>> aL = [1,2,3]
>>> aT = "a","A",3
>>> a,b,c = aS
>>> print(a,b,c)
a b c
>>> a,b,c = aL
>>> print(a,b,c)
1 2 3
>>> a,b,c = aT
>>> print(a,b,c)
a A 3
>>> aD = {}
>>> aD = {'a':0,'b':1,'c':2,'d':3}
>>> aD
{'c': 2, 'd': 3, 'a': 0, 'b': 1}
>>> aD['c']
2
>>> aD['e'] = 4
>>> aD
{'c': 2, 'd': 3, 'e': 4, 'a': 0, 'b': 1}
>>> aD['e'] = 5
>>> aD
{'c': 2, 'd': 3, 'e': 5, 'a': 0, 'b': 1}
>>> del aD['e']
>>> aD
{'c': 2, 'd': 3, 'a': 0, 'b': 1}
>>> # we have different methods available for list and dictionaries
>>> aL.sort()
>>> aL
[1, 2, 3]
>>> bL = range(0,99,3)
>>> bL
range(0, 99, 3)
>>> aL = range(0,88,3)
>>> aL
range(0, 88, 3)
>>> aL = [1,2,4,5,65,6,6]
>>> sK = int(input('enter search index key'))
enter search index key2
>>> aL.index(sK)
1
>>> aL
[1, 2, 4, 5, 65, 6, 6]
>>> # INDEX  is used to index for given value
>>> 
