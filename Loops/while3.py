while True:
    name=input('Enter your name:- ')
    if name == 'Joe':
        password=input('Hello, Joe. What is the password ')
    else:
        continue
    if password == 'swordfish':
        break
print('Access Granted')
