total_days_food = 0

total_days_gas = 0 

spent_food = int( input("Please enter the amount spent on food on Monday :"))
if(spent_food > 20):
    total_days_food += 1
spent_gas = int( input("Please enter the amount spent on gas on Monday :"))
if(spent_gas > 10):
    total_days_gas += 1


spent_food = int( input("Please enter the amount spent on food on Tuesday :"))
if(spent_food > 20):
    total_days_food += 1
spent_gas = int( input("Please enter the amount spent on gas on Tuesday :"))
if(spent_gas > 10):
    total_days_gas += 1

spent_food = int( input("Please enter the amount spent on food on Wednesday :"))
if(spent_food > 20):
    total_days_food += 1
spent_gas = int( input("Please enter the amount spent on gas on Wednesday :"))
if(spent_gas > 10):
    total_days_gas += 1
    
spent_food = int( input("Please enter the amount spent on food on Thursday :"))
if(spent_food > 20):
    total_days_food += 1
spent_gas = int( input("Please enter the amount spent on gas on Thursday :"))
if(spent_gas > 10):
    total_days_gas += 1
    
spent_food = int( input("Please enter the amount spent on food on Friday :"))
if(spent_food > 20):
    total_days_food += 1
spent_gas = int( input("Please enter the amount spent on gas on Friday :"))
if(spent_gas > 10):
    total_days_gas += 1
    
spent_food = int( input("Please enter the amount spent on food on Saturday :"))
if(spent_food > 20):
    total_days_food += 1
spent_gas = int( input("Please enter the amount spent on gas on Saturday :"))
if(spent_gas > 10):
    total_days_gas += 1
    
spent_food = int( input("Please enter the amount spent on food on Sunday :"))
if(spent_food > 20):
    total_days_food += 1
spent_gas = int( input("Please enter the amount spent on gas on Sunday :"))
if(spent_gas > 10):
    total_days_gas += 1


print("You spent more than 20 dollars per day on food in " + str(total_days_food) + " days of the week.")
print("You spent more than 10 dollars per day on gas in " + str(total_days_gas) + " days of the week. ")
