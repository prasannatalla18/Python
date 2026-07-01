Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,5.6,"python",6+9j,True,False]
print(a)
[2, 5.6, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=5
type(b)
<class 'int'>
c=[5]
type(c)
<class 'list'>
a=["python","java","c","c++"]
a.append("DSA")
a
['python', 'java', 'c', 'c++', 'DSA']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', 'DSA', ['ml', 'ai']]
#extend
a=["ml","ai","ds"]
a.extend(["c","c++","python"])
a
['ml', 'ai', 'ds', 'c', 'c++', 'python']
#insert
b=["vja","hyd"]
b.insert(1."vzg")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b.insert(1,"vzg")
b
['vja', 'vzg', 'hyd']
#index
a=["black","white","pink","red"]
a.index("white")
1
a.copy()
['black', 'white', 'pink', 'red']
#copy
b=a.copy()
b
['black', 'white', 'pink', 'red']
b.count("pink")
1
#sort
a=["grapes","apple","mango","banana"]
a.sort()
a
['apple', 'banana', 'grapes', 'mango']
b=[8,6,0,3,6,1,2,20]
b.sort()
>>> b
[0, 1, 2, 3, 6, 6, 8, 20]
>>> a=[7,8,9,10,12,40,60]
>>> a.reverse
<built-in method reverse of list object at 0x0000022C278163C0>
>>> a.reverse()
>>> a
[60, 40, 12, 10, 9, 8, 7]
>>> b=["java","html","css"]
>>> b.reverse()
>>> b
['css', 'html', 'java']
>>> a=["c","c++","ml","ai"]
>>> a.pop()
'ai'
>>> a
['c', 'c++', 'ml']
>>> a.pop("c++")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.pop("c++")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(1)
'c++'
>>> a
['c', 'ml']
>>> #remove
>>> a.remove("ml")
>>> a
['c']
>>> a=["prasanna","rama","aruna","chandrusha"]
>>> len(a)
4
>>> b="pooja"
>>> len(b)
5
>>> c=["pooja"]
>>> len(c)
1
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("hi")
>>> b
['hi']
