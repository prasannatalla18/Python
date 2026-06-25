Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=4,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=9
print(a+b)
13
a,b=2,3
print(a+b)
5
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
a=b=c=10
print(a,b,c)
10 10 10
a,b,c=2,3,4
print(a,b,c)
2 3 4
a,b,c=2,3,4,5,6
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a,b,c=2,3,4,5,6
ValueError: too many values to unpack (expected 3, got 5)
>>> a,b,c=(3,4,5)
>>> print(a,b,c)
3 4 5
>>> first name="prasanna"
SyntaxError: invalid syntax
>>> first_name="prasanna"
>>> print(first_name)
prasanna
>>> firstname="prasanna"
>>> print(firstname)
prasanna
>>> fname="lakshmi"
>>> lname="prasanna"
>>> print(fname+lname)
lakshmiprasanna
>>> print(fname+" "+lname)
lakshmi prasanna
>>> print(fname,lname)
lakshmi prasanna
>>> name="prasanna"
>>> print(name)
prasanna
>>> NAME="prasanna"
>>> print(NAME)
prasanna
>>> Name="prasanna"
>>> print(Name)
prasanna
>>> a=4
>>> print(a)
4
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
