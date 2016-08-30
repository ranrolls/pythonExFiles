Python 3.6.0a4 (v3.6.0a4:017cf260936b, Aug 16 2016, 00:45:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
# list of rows means multi dimension list or tuple
>>> aL = [[1,2],[3,4]]
>>> aT = ( (1,2),(3,4),(5,6))
>>> aL
[[1, 2], [3, 4]]
>>> for r in aL:
	for v in r:
		print(v)

		
1
2
3
4
>>> for r in aT:
	for k,v in r:
		print(k,v)

		
Traceback (most recent call last):
  File "<pyshell#11>", line 2, in <module>
    for k,v in r:
TypeError: 'int' object is not iterable
>>> for r in aT:
	for k,v in r.items():
		print(k,v)

		
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    for k,v in r.items():
AttributeError: 'tuple' object has no attribute 'items'
>>> for r in aL:
	for k,v in r.items():
		print(k,v)

		
Traceback (most recent call last):
  File "<pyshell#19>", line 2, in <module>
    for k,v in r.items():
AttributeError: 'list' object has no attribute 'items'
>>> 
