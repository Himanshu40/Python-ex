import sys

print('Hey, I am your basic calculator :D')
while True:
    num1 = int(input('Enter a number:- '))
    num2 = int(input('Enter another number:- '))
    op = input('Which operation do you need? +,-,/,*,// ')
    if op == '+':
        calc = num1 + num2
    elif op == '-':
        calc = num1 - num2
    elif op == '*':
        calc = num1 * num2
    elif op == '/':
        calc = num1 / num2
    elif op == '//':
        calc = num1 // num2
    else:
        print('Enter any valid operation')
        opt = input('Do you want to retry? Yes or No ')
        if opt == 'Yes':
            continue
        else:
            sys.exit()
    print(str(num1) + op + str(num2) + '=' + str(calc))
    opt = input('Any other calculation? Yes or No ')
    if opt == 'Yes':
        continue
    else:
        sys.exit()
