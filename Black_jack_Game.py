import art  # Importing the art module
import random  # Importing the random module to randomly select cards
print(art.logo)  # Print the logo from the art module # Initialize player and computer scores, and set the target blackjack value to 21
p1_score = 0 
c_score = 0
blackjack = 21
user=str
def blackjack_game():   # Define a list of possible card values, including face cards and aces
    cards = [1,11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    lenn = len(cards)  # Get the length of the card list
    p1_score = 0  # Reset player score
    c_score = 0  # Reset computer score
    blackjack = 21  # Target score
    p1_cards_store = []  # Store player's cards
    comp_cards_store = []  # Store computer's cards
    go = True  # Control variable for player's actions
    go1 = True  # Control variable for overall game state
    # First round: deal initial hands
    for _ in range(1):  
        for _ in range(2):  # Draw 2 cards for the player
            p1_cards = random.randint(0,lenn-1)
            p1_cards_store.append(cards[p1_cards])
        # Calculate player's score from the drawn cards
        p1_score =sum(p1_cards_store)
        print(f"\n Your Cards: {p1_cards_store},  Current score: {p1_score}")
        # Draw 2 cards for the computer
        for _ in range(2):
            comp_cards = random.randint(0,lenn-1)
            comp_cards_store.append(cards[comp_cards])
        # Calculate computer's score from the drawn cards
        c_score = sum(comp_cards_store)
        print(f" Computer first Card: {comp_cards_store[0]} ")  # Main game loop: check for blackjack, player's actions, and game outcomes
    while go1:
        if p1_score == c_score == blackjack:  # If both have blackjack, it's a draw
            print("Draw")
            print(f" Computer Card: {comp_cards_store} score: {c_score}")
            go1 = False
        elif p1_score == blackjack:  # Player wins 😇 if they hit blackjack
            print("Player 1 wins 😇")
            print(f" Computer Card: {comp_cards_store} score: {c_score}")
            go1 = False
        elif c_score == blackjack:  # Computer wins 😇 if they hit blackjack
            print("Computer  wins 😇")
            print(f" Computer Card: {comp_cards_store} score: {c_score}")
            go1 = False
        elif p1_score > blackjack:  # Player loses if they bust
            print("Player_1 lose 😔")
            go1 = False
        elif c_score > blackjack:  # Computer loses if they bust
            print("Computer lose 😔")
            go1 = False
        if go1 == True:  # If the game is still ongoing
            while go:
                # Ask the player whether to hit or pass
                hit_pass = input("\nType 'y' to get another card, type 'n' to pass: \n")
                # Reset player score to recalculate after drawing
                if hit_pass == "y":  # Player chooses to hit
                    p1_cards = random.randint(0,lenn-1)
                    p1_cards_store.append(cards[p1_cards])
                    p1_score = sum(p1_cards_store)
                    print(f"\n Your Cards: {p1_cards_store},  Current score: {p1_score}")
                    if p1_score == blackjack:  # If player hits blackjack
                        if c_score < 17:  # Computer must draw another card if under 17
                            comp_cards = random.randint(0,lenn-1)
                            comp_cards_store.append(cards[comp_cards])# Recalculate computer score
                            c_score = sum(comp_cards_store)
                            print(f" Computer Card: {comp_cards}")
                            if ( p1_score > c_score and p1_score == blackjack)  or ( p1_score > c_score and p1_score < blackjack):
                                 print("Player 1 wins 😇")
                                 go = False
                            elif  (c_score > p1_score and c_score == blackjack )or (c_score > p1_score and c_score < blackjack):
                              print("Computer  wins 😇")
                              go = False
                        else:# No further actions if computer's score is 17 or higher
                           if ( p1_score > c_score and p1_score == blackjack)  or ( p1_score > c_score and p1_score < blackjack):
                                 print("Player 1 wins 😇")
                                 go = False
                           elif  (c_score > p1_score and c_score == blackjack )or (c_score > p1_score and c_score < blackjack):
                              print("Computer  wins 😇")  
                              go = False
                    elif p1_score > blackjack:  # Player busts
                        print("Player1 lose 😔")
                        print(f" Computer Card: {comp_cards_store} score: {c_score}")
                        go = False
                elif hit_pass == "n":  # Player passes
                        go1=False
                        seventeen=True
                        if c_score < 17 :  # Computer must draw if its score is less than 17
                            while seventeen:
                                    comp_cards = random.randint(0,lenn-1)
                                    comp_cards_store.append(cards[comp_cards])
                                    c_score = sum(comp_cards_store)
                                    if c_score > 17 or c_score == 17 :
                                     seventeen = False
                        print(f" Computer Card: {comp_cards_store} Current score: {c_score} ")
                        if p1_score == c_score :
                            print("Draw")
                            print(f" Player Card: {p1_cards_store}  score: {p1_score} ")
                            print(f" Computer Card: {comp_cards_store}  score: {c_score} ")
                            go = False
                        elif c_score > blackjack:  # Computer busts
                            print("Computer lose 😔")
                            print(f" Computer Card: {comp_cards_store}  score: {c_score} ")
                            go = False
                        elif ( p1_score > c_score and p1_score == blackjack)  or ( p1_score > c_score and p1_score < blackjack):
                                 print("Player 1 wins 😇")
                                 go = False
                        elif  (c_score > p1_score and c_score == blackjack )or (c_score > p1_score and c_score < blackjack):
                              print("Computer  wins 😇")
                              go = False
                        elif p1_score > blackjack:  # Player busts
                            print("Player1 lose 😔")
                            print(f" Computer Card: {comp_cards_store} score: {c_score}")
                            go = False
    else:
        print("Game Over")  # End game if all conditions are met
        go1 = False
while input("\nDo you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ") == "y":
    blackjack_game()