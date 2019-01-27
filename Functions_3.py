'''
Dynamic Arguments
*args
**kwargs
'''

def add(*x):
    #print(x)
    count = 0
    for val in x:
        count += val
    print(count)

add(4,5,6,12,5,55)

def emp(**details):
    print(details)

emp(name='Ram',sal=25000,dept='IT')
emp(name='Shyam',dept='IT',address='Delhi',location='Pune')
emp(name='Anuj',company='HCL',dept='HR',sal=26000)
