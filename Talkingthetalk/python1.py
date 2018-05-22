def sum(num1=0,num2=0):
    return (num1+num2)

def sub(num1=0,num2=0):
    return (num1-num2)

def mul(num1=0,num2=0):
    return (num1*num2)

def div(num1=1,num2=1):
    return (num1/num2)

def hello(argcount, *varargs):
    print"You passed ",argcount," arguments"
    for arg in varargs:
        print arg

print("Hello Calculator\n")
num1=int(input("Enter a number: \n"))
num2=int(input("Enter another number: \n"))
print num1," + ",num2," = ",sum(num1,num2)
print num1," - ",num2," = ",sub(num1,num2)
print num1," * ",num2," = ",mul(num1,num2)
print num1," / ",num2," = ",div(num1,num2)
hello(4,3,8,9,10)
