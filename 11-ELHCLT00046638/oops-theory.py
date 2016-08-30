# constructor method __init__
# obj self reference by self
# obj instance obj1 = MyClass()

# some other important attributes for class are:
__bases__ A tuple that contains base classes from which the class directly inherits. if the class does not inherit from other classes, the tuple is empty.

__dict__ A dictionary that corresponds to the class's namespace. Each key-value pair represents an identifier and its value in the namespace.

__doc__ A class's docstring. If the class does not specify a docstring, the value is None

__module__ A string that contains the class's name

__class__ A reference to the class from which the object was instantiated

---------------------------------------------

Defining method __del__ for class will help in executing a procedure when obj is destroyed or dereferenced from class. This method helps in perform termination before python reclaims object memory typically used to close network or database connections

---------------------------------------
