def calc():
    x = 12
    y = 12
    def add():
        z = x + y
        return z
    def sub():
        z = x - y
        return z

    #a = add()
    #s = sub()
    #return a,s
    return add, sub

##add = calc()[0]()
##print(add)

a,b = calc()
print(a())
print(b())
