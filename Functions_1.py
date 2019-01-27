#global variable
x = 10
y = 22
def add():
    #local variable
    x = 12
    y = 14
    global z
    z = x + y
    print(z)

add()
print("Before:",z)
z = x - y
print("After:",z)
