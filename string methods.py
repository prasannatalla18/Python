Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string methods
>>> #len()
>>> a="python"
>>> len(a)
6
>>> b="python course"
>>> len(b)
13
>>> c=""
>>> len(c)
0
>>> d=" "
>>> len(d)
1
>>> #count
>>> a="twinkle twinkle little star"
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("twinkle")
2
>>> a.count("t")
5
>>> a.count("k")
2
>>> a.count(" ")
3
>>> #find a string
>>> a="code"
>>> a[1]
'o'
>>> a.find("d")
2
>>> a.find("e")
3
>>> b="hello"
>>> b.find("l")
2
>>> b[2:4]
'll'
>>> #escape sequences
>>> #\n->new line
>>> #\t->tab space
a="name\nmobile\tmailid\nclg
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobile\tmailid\nclg"
print(a)
name
mobile	mailid
clg
b="name:prasanna\nmobileno:7330911992\tmailid:prasannatalla18@gmail.com\nclg:SCET"
print(b)
name:prasanna
mobileno:7330911992	mailid:prasannatalla18@gmail.com
clg:SCET
#replace
a="wait until you succeed"
a.replace("wait",work)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.replace("wait",work)
NameError: name 'work' is not defined
a.replace("wait","work")
'work until you succeed'
a
'wait until you succeed'
b="wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'
b.replace("wait","work",1)
'work wait until you succeed'
#lower
c="HI"
c.lower()
'hi'
c="python"
c.upper(0)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c.upper(0)
TypeError: str.upper() takes no arguments (1 given)
a[0].upper()
'W'
c[0].upper()
'P'
c.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.title()
'I Am In Class'
#some cases
a="java"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha
<built-in method isalpha of str object at 0x0000027989C1EF70>
a.isalpha()
True
b="python course"
b.isalpha()
False
c="pythoncourse"
c.isalpha()
True
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="1234"
d.isdigit()
True
d.isalnum()
True
e="prasanna123"
e.isalnum()
True
f="prasann@123"
f.isalnum()
False
#
a=hello python"
SyntaxError: unterminated string literal (detected at line 1)
a="hello python"
a.startswith("h")
True
a.endswith("n")
True
#strip()
#lstrip(),rstrip()
a="                 prasanna            "
a.strip()
'prasanna'
a.lstrip()
'prasanna            '
a.rstrip()
'                 prasanna'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am in vijayawada"
b.split()
['i', 'am', 'in', 'vijayawada']
c="codegnan"
c.split()
['codegnan']
#join
a="vij hyd vzg"
"".join(a)
'vij hyd vzg'
b="vij","hyd","vzg"
"".join(b)
'vijhydvzg'
" ".join(b)
'vij hyd vzg'
"k".join(b)
'vijkhydkvzg'
#concatenation
a="hello"
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
fname="prasanna"
lname="talla"
print(fname+lname)
prasannatalla
print(fname+" "+lname)
prasanna talla
print(fname.title()+" "+lname.title())
Prasanna Talla
print((fname+" "+lname).title())
Prasanna Talla
#formatting
a=4
b=8
print(a+b)
12
print("the sum is",a+b)
the sum is 12
x="vij"
print("the city is",x)
the city is vij
#format method
a="motu"
b="patulu"
print("hello",a+b)
hello motupatulu
print("hello {}{}",.format(a,b))
SyntaxError: invalid syntax
print("hello {}{}".format(a,b))
hello motupatulu
print("hello {} {}",.format(a,b))
SyntaxError: invalid syntax
print("hello {} {}".format(a,b))
hello motu patulu
print("hello {} hello{}".format(a,b))
hello motu hellopatulu
#fstring
a="sita"
b="ram"
print(f"hello {a}{b}")
hello sitaram
print(f"hello {a} {b}")
hello sita ram
