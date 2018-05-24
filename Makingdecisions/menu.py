print "-----BREAKFAST MENU-----"
print "1. Eggs"
print "2. Pancakes"
print "3. Waffles"
print "4. Oatmeal"

choice=int(input("Enter a breakfast item:-"))

if choice==2:
    meal = "Pancackes"
elif choice==3:
    meal = "Waffles"

if choice==1:
    print "1. Wheat Toast"
    print "2. Sour Dough"
    print "3. Rye Toast"
    print "4. Pancakes"
    bread = int(input("Enter a type of bread:-"))

    if bread==1:
        print "You choose eggs with wheat toast"
    elif bread==2:
        print "You choose eggs with sour dough"
    elif bread==3:
        print "You choose eggs with rye toast"
    elif bread==4:
        print "You choose eggs with pancackes"
    else :
        print "We have eggs but not that kind of bread"

elif choice==2 or choice==3:
    print "1. Syrup"
    print "2. Strawberries"
    print "3. Powdered Sugar"
    topping = int(input("Choose a topping:-"))

    if topping==1:
        print "You choose "+meal+" with syrup"
    elif topping==2:
        print "You choose "+meal+" with strawberries"
    elif topping==3:
        print "You choose "+meal+" with Powdered Sugar"
    else :
        print "We have that "+meal+" but not that topping"

elif choice==4:
    print "You choose Oatmeal"

else :
    print "We don't serve that breakfast item"
