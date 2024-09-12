import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letters_item=len(letters)
number_item=len(numbers)
symbols_item=len(symbols)
l=[]
n=[]
s=[]
print("\t!!!Welcome to the PyPassword Generator!!!\n")

lett=int(input("How many Letters would you like in you password?:\n"))
for i in range(lett):
 Generate_letters=random.randint(0,letters_item-1)
 l.append(letters[Generate_letters])

num=int(input("How many Numbers would you like in you password?:\n"))
for i in range(num):
 Generate_numbers=random.randint(0,number_item-1)
 n.append(numbers[Generate_numbers])

sym=int(input("How many Symbols would you like in you password?:\n"))
for i in range(sym):
 Generate_symbols=random.randint(0,symbols_item-1)
 s.append(symbols[Generate_symbols])

stored_keyword=[]
stored_keyword=l+n+s
stored_keyword2= ' '.join(stored_keyword) 
print("\nGenerated keywords according to your inputs                                  :",stored_keyword2,"\n")
stored_keyword_item=len(stored_keyword)
times=lett+num+sym
password=[]
for i in range(times):
 generate_pass = random.randint(0, stored_keyword_item-1)
 password.append(stored_keyword[generate_pass])
Password2=  ' '.join(password) 
print("Generated Strong  password from that generated keywords that shuffles twice  :\n",Password2) #tell me this is right or wrong