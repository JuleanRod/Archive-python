married = "Married", "married", "MARRIED"
single = "Single", "single", "SINGLE"
divorced = "Divorced", "divorced", "DIVORCED"
separated = "Separated", "separated", "SEPARATED"
statuses = married + single + divorced + separated 
count = 0

married_status = 0
single_status = 0
divorced_status = 0
separated_status = 0

married50plus = 0
married40s = 0
married30s = 0
married20s = 0

single50plus = 0
single40s = 0
single30s = 0
single20s = 0

divorced50plus = 0
divorced40s = 0
divorced30s = 0
divorced20s = 0

separated50plus = 0
separated40s = 0
separated30s = 0
separated20s = 0

while(count < 6):
    marital_status = input("Please enter persons marital status: ")
    age = int( input("Please enter perons age: "))
    if marital_status in married and age >= 50:
        married_status += 1
        married50plus += 1
    elif marital_status in married and (age >= 40 and age < 50):
        married_status += 1
        married40s += 1
    elif marital_status in married and (age >= 30 and age < 40):
        married_status += 1
        married30s += 1
    else:
        if marital_status in married and (age >= 20 and age < 30):
            married_status += 1
            married20s += 1
    
    
    if marital_status in single and age >= 50:
        single_status += 1
        single50plus += 1
    elif marital_status in single and (age >= 40 and age < 50):
        single_status += 1
        single40s += 1
    elif marital_status in single and (age >= 30 and age < 40):
        single_status += 1
        single30s += 1
    else:
        if marital_status in single and (age >= 20 and age < 30):
            single_status += 1
            single20s += 1
    
    
    if marital_status in divorced and age >= 50:
        divorced_status += 1
        divorced50plus += 1
    elif marital_status in divorced and (age >= 40 and age < 50):
        divorced_status += 1
        divorced50plus += 1
    elif marital_status in divorced and (age >= 30 and age < 40):
        divorced_status += 1
        divorced30s += 1
    elif marital_status in divorced and age > 20:
        divorced_status += 1
        
    else:
        if marital_status in divorced and (age >= 20 and age < 30):
            divorced_status += 1
            divorced20s += 1
    
  
    if marital_status in separated and age >= 50:
        separated_status += 1
        separated50plus += 1
    elif marital_status in separated and (age >= 40 and age < 50):
        separated_status +=1
        separated40s += 1
    elif marital_status in separated and (age >= 30 and age < 40):
        separated_status += 1
        separated30s += 1
    else:
        if marital_status in separated and (age >= 20 and age < 30):
            separated_status += 1
            separated20s += 1
    
    if age < 20:
        print("Sorry ! The person does not belong to any group")
    
    if marital_status not in statuses:
        print("Sorry! The marital status does not belong to one of the known statuses")
   
    count += 1
    
print("*****")
print("The number of pepole who are married is: " + str(married_status))
print("The number of pepole who are married and over the 50 is: " + str(married50plus))
print("The number of pepole who are married and in the age group of 40's is: " + str(married40s))
print("The number of pepole who are married and in the age group of 30's is: " + str(married30s))
print("The number of pepole who are married and in the age group of 20's is: " + str(married20s))

print("*****")
print("The number of pepole who are single is: " + str(single_status))
print("The number of pepole who are single and over the 50 is: " + str(single50plus))
print("The number of pepole who are single and in the age group of 40's is: " + str(single40s))
print("The number of pepole who are single and in the age group of 30's is: " + str(single30s))
print("The number of pepole who are single and in the age group of 20's is: " + str(single20s))

print("*****")
print("The number of pepole who are divorced is: " + str(divorced_status))
print("The number of pepole who are divorced and over the 50 is: "+ str(divorced50plus))
print("The number of pepole who are divorced and in the age group of 40's is: " + str(divorced40s))
print("The number of pepole who are divorced and in the age group of 30's is: " + str(divorced30s))
print("The number of pepole who are divorced and in the age group of 20's is: " + str(divorced20s))

print("*****")
print("The number of pepole who are separated is: " + str(separated_status))
print("The number of pepole who are separated and over the 50 is: " + str(separated50plus))
print("The number of pepole who are separated and in the age group of 40's is: " + str(separated40s))
print("The number of pepole who are separated and in the age group of 30's is: " + str(separated30s))
print("The number of pepole who are separated and in the age group of 20's is: " + str(separated20s))
print("*****") 
