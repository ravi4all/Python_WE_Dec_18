import random

gamePosition = [0,1,2,3,4,5,6,7,8]
def gameBoard():
    print("""
        {} | {} | {}
        ----------
        {} | {} | {}
        ----------
        {} | {} | {}
    """.format(gamePosition[0], gamePosition[1],
               gamePosition[2], gamePosition[3],
               gamePosition[4], gamePosition[5],
               gamePosition[6], gamePosition[7],
               gamePosition[8]))

def check_winner(char, pos_1, pos_2, pos_3):
    if gamePosition[pos_1] == char and gamePosition[pos_2] == char and gamePosition[pos_3] == char:
        return True

def check_all(char):
    if check_winner(char, 0, 1, 2):
        return True
    if check_winner(char, 3, 4, 5):
        return True
    if check_winner(char, 6, 7, 8):
        return True

    if check_winner(char, 0, 3, 6):
        return True
    if check_winner(char, 1, 4, 7):
        return True
    if check_winner(char, 2, 5, 8):
        return True

    if check_winner(char, 0, 4, 8):
        return True
    if check_winner(char, 2, 4, 6):
        return True

def game():
    user_ch = input("Enter your choice - 0 or X ? ")
    cpu_ch = ""
    if user_ch == 'X':
        cpu_ch = '0'
    elif user_ch == '0':
        cpu_ch = 'X'
    pos_occupied = []
    while True:
        gameBoard()
        user_pos = int(input("Enter the position : "))
        if user_pos in pos_occupied:
            print("Position Occupied")
            continue
        gamePosition[user_pos] = user_ch
        pos_occupied.append(user_pos)

        if check_all(user_ch) == True:
            gameBoard()
            print("You Win")
            break
        elif check_all(cpu_ch) == True:
            gameBoard()
            print("CPU Win")
            break

        while True:
            cpu_pos = random.randrange(9)
            if cpu_pos not in pos_occupied:
                gamePosition[cpu_pos] = cpu_ch
                pos_occupied.append(cpu_pos)
                # gameBoard()
                break
game()
