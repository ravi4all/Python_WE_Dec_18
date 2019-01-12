import webbrowser

helloIntent = ['hi','hello','hey','hey there','hi there','hola','howdy']

# Membership Operator - in, not in

chat = True
while chat:
    msg = input("Enter your message : ")

    if msg in helloIntent:
        print("Hello There...")
    elif msg.startswith('open'):
        web = msg.split()[-1]
        webbrowser.open(web+'.com')
    elif msg == "bye":
        print("Bye")
        chat = False
    else:
        print("I don't understand")
