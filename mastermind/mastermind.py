#maximum size of code
MAX = 5

import sys

#input player code
def player_code():
    code = "string to check max length"
    while(len(code) > MAX):
        #code = input(f'Enter your code (max length is {MAX}): ')
        print(f'Enter your code (max length is {MAX})')
        code = sys.stdin.readline().strip()
        if(code == ""):
            code = "string to check max length"
    return code

#player guesses
def player_guess(code, size):
    guess = ""
    attempts = 0
    while (guess != code):
        while(len(guess) < size):
            guess = input(f'Enter your guess (size of guess is {size}): ')

        attempts += 1
        if(guess == code):
            print("You cracked the code!\n")
            return attempts
        for digit_index in range(0, size):
            if(guess[digit_index] == code[digit_index]):
                print(guess[digit_index]," is in the correct position\n")
            elif(guess[digit_index] in code):
                print(guess[digit_index], "is in the code, but not at the right position\n")
            else:
                print(guess[digit_index], "is wrong\n")
        guess = ""
#hiding the code
def hide():
    print("\033[H\033[J", end="")

def winner(one, two):
    if(one < two):
        print("Player 1 has won!\tGuesses: Player 1: ",one, "\n\t\t\t\t Player 2: ",two,"\n")
    elif(one == two):
        print("Tie!\tGuesses for both the players: ",one,"\n")
    else:
        print("Player 2 has won!\tGuesses: Player 1: ",one, "\n\t\t\t\t Player 2: ",two,"\n")

def main():
    #size_of_code = int(input("Decide the size of code (for maintaining equal chances): "))
    print("Only for player 1\n")
    player_one_code = player_code()
    size_of_code = len(player_one_code)
    hide()
    print("Only for player 2\n")
    player_two_attempts = player_guess(player_one_code, size_of_code)

    print("Only for player 2\n")
    player_two_code = player_code()
    size_of_code = len(player_two_code)
    hide()
    print("Only for player 1\n")
    player_one_attempts = player_guess(player_two_code, size_of_code)

    winner(player_one_attempts, player_two_attempts)

main()