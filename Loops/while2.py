while True:
    name=input('Enter your name:-')
    if name != 'Himanshu':
        continue
    print('Hello Himanshu, Welcome back')
    print('Enter Password:-')
    password=input()
    if password == '123456':
        break
print("Access Granted")
