correct_pin='1234'
balance=5000
pin=int(input('Enter your PIN'))
if pin==correct_pin:
    while True:
        print('1. Check Balance')
        print('2. Deposit Money')
        print('3. Withdraw Money')
        print('4. Exit')
        choice=int(input('Enter your choice: '))
        if choice==1:
            print(f'Your current balance is: {balance}')
        elif choice==2:
            amount=float(input('Enter the amount to deposit: '))
            balance+=amount
            print(f'Your new balance is: {balance}')
        elif choice==3:
            amount=float(input('Enter the amount to withdraw: '))
            if amount<=balance:
                balance-=amount
                print(f'Your new balance is: {balance}')
            else:
                print('Insufficient funds')
        elif choice==4:
            break
        else:
            print('Invalid choice')
