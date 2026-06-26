Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypes
>>> a=10
>>> type(a)
<class 'int'>
>>> b=4.5
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="codegnan"
>>> type(d)
<class 'str'>
>>> e='''prasanna'''
>>> type(e)
<class 'str'>
>>> f=3+4j
>>> type(f)
<class 'complex'>
>>> g=7j
>>> type(g)
<class 'complex'>
>>> h=6i+3
SyntaxError: invalid decimal literal
>>> i=4j=3
SyntaxError: cannot assign to literal
>>> i=4j+3
>>> type(i)
<class 'complex'>
>>> j=True
>>> type(j)
<class 'bool'>
>>> k=False
>>> type(k)
<class 'bool'>
>>> l=false
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l=false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> m="True"
>>> type(m)
<class 'str'>
