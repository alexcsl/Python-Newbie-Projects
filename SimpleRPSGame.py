#    MAKE A ROCK PAPER SCISSORS GAME !!!
import random
import os

def get_choice() :
    choices = ["rock", "paper", "scissors"]
    playerChoice = validate_player_choice()
    roboChoice = random.choice(choices)
    choice = {"Player": playerChoice.lower(), "Computer": roboChoice}
    return choice

#function to check the win
            #casefold() for ignore case
def check_win(playerChoice, computerChoice):
    #Formatted String Literals =  print(f".....") 
    print(f"The User chooses: {playerChoice.capitalize()}!\nThe Almighty Bot chooses: {computerChoice.capitalize()}!")
    #check the win condition
    if playerChoice == computerChoice:
        return "\nNice Tie!"
    elif playerChoice == "rock":
        if computerChoice == "scissors":
            return "Rock can break scissors!\n\nYou Win!!"
        else: return "Rock gets consumed by paper\n\nYou Lose!!"
    elif playerChoice == "scissors":
        if computerChoice == "paper":
            return "Scissors cut Paper!\n\nYou Win!!"
        else: return "Scissors can't cut rock :(\n\nYou Lose!!"
    elif playerChoice == "paper":
        if computerChoice == "rock":
            return "Paper consumes Rock!\n\nYou Win!!"
        else: return "Easy Cut!\n\nYou Lose!!"

#Function to start game
def game_start():
    choice = get_choice()
    #Accessing the Dictionary "Choice"
    pChoice = choice["Player"]
    cChoice = choice["Computer"]
    result = check_win(pChoice, cChoice)
    print(result)
    print("\n")
    input("Press ENTER to continue... ")
    try_again()

#function to prompt user input to try again or not
def try_again():
    #Input Validation
    while (True):
        restartChoice = input("Try Again? [Y/N] ")
        if(restartChoice == "y" or restartChoice == "n" or restartChoice == "Y" or restartChoice == "N"):
            print("Choice Accepted.")
            break
        else:
            print("Please input either [Y/N]! ")

    #switch case for the choice
    if restartChoice == "Y" or restartChoice == "y":
        os.system('cls')
        print("Rematch Accepted")
        game_start()
    else: #no need to put conditions because the input is already validated
        os.system('cls')
        print("Thank you for playing this simple Rock Paper Scissors game!\n\n")

#function to validate player's choice
def validate_player_choice():
    while(True):
        choice = input("Enter your move (Rock, Paper, Scissors): ")
        if choice.lower() == "rock" or choice.lower() == "paper" or choice.lower() == "scissors":
            break
        else:
            print("\nInput either ""Rock"", ""Paper"", or ""Scissors""!!")
    return choice

#The first initial game start
game_start()