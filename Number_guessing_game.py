import random
import art
def Play_game():
    print(art.logo)
    number=random.randrange(1, 100)
    hidden_number="_"
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100. ")
    print("The number: ",hidden_number,"\n")
    player_choice=str(input("Choose a difficulty. Type 'easy' or 'hard' :\n" ))
    attempts = 10 if player_choice == "easy" else 5

    for _ in range(attempts):
                user=int
                try:
                    user=int(input(f"You have remaining {attempts} attempts to guess the number. \nMake a guess : "))
                except ValueError:
                 print("Please enter a valid number!")
                 attempts-=1
                 if attempts == 1 and user != number:
                    print("You've run out of guesses, you lose.😟😟😟")
                    break
                 continue
                
                if attempts == 1 and user != number:
                    print("You've run out of guesses, you lose.😟😟😟")
                    break

                if user != number :
                    attempts-=1

                if user < number:
                    print("To low 😟. \n Guess again \n ")

                elif user > number:
                    print("To high😟. \n Guess again \n ")

                elif user == number:
                    print(f"\n 🤩🤩🤩 !!! yah! You guessed right number. You Win! 😇😇😇 . The number is: {number} ")
                    break

                continue
Play_game()