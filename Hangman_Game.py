import random
import Wordlist
import hangman

computer=random.choice(Wordlist.word_list)
print("\n!!! Welcome to HANGMAN Game !!! here you choose you discover the letters otherwise a hangman is being readying to attack you before that try to guess\n")
print(computer)
lenght=len(computer)
display=" "
for i in range(lenght):
 display+="_"
print(f"{display} This has {lenght} letter   \n")

game_over=False
add_letters=[]
lives=6

while  not game_over  :
 print(f"You have {lives} lives ")
 entered_letter=(input(str("Guess a letter: \n"))).lower()
 count=""
 if entered_letter in add_letters:
       print("You already guessed this")

 for letter in computer :
    
    if letter == entered_letter:
     
     count+=letter
     add_letters.append(entered_letter)

    elif letter in add_letters:
     count+=letter

    else:
     count+="_"

 print(count)

 if entered_letter.isalpha():
       print("")
 else:
   print("!!! Invalid input")

 if entered_letter not in computer :
    print("!!! You Guessed wrong letter. This not exist in the word  ! Now you going to lose 1 life")
    lives-=1
    if  lives == 0 :
       game_over = True
       print(f"Your ended your lives. Your lives is {lives}  ")
       print(f"\t***********************************  IT WAS {computer}!  YOU LOSE************************************************************", hangman.logo)
 else:
   print("*** You Guessed right ")
 if  "_" not in  count:
      
       game_over = True
       print("***********************************YOU WIN************************************************************")

 print(hangman.stages[lives])
