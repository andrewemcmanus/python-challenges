print("Welcome to Chase bank.")

age = input("How old are you?\n")
age = int(age)
balance = input("What is your account balance?\n")
current_balance = int(balance)
action = input("What would you like to do? (deposit, withdraw, check_balance)\n")

def transaction(input1, input2):
    if input1 == "deposit":
        question = input("How much would you like to deposit?\n")
        amount = int(question)
        new_balance = input2 + amount
        string_balance = str(new_balance)
        print('Your new balance is ' + string_balance)
        return new_balance
    elif input1 == "withdraw":
        question = input("How much would you like to withdraw?\n")
        amount = int(question)
        new_balance = input2 - amount
        string_balance = str(new_balance)
        print('Your new balance is ' + string_balance)
        return new_balance
    elif input1 == "check_balance":
        string = str(input2)
        print('Your current balance is ' + string)
    else:
        print('error')

transaction(action, current_balance)
ask = input('Are you finished?[y/n]\n')
def finished(input):
    if input == 'y':
        print("Have a nice day!")
    elif input == 'n':
        action = input("What would you like to do? (deposit, withdraw, check_balance)\n")
        transaction(action, current_balance)
    else:
        print(error)
finished(ask)
