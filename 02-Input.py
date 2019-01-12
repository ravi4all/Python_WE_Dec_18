# by default input type is string
name = input("Enter your name : ")
#msg = "Hello "+name
#msg = "Hello {}".format(name)
msg = f"Hello {name}"
print(msg)

# type cast
# int, float, str, bytes...
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
result = num_1 + num_2
print("Sum is",result)
