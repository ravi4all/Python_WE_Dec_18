def atm():
    try:
        total = 10000
        pin = input("Enter PIN : ")
        if pin == "1234":
            print("Welcome User")
        else:
            # print("Invalid User")
            raise ValueError("Invalid User")
    except ValueError as err:
        print(err)
        atm()

    try:
        amount = int(input("Enter amount : "))
        if amount > total:
            raise ValueError("Insufficient Balance...")
        total -= int(amount)
        print("Remaining Balance...")
        print("Transaction Completed...")
    except ValueError as err:
        print(err)
        atm()

# try:
#     atm()
# except ValueError as err:
#     print(err)
#     atm()

atm()