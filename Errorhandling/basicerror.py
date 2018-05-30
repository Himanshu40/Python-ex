try:
    value = int(input("Enter a number from 1 to 10:- "))
except:
    print("You didn't enter a number")
else:
    if (value>=1) and (value<=10):
        print("Your value :- ", value)
    else:
        print("Your value is out of range")
