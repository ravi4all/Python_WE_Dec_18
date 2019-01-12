num = 29
prime = False
'''
for i in range(2,num):
    if num % i == 0:
        prime = False
        break
    else:
        prime = True

if prime:
    print("Prime Number")
else:
    print("Not Prime")
'''

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
