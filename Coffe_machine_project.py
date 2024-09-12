from Game_data import MENU, resources
import time
from colorama import Fore, Style
import tkinter as tk
maintenances=str
on=True
price=float(0.0)
#gui setup
window=tk.Tk()
window.title("Coffee Machine")
#labels
label=tk.Label(window,text="***  WELCOME!!! SIR TO YOUR  ***""\t\t***  _*CHAMP'S_RESTAURANT*_  ***")
label.pack()
#Entry field
enter=tk.Label(window,text="Insert money: ")
enter.pack()
entry=tk.Entry(window)
entry.pack()

while on:
        # 1. taking the input of customer
        ask=input(Fore.LIGHTCYAN_EX+"What would you like? (Espresso for this click 'e' \t Latte for this click 'l' \t Cappuccino for this click 'c'): ").lower()
        resources_value=resources
        print(f"Report of ingredients before the coffee is made: {resources_value}")
        
        #button for espresso
        if ask == "e":
                print(Fore.GREEN+" Checking resources are available for your order..... ")
                time.sleep(3)
                # 4.  Check resources sufficient?
                if resources ["water"] >= 50 and resources ["coffee"] >= 18 :
                    print("Resources are available")

                    coins=float(input(Fore.MAGENTA+f"Enter the cost. Cost for Espresso is {MENU["espresso"] ["cost"]} :  "))
                    # 6. Check transaction successful?
                    if coins == MENU["espresso"]["cost"]:
                         price = coins+price
                         resources["Profit"]=price
                         print("Your Coffee is coming...")
                         time.sleep(1)
                        # Deducting resources are left ### report after and before are left 
                         resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                         resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                         # 7. Make Coffee
                        ##  Once all resources have been deducted, tell the user “Here is your ordered coffee. Enjoy!”.
                         print("Enjoy! your espresso ")

                    elif coins >  MENU["espresso"] ["cost"]:

                         change= coins -  MENU["espresso"]["cost"]
                         coins=coins -change
                         price = coins+price
                         print(f"You have give more money. Take your change {change:.2f} \n Your Coffee is coming")
                         resources["Profit"]=price

                         time.sleep(1)
                        # Deducting resources are left ### report after and before are left 
                         resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                         resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                         # 7. Make Coffee
                        ##  Once all resources have been deducted, tell the user “Here is your ordered coffee. Enjoy!”.
                         print("Enjoy! your espresso ")
                    else:
                         print("Sorry there is not enough money. Money refunded")
                         on = False
                
                else:
                    print("To make your coffee unfortunately! we dont have enough resources")
                    on = False

        elif ask=="l":
                print(Fore.GREEN+" Checking resources are available for your order..... ")
                time.sleep(3)
                time.sleep(3)
                # 4.  Check resources sufficient?
                if resources["water"] >= 200  and  resources["milk"] >= 150 and  resources["coffee"] >= 24 :
                    print("Resources are available ")

                    coins=float(input(Fore.MAGENTA+f"Enter the cost. Cost for Espresso is {MENU["latte"]["cost"]} :  "))
                    # 6. Check transaction successful?
                    if coins == MENU["latte"] ["cost"]:
                         price = coins+price
                         resources["Profit"]=price
                         print(" Your Coffee is coming...")
                         time.sleep(1)
                         # Deducting resources are left ### report after and before are left 
                         resources["water"] -= MENU["latte"]["ingredients"]["water"]
                         resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                         resources["milk"]  -=  MENU["latte"]["ingredients"]["milk"]

                         # 7. Make Coffee
                        ##  Once all resources have been deducted, tell the user “Here is your ordered coffee. Enjoy!”. 
                         print("Enjoy! your latte ")
                    elif coins >  MENU["latte"]["cost"]:
                         change = coins -  MENU["latte"]["cost"]
                         coins=coins -change
                         price= coins+price

                         print(f"You have give more money. Take your change {change:.2f} \n Your Coffee is coming...")
                         resources["Profit"]=price
                         
                         time.sleep(1)
                           # Deducting resources are left ### report after and before are left 
                         resources["water"] -= MENU["latte"]["ingredients"]["water"]
                         resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                         resources["milk"]  -=  MENU["latte"]["ingredients"]["milk"]
                         # 7. Make Coffee
                        ##  Once all resources have been deducted, tell the user “Here is your ordered coffee. Enjoy!”.
                         print("Enjoy! your latte ")
                    else:
                         print("Sorry there is not enough money. Money refunded")
                         on = False
                else:
                    print("To make your coffee unfortunately! we dont have enough resources")
                    on = False


        elif ask=="c":
                print(Fore.GREEN+" Checking resources are available for your order..... ")
                time.sleep(3)
                
                # 4.  Check resources sufficient?
                if resources["water"] >= 250 and resources["milk"] >=100 and  resources["coffee"] >= 24 :
                    print("Resources are available ")

                    coins=float(input(Fore.MAGENTA+f"Enter the cost. Cost for Espresso is {MENU["cappuccino"]["cost"]} :  "))
                    # 6. Check transaction successful?
                    if coins == MENU["cappuccino"]["cost"]:
                         price = coins+price
                         resources["Profit"]=price

                         print("Your Coffee is coming...")
                         time.sleep(1)
                           # Deducting resources are left ### report after and before are left 
                         resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                         resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                         resources["milk"]  -=  MENU["cappuccino"]["ingredients"]["milk"]
                         
                         # 7. Make Coffee
                        ##  Once all resources have been deducted, tell the user “Here is your ordered coffee. Enjoy!”.
                         print("Enjoy! your cappuccino")
                    elif coins >  MENU["cappuccino"]["cost"]:

                         change= coins -  MENU["cappuccino"]["cost"]
                         coins=coins -change
                         price=coins+price

                         print(f"You have give more money. Take your change {change:.2f} \n Your Coffee is coming... ")
                         resources["Profit"]=price
                         time.sleep(1)
                           # Deducting resources are left ### report after and before are left 
                         resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                         resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                         resources["milk"]  -=  MENU["cappuccino"]["ingredients"]["milk"]
                         
                         # 7. Make Coffee
                        ##  Once all resources have been deducted, tell the user “Here is your ordered coffee. Enjoy!”.
                         print("Enjoy! your cappuccino")
                    else:
                         print("Sorry there is not enough money. Money refunded")
                         on = False
                else:
                    print("To make your coffee unfortunately! we dont have enough resources")
                    on = False
        else:
             print("That is not in our menu. Wrong ordered!. Order again \n")
             continue
        # 7. Report of ingredients after making the coffee
        after_report=resources
        report=input(Fore.WHITE+"Want to check report click yes or no! Only for staff members ")
      
        if report == "yes":
           print(f"Report of ingredients after the coffee is made: {after_report}")
        else:
             print("If you dont want to see the report then verify manually the resources")

        # 8. how to turn off the coffee machine
        maintenances=input(Fore.RED+"\n \t Want to turn off machine for maintenances click 'off' or continue taking next order click 'next' ")
        if maintenances == "off":
          on = False
          print("Turning off...")
          time.sleep(3)
          print(Fore.LIGHTWHITE_EX+"Turned off. Hope! all loved my Coffee")
        else:
           print("Next order Please!")
           continue
####
# 5.processing coins  