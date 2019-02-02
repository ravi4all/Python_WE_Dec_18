def calc(x,y):
    return x+y, x-y, x*y, x/y

#output = calc(12,45)
#print(output)

a,b,c,d = calc(12,45)
print(a,b,c,d)

a,b,*c = calc(12,6)
print(a,b,c)
