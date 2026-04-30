import getpass
import random
from datetime import datetime
balance=1000
username='amira driffa'
password='Amira123456'
max_attempts=3
attempts=0
history=[]
login_success=False
system_running=True
totalwithd=0
while system_running:
    print('Welcome to the Digital Banking System\n' \
          'Please log in to continue.')
    while attempts<max_attempts:
        a=input('Enter your username: ').strip().lower()
        b=getpass.getpass('Enter your password: ').strip()
        if a==username and b==password:
            print('Login successful!')
            login_success=True
            break
        else:
            attempts+=1
            print('Username or password incorrect. Please try again. ')
            if attempts==max_attempts:
                print('Too many failed attempts, system terminating')
                system_running=False
    while login_success:
        op=input(f'Welcome {username}!\n'
        '===BANK MENU===\n' 
        '1. Check balance.\n'
        '2. Deposit money.\n' 
        '3. Withdraw money.\n' \
        '4. View transaction history.\n' 
        '5. Exit.\n'
        '6. Logout.\n'
        '===============\n')
        operations=['1','2','3','4','5','6']
        if op not in operations:
            print('Invalid option. Please choose a number between 1 and 6.')
        else:
            if op=='1':
                print(f'Your current balance is £{balance:,}.\n')
            elif op=='2':
                while True:
                    deposit=input('Please insert your card and tell us how much money would you like to deposit? :£ \n' \
                                   'Please insert the money in slot A.')
                    try:
                        dep=int(deposit)
                        if dep<=0:
                            print('Amount must be greater than 0.')
                            continue
                    except ValueError:
                        print('Please enter a valid value.')
                        continue
                    balance+=dep
                    formatted_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(f'You deposited £{dep}.\n'
                        f'Your balance now is: £{balance:,}.\n'
                        'Remember to retrieve your card.\n')
                    his=f'Deposited £{dep} at {formatted_time}, new balance £{balance:,}.'
                    history.append(his)
                    break
            elif op=='3':
                while True:
                    withdrawal=input('Please insert your card and tell us how much money would you like to withdraw? :£ ')
                    try: 
                        withd=int(withdrawal)
                        if withd>balance:
                            print('You do not have enough money in your account to withdraw this amount.')
                            continue
                        elif withd<=0:
                            print('Amount must be greater than 0.')
                            continue
                        elif totalwithd + withd >300:
                            print('Total amount perday exceeded')
                            continue
                    except ValueError:     
                        print('Please enter a valid value.')
                        continue
                    balance-=withd
                    totalwithd+=withd
                    formatted_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(f'You withdrew £{withd}.\n'
                        f'Your balance now is: £{balance:,}.\n'
                        'Remember to retreive your card and the money from slot B.\n')
                    his1=f'Withdrew £{withd} at {formatted_time}, new balance £{balance:,}.'
                    history.append(his1)
                    break
            elif op=='4' :
                if len(history)==0:
                    print('No transactions yet.\n')
                else:
                    print('Transaction history:')
                    for transaction in history:
                        print(transaction)
            elif op=='5':
                print('Thank you for using our banking system!')
                system_running=False 
                break
            elif op=='6':
                attempts=0
                login_success=False
                break
            if op in ['1','2','3','4']:
                number = random.randint(1,6)
                if number==1:
                    if balance>=20:
                        balance-=20
                        formatted_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        history.append(f'Debit card payment £20 at {formatted_time}, new balance £{balance:,}')
                        print(f'A debit card payment of £20 occurred, new balance £{balance:,}')
                elif number==5:
                    balance+=20
                    formatted_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    history.append(f'Bank deposited £20 at {formatted_time}, new balance £{balance:,}')
                    print(f'The Bank deposited £20, new balance £{balance:,}')
                         