import webbrowser, os, random
import searchMovie

def chat():
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
        elif msg == "play music":
            path = r'C:\Users\asus\Music'
            os.chdir(path)
            songs = os.listdir()
            song = random.choice(songs)
            os.startfile(song)
        elif msg == "bye":
            print("Bye")
            chat = False
        else:
            print("I don't understand")

print("""
1. Movie Search Engine
2. Product Search Engine
3. Dictionary
4. Start Chat
""")

choice = input("Enter your choice: ")

if choice == "1":
    searchMovie.search()
elif choice == "4":
    chat()
else:
    print("Wrong Choice...")
