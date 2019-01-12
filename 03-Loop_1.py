#Loops

#for    - loop will execute in a range 
#while  - loop will execute untill condition becomes false

'''
range(5)
- loop will start from 0 by default and step will be of 1

range(5,20)
- loop will start from 5 and will stop at 20

range(5,20,2)
- loop will start from 5 and inc. by 2 and will stop at 20
'''

for i in range(4):
    print(i)
    print("Hello")

print('Bye')


for i in reversed(range(1,10)):
    print(i)
print('-------------------')

for i in range(10,1,-1):
    print(i)
