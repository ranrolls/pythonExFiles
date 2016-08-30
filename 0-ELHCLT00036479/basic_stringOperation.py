>>> a = 'hello '
>>> b='world'
>>> a+b
'hello world'
>>> a+' my '+b
'hello  my world'
>>> print 'wel'
SyntaxError: Missing parentheses in call to 'print'
>>> print 'wel'
SyntaxError: Missing parentheses in call to 'print'
>>> print "wel"
SyntaxError: Missing parentheses in call to 'print'
>>> a = 'hello '
>>> 
>>> a
'hello '
>>> a = 2
>>> b = '2'
>>> str(a)==b
True
>>> a*3
6
>>> b*3
'222'
>>> b
'2'
>>> a[:]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a[:]
TypeError: 'int' object is not subscriptable
>>> b[:]
'2'
>>> m
5
>>> n
12.0
>>> a='the quick brown fox jumps over a little lazy dog.'
>>> a[::-1]
'.god yzal elttil a revo spmuj xof nworb kciuq eht'
>>> a[:]
'the quick brown fox jumps over a little lazy dog.'
>>> a[3:9:2]
' uc'
>>> a[3:19:-2]
''
>>> a[2:22:1]
'e quick brown fox ju'
>>> a[2:33:2]
'eqikbonfxjmsoe  '
>>> a.find('fox')
16
>>> a.rfind('r')
29
>>> a.lfind('r')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.lfind('r')
AttributeError: 'str' object has no attribute 'lfind'
>>> a.count('r')
2
>>> a.count('o')
4
>>> a.strip()
'the quick brown fox jumps over a little lazy dog.'
>>> a[2:33:2].strip()
'eqikbonfxjmsoe'
>>> fox in a
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    fox in a
NameError: name 'fox' is not defined
>>> 'fox' in a
True
>>> 'foxi' in a
False
>>> 'foxi' not in a
True
>>> true
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> True
True