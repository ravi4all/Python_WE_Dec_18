Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "this is some demo text. python programming for machine learning"
>>> a.upper()
'THIS IS SOME DEMO TEXT. PYTHON PROGRAMMING FOR MACHINE LEARNING'
>>> a.title()
'This Is Some Demo Text. Python Programming For Machine Learning'
>>> a.capitalize()
'This is some demo text. python programming for machine learning'
>>> a.count('i')
5
>>> a.index('i')
2
>>> a.index('i', 3)
5
>>> a.index('i', 6)
39
>>> a[0]
't'
>>> a[1]
'h'
>>> a[5]
'i'
>>> a[-1]
'g'
>>> a[0:6]
'this i'
>>> a[0:10]
'this is so'
>>> a[0:20:2]
'ti ssm eot'
>>> a
'this is some demo text. python programming for machine learning'
>>> a[0:20:2]
'ti ssm eot'
>>> a[0:20:3]
'tsso mt'
>>> a[20:0]
''
>>> a[20:1]
''
>>> a[20:1:-1]
'xet omed emos si si'
>>> a[-1:-20]
''
>>> a[-1:-20:-1]
'gninrael enihcam ro'
>>> a[-20:-1]
'for machine learnin'
>>> a.startswith('o')
False
>>> a.startswith('t')
True
>>> a.endswith('i')
False
>>> a
'this is some demo text. python programming for machine learning'
>>> a.isdigit()
False
>>> a.islower()
True
>>> a.center(13)
'this is some demo text. python programming for machine learning'
>>> a.center(50)
'this is some demo text. python programming for machine learning'
>>> len(a)
63
>>> a = "welcome to hdfc"
>>> len(a)
15
>>> a.center(16)
'welcome to hdfc '
>>> a.center(17)
' welcome to hdfc '
>>> a.center(30)
'       welcome to hdfc        '
>>> a.center(30,'&')
'&&&&&&&welcome to hdfc&&&&&&&&'
>>> a.center(30,'#')
'#######welcome to hdfc########'
>>> a.center(30,'-')
'-------welcome to hdfc--------'
>>> a.split()
['welcome', 'to', 'hdfc']
>>> 
