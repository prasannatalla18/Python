Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #arithmetic
>>> a=2
>>> b=4
>>> print(a+b)
6
>>> print(a-b)
-2
>>> print(a*b)
8
>>> print(a//b)
0
>>> print(a/b)
0.5
>>> print(a**b)
16
>>> print(a%b)
2
>>> #assignment
>>> a=3
>>> b=5
>>> print(a+=b)
SyntaxError: invalid syntax
>>> a+b
8
>>> a+=b
>>> a
8
>>> print(a)
8
>>> b+=a
>>> b
13
>>> a-=b
>>> a
-5
>>> a*=b
>>> a
-65
>>> a//=b
>>> a
-5
>>> a/=b
>>> a
-0.38461538461538464
>>> a**=b
a
-4.0303844668336445e-06
#comparision
a=4
b=9
a<b
True
b>a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a<=b
True
b>=a
True
a>=b
False
b<=a
False
#logical
a=3
b=6
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a!=b or a==b
True
a<=b or b<=a
True
not True
False
not False
True
a=4
type(a) is int
True
#identity
type(a) is not int
False
b=6.7
type(b) is float
True
type(b) is not float
False
a=4.3
type(a) is int
False
type(a) is not int
True
type(a) is float
True
a="prasanna"
type(a) is str
True
type(a) is float
False
type(a) is not string
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    type(a) is not string
NameError: name 'string' is not defined. Did you forget to import 'string'?
