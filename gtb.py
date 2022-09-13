# import subprocess
# subprocess.call(["afplay","atm-2249.mp3"])

import sys
func = ""
def login():
    user_name = input("Enter your username >")
    password = input("Enter your password >")
    if user_name=="kayode" and password=="kay1212":
        operation()
    else:
        print("Invalid details supplied. Please try again")
        login()
def operation():
    global func
    print("""Enter your operation:
        1. open an account
        2. Deposit
        3. Withdraw
        4. quit""")
    option = input(">>> ")

    if option=="1":
        func = "open"
        open()
    elif option=="2":
        func = "deposit"
        deposit()
    elif option=="3":
        func = "withdraw"
        withdraw()
    elif option=="4":
        sys.exit()
    else:
        print("Invalid input")
        operation()
def tryAgain():
    print("Enter 1. perform operation again\n 2. go to menu")
    user = input(">>>")
    if user=="1":
        if func =="open":
            open()
        elif func == "deposit":
            deposit()
        elif func=="withdraw":
            withdraw()
    elif user=="2":
        operation()
    else:
        print("Invalid input")
        tryAgain()

def open():
    val1 = input("Enter your first name")
    val2 = input("Enter your last name")
    val3 = input("your mm/dd/year")

    print( "welcome to GuarantyTrust Bank "+ "your new account Number is 0162597667")
    tryAgain()
available = int(5000)
  
def deposit():
    val2 = int(input("Enter amount >"))
    val3 = int(val2 + available )
    print ("your available balance is " + " $" + str(val3))
    tryAgain()

def withdraw():
    val2 = int(input("Enter amount >"))
    val3 =(available - val2)
    print ("your available balance is " + " $" + str(val3))
   
            
    tryAgain()

login()         
    