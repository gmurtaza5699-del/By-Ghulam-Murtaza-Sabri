import datetime


print('My Contacts')

print('\nRecent Calls\n'
    'murtaza''  ''12:09 AM\n'
    'haider''   ''01:49 PM\n'
    'bilal''    ''10:09 AM\n')


contacts = {
    'murtaza': '03132832349',
    'ali': '03132832349',
    'haider': '03132832349',
    'bilal': '03132832349',
}


while True:
    print('1: Add Contact(1) \n2: View Contact(2) \n3: Call Number(3) \n4: Send Messeage(4) \n5: Search Contact \nType exit to exit')
    user = input('Enter: ') 
    if user == '1':
        print('Add Contact')
        name = input('Name: ')
        number = int(input('Number: '))
        print('\nAdded to Contacts\n')
        contacts[name] = number
    elif user == '2':
        print('View Contacts')
        print(f'\n{contacts}\n')
    elif user == '3':
        print('Call Number')
        dial_name = input('Enter Number: ')
        if dial_name in contacts:
            print(f'\nNumber you have dial is busy  {datetime.datetime.now()}\n')
            print('Call ended')
        else:
            print('\nContact not found!\n')
    elif user == '4':
        print('Send Messeage')
        contact_name = input('Contact Name: ')       
        if contact_name in contacts:
            messeage = input('Message: ') 
            print(f'\nMesseage sent to {contact_name}\n')
        else:
            print('\nContact not found\n')
    elif user == '5':
        print('Search Contact')
        search = input('Search: ')
        if search in contacts:
            print(f'\n{search}: {contacts[search]}\n')
        else:
            print('\nContact not found\n')
    elif user == 'exit':
        print('Thanks for using')
        break
    else:
        print('Some thing went wrong')