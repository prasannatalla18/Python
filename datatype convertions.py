Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype convertions
#int
int(6)
6
int(4.5)
4
int("python")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(3+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(6)
6.0
float(5.4)
5.4
float("python")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
float(3+9j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(3+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
>>> #string
>>> str(6)
'6'
>>> str(5.3)
'5.3'
>>> str("python")
'python'
>>> str(3+9j)
'(3+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex
>>> complex(6)
(6+0j)
>>> complex(6.3)
(6.3+0j)
>>> complex("python")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
>>> complex(3+9j)
(3+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(8)
True
>>> bool(4.5)
True
>>> bool("python")
True
>>> bool(3+9j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> bool(1)
True
>>> bool(0)
False
