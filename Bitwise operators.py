Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #bitwise
>>> a=2
>>> b=4
>>> a&b
0
>>> a=5
>>> b=7
>>> a&b
5
>>> bin(2)
'0b10'
>>> bin(4)
'0b100'
>>> bin(5)
'0b101'
>>> bin(7)
'0b111'
>>> a=3
>>> b=6
>>> a|b
7
>>> a=4
>>> a=8
>>> a|b
14
>>> a=4
>>> b=8
>>> a|b
12
>>> #not
>>> a=5
>>> -(a+1)
-6
>>> ~a
-6
>>> a=9
>>> ~a
-10
>>> b=-9
>>> ~b
8
>>> c=-12
>>> !c
SyntaxError: invalid syntax
>>> ~c
11
a=3
b=5
a^b
6
a=7
b=9
a^b
14
#leftshift
a=3
a<<2
12
b=4
b<<3
32
#right shift
a=5
a>>2
1
a=6
a>>3
0
