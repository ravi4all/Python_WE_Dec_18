#Using eval()
def calc(x,y):
    z = x + y
    print(z)

print("""
1. Add
2. Sub
3. Mul
4. Div
""")

ch = input("Enter your choice : ")

todo = {
    "1" : calc,
    "2" : calc,
    "3" : calc,
    "4" : calc
    }

num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
todo.get(ch, errHandler)(num_1, num_2)
