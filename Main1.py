from colorama import Fore
import random
import os
from logo import display_logo


def options():
    options = Fore.MAGENTA + '''
    1.  Single Player
    2.  Two Players
    3.  Exit
    '''
    print(options)
    print("\n")
    
def selection():
    select = input("Enter the Option : ")
    return select

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def guess_number(number, player_name):
    guess_count = 0
    Guess = False
    while not Guess:
        try:
            guess = int(input(Fore.BLUE + f"{player_name}, Guess the number : "))
            if guess < 1 or guess > 100:
                print(Fore.RED + "Number is Out of Range. Please guess between 1 and 100.")
                continue
            
            guess_count += 1
            
            if guess == number:
                print(Fore.GREEN + "Congratulations! You guessed it right!")
                Score = max(0, 100 - ((guess_count - 3) / guess_count) * 100) if guess_count > 3 else 100
                print("\n")
                print(Fore.LIGHTMAGENTA_EX + f"Your Score is {int(Score)}%.")
                Guess = True
                return Score
            
            elif guess < number:
                print(Fore.YELLOW + f"Number is Greater than {guess}")
            else:
                print(Fore.YELLOW + f"Number is Lesser than {guess}")
                
            print("\n")
        
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number.")

def Single_player():
    print("\nInstructions :-")
    instruction = Fore.GREEN + '''
    *****************************************************
    *                                                   *
    *   # Guess the Number between 1 to 100             *
    *   # You have 3 free chances to guess the number   *
    *   # After 3 chances your Score will decrease      *
    *                                                   *
    *****************************************************
    '''
    print(instruction)
    
    number = random.randint(1, 100)
    Score = guess_number(number, "Player")
    print("\nPress Enter to continue...")
    input()

def multiplayer():
    print("\nInstructions :-")
    instruction = Fore.GREEN + '''
    *****************************************************
    *                                                   *
    *   # Guess the Number between 1 to 100             *
    *   # You have 3 free chances to guess the number   *
    *   # After 3 chances your Score will decrease      *
    *                                                   *
    *****************************************************
    '''
    print(instruction)
    
    Player1 = input(Fore.MAGENTA + "Enter the First Player's Name : ")
    Player2 = input(Fore.RESET + "Enter the Second Player's Name : ")
    
    clear_screen()
    display_logo()
    
    number1 = random.randint(1, 100)
    first_player_Score = guess_number(number1, Player1)
    
    print(Fore.RED + f"Now, it's {Player2}'s turn to guess the number! Press Enter to continue...")
    input()
    
    clear_screen()
    display_logo()
    
    number2 = random.randint(1, 100)
    second_player_Score = guess_number(number2, Player2)
    
    print("\n")
    
    if second_player_Score > first_player_Score:
        print(Fore.GREEN + f"{Player2} wins the game with a score of {int(second_player_Score)}%")
    else:
        print(Fore.GREEN + f"{Player1} wins the game with a score of {int(first_player_Score)}%")
    
    print("\nPress Enter to continue...")
    input()

while True:
    clear_screen()
    display_logo()
    options()
    select = selection()
    
    if select == "1":
        clear_screen()
        display_logo()
        Single_player()
        
    elif select == "2":
        clear_screen()
        display_logo()
        multiplayer()
        
    elif select == "3":
        print(Fore.YELLOW + "Thank you for playing! Goodbye!")
        break