Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #striding
>>> a="Data science"
>>> a[::]
'Data science'
>>> a[::1]
'Data science'
>>> a[::2]
'Dt cec'
>>> b="cloud computing"
>>> a[::5]
'Dsc'
>>> b[::5]
'c u'
>>> b[::4]
'cdmi'
>>> b[::8]
'cm'
>>> a[2:]
'ta science'
>>> b[2:]
'oud computing'
>>> b[3:11]
'ud compu'
>>> a[::2]
'Dt cec'
>>> b[::2]
'codcmuig'
>>> b[::6]
'cci'
>>> c="machine learning"
>>> c[1:9:2]
'ahn '
>>> c[3:14:2]
'hn eri'
>>> a[5:15:4]
'sn'
>>> c[5:15:4]
'nei'
>>> c[2:12:3]
'cnlr'
>>> c[0:10:1]
'machine le'
>>> #negative striding
>>> d="python course"
>>> d[-1:-10:-2]
'ero o'
d[-3:-13:-4]
'r t'
d[-5:-11:-3]
'on'
