employee_name = input("Please enter your name :")
employee_salary = int( input("Please enter your salary :"))
federaltax = employee_salary * .20
state_tax = employee_salary * .5

if(employee_salary > 100000):
    federal_tax = (employee_salary * 20) / 100
else:
    federal_tax = (employee_salary * 15) / 100

print("Your Federal Tax is :" + str(federal_tax))

state_tax = employee_salary * .05
print("Your State Tax is :" + str(state_tax))

net_salary = employee_salary - state_tax - federal_tax
print("Your net salary is :" + str(net_salary))
