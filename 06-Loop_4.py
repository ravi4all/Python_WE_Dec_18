'''
    *
   ***
  *****
 *******
*********
'''

for i in range(10):
    print(' ' * (10 - i) + '*' * (2*i + 1))

for i in range(10):
    for j in range(10 - i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()
