users = [ 'chris', 'john', 'smith', 'paul', 'admin']
for user in users:
    if user == 'admin':
        print('Hello Admin, would you like a status report?')
    else:
        print("Hello: " + user)


# E5-10 also below in this file:


new_users = ['smith', 'paul', 'tony', 'tim', 'billy']

for item in new_users:
    item.lower()
    if item not in users:
        users.append(item)
        print('New username added.')
    elif item in users:
        print('This username is taken.')

# E5-11 Below:

ordinal_numbers = range(1, 10)
for num in ordinal_numbers:
    if num == 1 or num == 2 or num == 3:
        if num == 1:
            print('1st ')
        elif num == 2:
            print('2nd ')
        else:
            print('3rd ')
    else:
        print(str(num) + "th")

