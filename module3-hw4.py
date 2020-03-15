lessthan_30k = 0
between_30and50k = 0
between_50and75k = 0
morethan_75k = 0

income_first = int( input("Please enter yearly income of first person :"))
income_second = int( input("Please enter yearly income of second person :"))
income_third = int( input("Please enter yearly income of third person :"))
income_fourth = int( input("Please enter yearly income of fourth person :"))
income_fifth = int( input("Please enter yearly income of fifth person :"))
income_sixth = int( input("Please enter yearly income of sixth person :"))
income_seventh = int( input("Please enter yearly income of seventh person :"))

combined_income = income_first + income_second + income_third +income_fourth + income_fifth + income_sixth + income_seventh

if(income_first <= 30000):
    lessthan_30k += 1
if(50000 >= income_first > 30000):
    between_30and50k += 1
if(75000 >= income_first > 50000):
    between_50and75k += 1
if(income_first > 75000):
    morethan_75k += 1

if(income_second <= 30000):
    lessthan_30k += 1
if(50000 >= income_second > 30000):
    between_30and50k += 1
if(75000 >= income_second > 50000):
    between_50and75k += 1
if(income_second > 75000):
    morethan_75k += 1

if(income_third <= 30000):
    lessthan_30k += 1
if(50000 >= income_third > 30000):
    between_30and50k += 1
if(75000 >= income_third > 50000):
    between_50and75k += 1
if(income_third > 75000):
    morethan_75k += 1

if(income_fourth <= 30000):
    lessthan_30k += 1
if(50000 >= income_fourth > 30000):
    between_30and50k += 1
if(75000 >= income_fourth > 50000):
    between_50and75k += 1
if(income_fourth > 75000):
    morethan_75k += 1

if(income_fifth <= 30000):
    lessthan_30k += 1
if(50000 >= income_fifth > 30000):
    between_30and50k += 1
if(75000 >= income_fifth > 50000):
    between_50and75k += 1
if(income_fifth > 75000):
    morethan_75k += 1

if(income_sixth <= 30000):
    lessthan_30k += 1
if(50000 >= income_sixth > 30000):
    between_30and50k += 1
if(75000 >= income_sixth > 50000):
    between_50and75k += 1
if(income_sixth > 75000):
    morethan_75k += 1

if(income_seventh <= 30000):
    lessthan_30k += 1
if(50000 >= income_seventh > 30000):
    between_30and50k += 1
if(75000 >= income_seventh > 50000):
    between_50and75k += 1
if(income_seventh > 75000):
    morethan_75k += 1

print("Number of people who made less than or equal to 30000 is :" + str(lessthan_30k))
print("Number of people who made above 30000 and less than or equal to 50000 is :" + str(between_30and50k))
print("Number of people who made above 50000 and less than or equal to 75000 is :" + str(between_50and75k))
print("Number of people who made above 75000 is :" + str(morethan_75k))
print("The total(Combined) earning made by all people is :" + str(combined_income))
