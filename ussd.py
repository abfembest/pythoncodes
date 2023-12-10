import time
acct = 200.00
#Deposit code
def deposit():
    b = float(input('Enter amount to deposit '))
    balance = acct + b
    print('You new balance is ', balance)

#Withdraw
def withdraw():
    b = float(input('Enter amount to withdraw '))
    balance = acct - b
    print('You new balance is ', balance)
#Check balance   
def balance():
    print('You new balance is ', acct)

#Load card
def load():
    b = float(input('Enter amount to load '))
    x = input('Enter amount your  phone ')
    print('Loading...')
    time.sleep(10)
    balance = acct - b
    phonebal = 0
    phonebal += b
    print('Successful\n','You new account balance is ', balance,
          'Your phone baalance is ', phonebal)


def a446():
    print('======Welecome to account management=========')
    print('\n','1. fund your account', '\n', '2. withdrawal',
          '\n', '3. chek balance', '\n', '4. load card')
    a= int(input('Enter number to transact '))
    if a == 1:
        deposit()
    elif a == 2:
        withdraw()
    elif a == 3:
        balance()
    elif a == 4:
        load()
    else:
        print('Wrong input slected')
        exit
    
a446()
