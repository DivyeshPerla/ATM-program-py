print('Welcome to DP Bank ATM')
restart=('Y')
choices = 3
balance = 100000.14
while choices >= 0:
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (1999):
        print('You entered you pin Correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawl\n')
            print('Please Press 3 To Deposit\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('What Would you like to choose?'))
            if option == 1:
                print('Your Balance is $',balance,'\n')
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How Much Would you like to withdraw? \n 100/200/500/2000 for other enter 1: '))
                if withdrawl in [100, 200,  500 , 2000 ]:
                    balance = balance - withdrawl
                    print ('\nYour Balance is now Â£',balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [100, 200,  500 , 2000 ]:
                    print('Invalid Amount, Please Re-try again \n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input(' Enter Amount:'))    

            elif option == 3:
                Pay_in = float(input('How Much Would You Like To Pay In? '))
                balance = balance + Pay_in
                print ('\nYour Balance is now $',balance)
                restart = input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please collect your card...\n')
                print('THANK YOU \n ')
                print("VISIT AGAIN")
                break
            else:
                print('Please Enter a correct number. \n')
                restart = ('y')
    elif pin != ('1999'):
        print('Incorrect Password')
        choices = choices - 1
        if choices == 0:
            print('\nNo more tries')
            break
