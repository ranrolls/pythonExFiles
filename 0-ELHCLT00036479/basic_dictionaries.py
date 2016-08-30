Python 3.6.0a4 (v3.6.0a4:017cf260936b, Aug 16 2016, 00:45:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
a='a'
>>> a
'a'
>>> d = {'http':88, 'https':443, 'ftp':21}
>>> d['telnet']=23
>>> d['ftp']
21
>>> d.keys()
dict_keys(['http', 'https', 'telnet', 'ftp'])
>>> d.values()
dict_values([88, 443, 23, 21])
>>> 88 in d.values()
True
>>> 91 not in d.values()
True
>>> d.items()
dict_items([('http', 88), ('https', 443), ('telnet', 23), ('ftp', 21)])
>>> for item in d:
	print item
	
SyntaxError: Missing parentheses in call to 'print'
>>> for item in d:
	print (item)

	
http
https
telnet
ftp
>>> for item in d:
	print (d[str(item)])

	
88
443
23
21
>>> for k,v in d.item():
	print ('My item key is %s' %str(k))
	print('My item value is %s' %str(v))

	
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for k,v in d.item():
AttributeError: 'dict' object has no attribute 'item'
>>> for k,v in d.items():
	print('My item key is %s' %str(k))
	print('My item value is %s' %str(v))

	
My item key is http
My item value is 88
My item key is https
My item value is 443
My item key is telnet
My item value is 23
My item key is ftp
My item value is 21
>>> 
