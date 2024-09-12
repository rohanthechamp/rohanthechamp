import art
from Game_data import data
import random
import time
from colorama import Fore, Style

print(art.logo)
score=0
restart=True
a1= True
b1=True

while restart:
    if a1 == True:
         A=random.choice(data)

    if b1== True:
        B=random.choice(data)

    print(Fore.GREEN+ f"\nCompare A: {A['name']}, {A['follower_count']} , a {A['description']} from {A['country']}")
    print(art.vs)
    print(Fore.YELLOW + f"Compare B: {B['name']}, {B['follower_count']} , a {B['description']} from {B['country']}")

    user=str( input(    Fore.LIGHTBLUE_EX+   "Who has more followers Type 'A'  or 'B':  ")).lower()

    print("Comparing followers...")
    time.sleep(1)  

    if user not in ['a', 'b']:
        print(Fore.MAGENTA+"Invalid input! Please type 'A' or 'B'.")
        continue
    
    if  A == B  or B == A:
        print(Fore.CYAN+"Comparison cannot be made because it is the same account.")
        continue

    if user =="a":

            if A['follower_count'] > B['follower_count'] :
               score+=1
               print( Fore.RED+ f"🔥 You're on fire! Your current score: {score} 🔥 \n")
               a1=False
               b1=True

            elif  A['follower_count'] < B['follower_count']:
              restart = False

    elif user =="b":

            if B['follower_count'] >  A['follower_count']:
               score+=1
               print(Fore.RED +f"🔥 You're on fire! Your current score: {score} 🔥")
               b1=False
               a1=True
            
            elif  B['follower_count'] < A['follower_count']:
               restart = False  

    if restart == False:
      print( Fore.CYAN+ f"😢 Oops, that's wrong! Your final score: {score}. Better luck next time!")

