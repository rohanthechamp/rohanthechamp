import calculator_art
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

print(calculator_art.logo)
continue_calculation=True
calculator={
            "+": add,
            "-":subtract,
            "*":multiply,
            "/":division
            }
while continue_calculation:

 n1=float(input("Enter the first number: "))
 operation=input("+ \n-\n*\n/\nPick an operation: ")
 n2=float(input("Enter the second number: "))
 if operation == "+":
     result=calculator["+"](n1,n2)
     print(calculator["+"](n1,n2))

 elif  operation == "-":
      result=calculator["-"](n1,n2)
      print(calculator["-"](n1,n2))

 elif operation == "*": 
     result=calculator["*"](n1,n2)
     print(calculator["*"](n1,n2))

 elif operation == "/":
     result=calculator["/"](n1,n2)
     print(calculator["/"](n1,n2))


 restart= input("Type 'y' to continue calculating with result, or type 'n' to start a new calculation: ")

 if restart == "y":
    
    operation=input("+ \n-\n*\n/\nPick an operation: ")
    n2=float(input("Enter the second number: "))
    
    if operation == "+":
     print(calculator["+"](result,n2))

    elif  operation == "-":
      print(calculator["-"](result,n2))

    elif operation == "*": 
     print(calculator["*"](result,n2))

    elif operation == "/":
     print(calculator["/"](result,n2))

 restart= input("Type 'y' to continue calculating with result, or type 'n' to start a new calculation: ")
