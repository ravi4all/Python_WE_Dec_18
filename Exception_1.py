try:
    a = int(input("Enter a number : "))
    b = int(input("Enter another number : "))

    i = a + b
    j = a - b
    k = a / b
    l = a * b
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except BaseException as ex:
    print(ex)
else:
    print(i)
    print(j)
    print(k)
    print(l)