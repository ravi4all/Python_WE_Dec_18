def add(x,y):
    z = x + y
    print(z)

def sub(x,y):
    #z = x - y
    z = x - y if x > y else y - x
    print(z)

def mul(x,y):
    z = x * y
    print(z)

def div(x,y):
    z = x / y
    print(z)

def errHandler(*args):
    print("Invalid Choice...")

print("""
1. Add
2. Sub
3. Mul
4. Div
""")

ch = input("Enter your choice : ")

todo = {
    "1" : add,
    "2" : sub,
    "3" : mul,
    "4" : div
    }

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
todo.get(ch, errHandler)(num_1, num_2)
