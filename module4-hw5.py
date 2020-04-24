total_numbers = int( input("How many numbers do you want to enter?: "))
count = 1
sum = 0
smallest = 0
while count <= total_numbers :
    number = int( input("Please enter your number: "))
    sum += number
    if count == 1:
        smallest = number
    elif number < smallest:
        smallest = number
    count += 1
    average = float(sum)/total_numbers
print("*****")
print("")
print("The smallest number is: " + str(smallest))
print("The average is: " + str(average))
