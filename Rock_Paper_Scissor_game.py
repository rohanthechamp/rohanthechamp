import random # Random imported

#Giving Images
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Computer Choosing
computer=random.randint(0,2)


#You Choosing
You=int(input("Enter 0 for Rock  1 Paper 2 for Scissor: \n"))


#Showing who choose what
#You Choice
if You < 0 or You > 2:
    print("Invalid Choices")
elif You==0:
    print(f"You Choose Rock {rock}")
elif You==1:
    print(f"You Choose Paper{paper}")
elif You==2:
    print(f"You Choose Scissors {scissors}")


#Computer Choice
if computer==0:
    print(f"Computer Choose Rock {rock}")
elif computer==1:
    print(f"Computer Choose Paper {paper}")
elif computer==2:
    print(f"Computer Choose Scissors {scissors}")


#Deciding who wins
if computer == You :
    print("Game Draw ! Play new game")
    print("""
       0 0
        >
        < \n
""" )


elif (computer ==0 and You == 2) or (computer ==2 and You == 1) or (computer ==1 and You == 0):
    print("COMPUTER wins!!!")
    print(""",--.     ,--.
 (  O )   (  O )
  `--'  \  `--'
         \   _
   >-.   /   /| 
      `-.__.' \n""")

elif (computer ==2 and You == 0)or(computer ==1 and You == 2)or(computer ==0 and You == 1):
    print("YOU Won!!!")
    print(""",--.     ,--.
 (  O )   (  O )
  `--'  \  `--'
         \   _
   >-.   /   /| 
      `-.__.'""")
