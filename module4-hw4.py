p100k_salary = 0 
b50k100k_salary = 0 
b25k50k_salary = 0
below25k_salary = 0
total_fedtax = 0
total_statax = 0

choice = "no", "NO"
response = ""
while(response not in choice):
    salary = int( input("Please one persons salary: "))
    if salary >100000 :
        federal_tax = (salary * 20) / 100
    else:
        if salary < 100000 :
            federal_tax = (salary * 15) / 100
    state_tax = (salary * 5) / 100
    if salary > 100000:
        p100k_salary += 1
    elif salary >= 50000 and salary < 100000:
        b50k100k_salary += 1
    elif salary >= 25000 and salary < 50000:
        b25k50k_salary += 1
    else:
        if salary < 25000:
            below25k_salary += 1
    net_salary = salary - federal_tax - state_tax
    print("Your federal tax is :" +  str(federal_tax))
    print("Your state tax is :" + str(state_tax))
    print("Your net salaryis: " + str(net_salary))
    total_fedtax += federal_tax
    total_statax += state_tax
    response = input("Would you like to continue?(yes/no): ")
    
    
print("*****")
print("The number of pepole who earned more than 100000 is: " + str(p100k_salary))
print("The number of pepole who earned More than or equal to 50000 and less than 100000 is: " + str(b50k100k_salary))
print("The number of pepole who earned More than or equal to 25000 and less than 50000 is: " + str(b25k50k_salary   ))
print("The number of pepole who earned Below 25000 is: " + str(below25k_salary))
print("The total state tax is: " + str(total_statax))
print("The total federa tax is: " + str(total_fedtax)) 
