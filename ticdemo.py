
choices = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


# for x in range(0, 9):
#     choices.append(str(x + 1))

playerOneTurn = True
winner = False
# Level 1:
# Print a 4 x 4 board
# - Shuffle dice
# - Choose a random side of each die
# - Print it out
# - Get user input


def printBoard():

    print(choices[0] + ' ' + '|' + ' ' +
          choices[1] + ' ' + '|' + ' ' + choices[2])
    print('---------')
    print(choices[3] + ' ' + '|' + ' ' +
          choices[4] + ' ' + '|' + ' ' + choices[5])
    print('---------')
    print(choices[6] + ' ' + '|' + ' ' +
          choices[7] + ' ' + '|' + ' ' + choices[8])


def check_winner():
    if (((choices[0] == 'X' or 'O') and (choices[1] == 'X' or 'O') and (choices[2] == 'X' or 'O')) or
        ((choices[3] == 'X' or 'O') and (choices[4] == 'X' or 'O') and (choices[5] == 'X' or 'O')) or
        ((choices[6] == 'X' or 'O') and (choices[7] == 'X' or 'O') and (choices[8] == 'X' or 'O')) or
        ((choices[0] == 'X' or 'O') and (choices[3] == 'X' or 'O') and (choices[6] == 'X' or 'O')) or
        ((choices[1] == 'X' or 'O') and (choices[4] == 'X' or 'O') and (choices[7] == 'X' or 'O')) or
        ((choices[2] == 'X' or 'O') and (choices[5] == 'X' or 'O') and (choices[8] == 'X' or 'O')) or
        ((choices[0] == 'X' or 'O') and (choices[4] == 'X' or 'O') and (choices[8] == 'X' or 'O')) or
            ((choices[2] == 'X' or 'O') and (choices[4] == 'X' or 'O') and (choices[6] == 'X' or 'O'))):
        global winner = True
        print("win")


while not winner:
    printBoard()

    if playerOneTurn:
        print("Player 1:")
    else:
        print("Player 2:")

    # IF CHOICE IS NOT A INT GIVE AN ERROR
    try:
        choice = int(input(">> "))
    except:
        print("please enter a number 1 - 9")
        continue

    # IF PLACE IS TAKEN, THIS WILL RETURN ERROR
    if choices[choice - 1] == 'X' or choices[choice-1] == 'O':
        print("illegal move, plase try again")
        continue

    # replaces index of choices with marker
    if playerOneTurn:
        choices[choice - 1] = 'X'
    else:
        choices[choice - 1] = 'O'

    # DWI's a CUNT!
    playerOneTurn = not playerOneTurn

    # check win
    check_winner()
    #
    # if ((choices[0] == "X" or "O") and (choices[1] == "X" or "O") and (choices[2] == "X" or "O")):

    #     winner = True
    #     print("win")
