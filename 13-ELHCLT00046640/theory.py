__str__ allows obj to be output with print statement
__setattr__ called by python every time a program makes a assignment to a obj attrib through the dot operator
__getattr__ called by python if an attrib is accessed as a right-hand value by the dot operator. Limitation for this method is that it executes only if attrib is not found in the object's __dict__
__add__ overloads the + operator

Build in methods are available to overload every unary operators, binary operators and build-in funcs

Common operators that can be overloaded
+ - * ** / // % << >> & | ^ ~ < > <= >= == != += -= *= **= /= //= %= <<= >>= &= ^= |= [] () . `` in

__neg__ __pos__ __invert__ are methods for unary operator

Parenthesis may be used to force order of evaluation
Overloading mathematical operator automatically overloads the corresponding augmented assignment statement

overloading the + operator causes += to be overloaded as well

Other method for binary operator/statements

+   __add__ , __radd__
-   __sub__ , __rsub__
*   __mul__ , __rmul__
/   __div__ , __rdiv__
// __floordiv__ , __rfloordiv__
%   __mod__ , __rmod__
**  __pow__ , __rpow__
<<  __lshift__ , __rlshift__
>>  __rshift__ , __rrshift__
&   __and__ , __rand__
^   __xor__ , __rxor__
|   __or__ , __ror__
+=  __iadd__
-=  __isub__
*=  __imul__
/=              and so on

methods for overloading build-in funcs are also available

__abs__ abs(x)
__len__ len(x)
and so on