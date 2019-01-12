import time

seconds = 133
m = seconds // 60
s = seconds % 60

while True:
    time.sleep(0.5)
    s -= 1

    if m == 0 and s == 0:
        break

    print("{}:{}".format(m,s))

    if s == 0:
        m -= 1
        s = 60
