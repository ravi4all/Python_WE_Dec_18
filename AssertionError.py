def atm():
    try:
        total = 10000
        pin = input("Enter PIN : ")
        assert (pin == '1234'), "Invalid PIN"
    except AssertionError as err:
        print(err)
        atm()

    try:
        amount = int(input("Enter amount : "))
        assert (amount < total), "Insufficient Balance"
        total -= int(amount)
        print("Remaining Balance...",total)
        print("Transaction Completed...")
    except AssertionError as err:
        print(err)
        atm()

# try:
#     atm()
# except ValueError as err:
#     print(err)
#     atm()

atm()