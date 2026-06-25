Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(3+3)
6
a=10
print(a)
10
b=2
c=4
print(b+c)
6
x=2
print(X)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
print(x)
2
z=40
print(z)
40
3=50
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a3=50
print(a3)
50
4a=90
SyntaxError: invalid decimal literal
a0123456789=100
print(a0123456789)
100
name="prasanna"
print(name)
prasanna
print("name")
name
city="vja"
print(city)
vja
country="india"
print(country)
india
>>> @a=40
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> _=20
>>> print(_)
20
>>> _b=100
>>> print(_)
20
>>> mailid="prasanna@gmail.com"
>>> print(mailid)
prasanna@gmail.com
>>> if=30
SyntaxError: invalid syntax
>>> elif=70
SyntaxError: invalid syntax
>>> print=10
>>> print(print)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(print)
TypeError: 'int' object is not callable
>>> a=4,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=4;b=9
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(a+b)
TypeError: 'int' object is not callable
>>> a,b=2,3
>>> print(a+b)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(a+b)
TypeError: 'int' object is not callable
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> print(a,b,c)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(a,b,c)
TypeError: 'int' object is not callable
