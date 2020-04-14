dep_1000plus = 0
dep_500to999 = 0
dep_100to499 = 0
dep_below100 = 0
total_balance = 0
for count in range(7):
    deposit = int( input("Please enter your deposit amount: "))
    if deposit >= 1000:
        dep_1000plus += 1
    elif deposit >= 500 and deposit <= 999:
        dep_500to999 += 1
    elif 100 <= deposit and deposit <= 499:
        dep_100to499 += 1
    elif deposit >= 0 and deposit <= 99:
        dep_below100 += 1
    else:
        if deposit < 0:
            print("You entered a wrong amount!")
    total_balance += deposit
    
print("You have " + str(dep_1000plus) + " deposit over or equal to 1000 dollars.")
print("You have " + str(dep_500to999) + " deposit between 500 and 999.")
print("You have " + str(dep_100to499) + " deposit between 100 and 499 dollars.")
print("You have " + str(dep_below100) + " deposit below 100 dollars.")
print("Your balance is : " + str(total_balance))
