#reister
# - email, first name, last name and password
# - generate account number

#login
# - Account number and password

# Bank operations

#Initializing the system
import random

database = {}   #also dictionary

def init():

    print("Welcome to Meta Bank")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n "))

    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        register()

    else:
        print("You have selected an invalid option")

        init()

def login():

    print("Please login")

    accountNumberFromUser = int(input("What is your account number \n"))
    password = input("What is your Password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)

    print('Invalid account or password')
    login()

def register():
    print(">>>> Register <<<<")

    email = input("your Email \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create Password \n")

    accountNumber = generateAcountNumber()

    database[accountNumber] = [ first_name, last_name, email, password, 0 ]

    print("       ****  Welcome  ****   ")
    print("****  Your Account is ready  ****")
    print("Your Account Number is: %d" % accountNumber)

    login()

def bankOperation(user):

    print("**** Welcome %s %s " % ( user(0), user(1)) )

    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit"))

    if(selectedOption == 1):
        depositOperation()

    elif(selectedOption == 2):
        withdrawalOperation()

    elif(selectedOption == 3):
        logout()

    elif(selectedOption == 4):
        exit

    else:
        print("Invalid Operation")

        bankOperation(user)

def withdrawalOperation():
    print("Withdrawal")

def depositOperation():
    print("Deposit")

def generateAcountNumber():
    return random.randrange(1111111111,9999999999)

def logout():
    login()

init()
