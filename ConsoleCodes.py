Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = [12,3,4,6,'hi','hello',10.4,45.3,True]
>>> x
[12, 3, 4, 6, 'hi', 'hello', 10.4, 45.3, True]
>>> import numpy
>>> numpy.array([[12, 3, 4, 6, 'hi', 'hello', 10.4, 45.3, True]])
array([['12', '3', '4', '6', 'hi', 'hello', '10.4', '45.3', 'True']],
      dtype='<U11')
>>> numpy.array([12, 3, 4, 6, 'hi', 'hello', 10.4, 45.3, True])
array(['12', '3', '4', '6', 'hi', 'hello', '10.4', '45.3', 'True'],
      dtype='<U11')
>>> x[0]
12
>>> x[0:5]
[12, 3, 4, 6, 'hi']
>>> x[-1]
True
>>> x[5:0:-1]
['hello', 'hi', 6, 4, 3]
>>> names = []
>>> names.append('Ram')
>>> names
['Ram']
>>> names.append('Raman')
>>> names.append('Aman')
>>> names.append('Amit')
>>> names.append('Ajay')
>>> names.append('Vijay')
>>> names
['Ram', 'Raman', 'Aman', 'Amit', 'Ajay', 'Vijay']
>>> names.pop()
'Vijay'
>>> names
['Ram', 'Raman', 'Aman', 'Amit', 'Ajay']
>>> names.pop(3)
'Amit'
>>> names.insert(2,'Pooja')
>>> names
['Ram', 'Raman', 'Pooja', 'Aman', 'Ajay']
>>> names.remove('Ajay')
>>> names
['Ram', 'Raman', 'Pooja', 'Aman']
>>> city = ['Pune','Mumbai','Noida','Patna','Chennai']
>>> names
['Ram', 'Raman', 'Pooja', 'Aman']
>>> names.append(city)
>>> names
['Ram', 'Raman', 'Pooja', 'Aman', ['Pune', 'Mumbai', 'Noida', 'Patna', 'Chennai']]
>>> names.pop()
['Pune', 'Mumbai', 'Noida', 'Patna', 'Chennai']
>>> names
['Ram', 'Raman', 'Pooja', 'Aman']
>>> names.extend(city)
>>> names
['Ram', 'Raman', 'Pooja', 'Aman', 'Pune', 'Mumbai', 'Noida', 'Patna', 'Chennai']
>>> names.index('Aman')
3
>>> sorted(names)
['Aman', 'Chennai', 'Mumbai', 'Noida', 'Patna', 'Pooja', 'Pune', 'Ram', 'Raman']
>>> names
['Ram', 'Raman', 'Pooja', 'Aman', 'Pune', 'Mumbai', 'Noida', 'Patna', 'Chennai']
>>> names.sort()
>>> names
['Aman', 'Chennai', 'Mumbai', 'Noida', 'Patna', 'Pooja', 'Pune', 'Ram', 'Raman']
>>> names = tuple(names)
>>> names
('Aman', 'Chennai', 'Mumbai', 'Noida', 'Patna', 'Pooja', 'Pune', 'Ram', 'Raman')
>>> names[0] = 'Ravi'
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    names[0] = 'Ravi'
TypeError: 'tuple' object does not support item assignment
>>> names = 'Ram', 'Shyam', 'Aman'
>>> names
('Ram', 'Shyam', 'Aman')
>>> a = 12
>>> a = 12,
>>> a
(12,)
>>> emp = {}
'
>>> emp = {'name':'Ram','dept':}
SyntaxError: invalid syntax
>>> 
>>> emp = {'name':'Ram','dept':'IT','sal':23000,'comp':'HCL'}
>>> emp
{'name': 'Ram', 'dept': 'IT', 'sal': 23000, 'comp': 'HCL'}
>>> emp.keys()
dict_keys(['name', 'dept', 'sal', 'comp'])
>>> emp[0]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    emp[0]
KeyError: 0
>>> emp['name']
'Ram'
>>> emp['city'] = 'Pune'
>>> emp
{'name': 'Ram', 'dept': 'IT', 'sal': 23000, 'comp': 'HCL', 'city': 'Pune'}
>>> emp.pop('city')
'Pune'
>>> emp
{'name': 'Ram', 'dept': 'IT', 'sal': 23000, 'comp': 'HCL'}
>>> emp = {}
>>> type(emp)
<class 'dict'>
>>> emp = dict()
>>> names = ['ram','shyam','aman','anuj','akash','vaibhav']
>>> sal = [10000,20000,30000,40000,50000,60000]
>>> comp = []
>>> 
>>> comp = ['tcs','hcl','tcs','tcs','hcl','ibm']
>>> emp
{}
>>> emp = {'names':names,'sal':sal,'comp':comp}
>>> emp
{'names': ['ram', 'shyam', 'aman', 'anuj', 'akash', 'vaibhav'], 'sal': [10000, 20000, 30000, 40000, 50000, 60000], 'comp': ['tcs', 'hcl', 'tcs', 'tcs', 'hcl', 'ibm']}
>>> emp['names'][0], emp['sal'][0], emp['comp'][0]
('ram', 10000, 'tcs')
>>> for i in range(len(emp['names'])):
	emp['names'][i], emp['sal'][i], emp['comp'][i]

	
('ram', 10000, 'tcs')
('shyam', 20000, 'hcl')
('aman', 30000, 'tcs')
('anuj', 40000, 'tcs')
('akash', 50000, 'hcl')
('vaibhav', 60000, 'ibm')
>>> 
