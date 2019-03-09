try:
    file = open('file_1.txt','w')
    data = 'Write this into file'
    file.write(data)
    # data = file.read()
    print(data)
except BaseException as ex:
    # print("Some error")
    print(ex)
finally:
    print("Inside Finally")
    file.close()