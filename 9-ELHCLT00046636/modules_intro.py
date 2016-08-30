Python 3.6.0a4 (v3.6.0a4:017cf260936b, Aug 16 2016, 00:45:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # fileName is module name with suffix .py
>>> # get module name by using __name__ attribute within module
>>> # module can be imported using "import" or "from" statement
>>> # find standard modules at c:\Python\lib
>>> # some standard modules are os, sys, time, random
>>> import os
>>> os.getcwd()
'D:\\Users\\ranjan.sh\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.tmpfile()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    os.tmpfile()
AttributeError: module 'os' has no attribute 'tmpfile'
>>> os.getuid()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    os.getuid()
AttributeError: module 'os' has no attribute 'getuid'
>>> import sys
>>> sys.path
['', 'D:\\Users\\ranjan.sh\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'D:\\Users\\ranjan.sh\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'D:\\Users\\ranjan.sh\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'D:\\Users\\ranjan.sh\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'D:\\Users\\ranjan.sh\\AppData\\Local\\Programs\\Python\\Python36-32', 'D:\\Users\\ranjan.sh\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages']
>>> 
