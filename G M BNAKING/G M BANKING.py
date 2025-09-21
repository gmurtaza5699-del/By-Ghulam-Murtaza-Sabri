head = 'G M Bank Limited'
tagline = 'Your Perfect Banking Partner'
print(tagline.center(100))
print(head.center(100))

print('1. Create Account')
print('2. Deposit Money')
print('3. View Account')
print('4. Withdraw Money')
print('5 Check Balance')
print('Type exit for Exit')


accounts = {
    'murtaza': {'pin': 5699, 'balance': 100000},
    'amir': {'pin': 1111, 'balance': 10000},
    'usman': {'pin': 2222, 'balance': 20000},
    'haider': {'pin': 3333, 'balance': 50000},
    'nadeem': {'pin': 4444, 'balance': 200000}
}

while True:
    user = input('Enter Need: ')

    if user == '1':
        print('Creating Account')
        name = input('Name: ')
        phone_num = input('Phone Number: ')
        pin = int(input('PIN (4 Digits): '))
        accounts[name] = {'pin': pin, 'balance': 0}
        print(f' Account name is {name}\n Phone Number is {phone_num} \n Account pin is ****')
        print('\nAccount Created Successfully\n')

    elif user == '2':
        print('Deposit Money')
        acc_name = input('Account Name: ')
        acc_pin = int(input('Enter PIN: '))
        if acc_name in accounts and accounts[acc_name]['pin'] == acc_pin:
            deposit_amount = int(input('Deposit Amount: '))
            accounts[acc_name]['balance'] += deposit_amount
            print(f"Deposited {deposit_amount}. New Balance = {accounts[acc_name]['balance']}")
        else:
            print('Check PIN or Account Name')
    elif user == '3':
            print('Your Account')
            acc_name = input('Account Name: ')
            acc_pin = int(input('Enter PIN: '))
            if acc_name in accounts and accounts[acc_name]['pin'] == acc_pin:
                print(f"Account Name: {acc_name}")
                print(f"Balance: {accounts[acc_name]['balance']}")
            else:
                print('Account does not exist or wrong PIN')
    elif user == '4':
        print('Withdrraw Money')
        acc_name = input('Account Name: ')
        acc_pin = int(input('Enter PIN: '))
        if acc_name in accounts and accounts[acc_name]['pin'] == acc_pin:
            withdraw_amount = int(input('Withdraw Amount: '))
            if withdraw_amount <= accounts[acc_name]['balance']:
                accounts[acc_name]['balance'] -= withdraw_amount
                print(f"Withdrew {withdraw_amount}. New Balance = {accounts[acc_name]['balance']}")
            else:
                print('Insufficient Balance')