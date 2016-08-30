>>> l = [1,2,3,4,"five","six","seven","eight"]
>>> l[1]
2
>>> l[5]
'six'
>>> l[7]
'eight'
>>> l[8]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    l[8]
IndexError: list index out of range
>>> l[7]
'eight'
>>> len(l)
8
>>> l.append("new")
>>> l
[1, 2, 3, 4, 'five', 'six', 'seven', 'eight', 'new']
>>> l.remove(2)
>>> l
[1, 3, 4, 'five', 'six', 'seven', 'eight', 'new']
>>> l.pop()
'new'
>>> l
[1, 3, 4, 'five', 'six', 'seven', 'eight']
>>> l.pop(3)
'five'
>>> help(l)
Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> l
[1, 3, 4, 'six', 'seven', 'eight']
>>> l.reverse()
>>> l
['eight', 'seven', 'six', 4, 3, 1]
>>> l.reverse()
>>> l
[1, 3, 4, 'six', 'seven', 'eight']
>>> l.append(5,6,7,8)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    l.append(5,6,7,8)
TypeError: append() takes exactly one argument (4 given)
>>> l.append(5)
>>> l.append(6)
>>> l.append(7)
>>> l.append(8)
>>> l
[1, 3, 4, 'six', 'seven', 'eight', 5, 6, 7, 8]
>>> l.index('six',0,3)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    l.index('six',0,3)
ValueError: 'six' is not in list
>>> l.index('six',0,7)
3
>>> l.append(1)
>>> l.append(3)
>>> l
[1, 3, 4, 'six', 'seven', 'eight', 5, 6, 7, 8, 1, 3]
>>> l.index('3',0,11)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    l.index('3',0,11)
ValueError: '3' is not in list
>>> len(l)
12
>>> l.index(3,0,11)
1
>>> l.index(3.4.11)
SyntaxError: invalid syntax
>>> l.index(3,4,11)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    l.index(3,4,11)
ValueError: 3 is not in list
>>> l.index(1,3,12)
10
>>> dir(l)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> l.sort()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    l.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> l.sort()
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    l.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> l = [3,6,8,4,2,6,8,9,4,2,0,5]
>>> l.sort()
>>> l
[0, 2, 2, 3, 4, 4, 5, 6, 6, 8, 8, 9]
>>> l2 = l;
>>> l2
[0, 2, 2, 3, 4, 4, 5, 6, 6, 8, 8, 9]
>>> id(l2)
47606640
>>> id(l)
47606640
>>> l3 = copy(l2)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    l3 = copy(l2)
NameError: name 'copy' is not defined
>>> l3 = list(l2)
>>> l3
[0, 2, 2, 3, 4, 4, 5, 6, 6, 8, 8, 9]