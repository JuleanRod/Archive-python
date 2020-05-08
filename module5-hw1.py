married = ["Married", "married", "MARRIED"]
single = ["Single", "single", "SINGLE"]
divorced = ["Divorced", "divorced", "DIVORCED"]
separated = ["Separated", "separated", "SEPARATED"]
other_mstatus = [divorced + separated] 
stateTax_8 = ["CA", "ca", "AZ", "az", "NV", "nv", "WA", "wa", "SD", "sd"]
stateTax_7 = ["TX", "tx", "IL", "il", "MO", "mo", "OH", "oh", "VA", "va"]
stateTax_6 = ["NM", "nm", "OR", "or", "IN", "in"]
allstate_tax = [stateTax_6 + stateTax_7 + stateTax_8]
#calculates wages
def calculatewages(h, r):
    wages = h * r
    return wages
#calculates Federal Tax based on marital status
def calculateFederaltax(ms, salary):
    fedTax = 0
    if ms in married:
        fedTax = salary * 0.20
    elif ms in single:
        fedTax = salary * 0.25
    else:
        if ms not in other_mstatus:
            fedTax = salary * 0.22
    return fedTax
#calculates State Tax based on state of residence
def calculateStateTax(salary, residence):
    if residence in stateTax_8:
        stateTax = salary * 0.08
    elif residence in stateTax_7:
        stateTax = salary * 0.07
    elif residence in stateTax_6:
        stateTax = salary * 0.06
    else:
        if residence not in allstate_tax:
            stateTax = salary * 0.05
    return stateTax
#calculates Net Wages 
def calculateNet(salary, f, s):
    netwage = salary - f - s
    print("Your wage is: $" + str(salary))
    print("Your federal tax is: $" + str(fedtax))
    print("Your state tax is: $" + str(statetax))
    print("Your net wage is: $" + str(netwage))
    
# main starts here
emp_hours = int( input("Please enter your work hours: "))
emp_rate = int( input("Please enter your hourly rate: "))
emp_residence = input("Please enter your state of resident: ")
emp_ms = input("Please enter your marital status: ")
print("")
print("**********")
print("")
salary = calculatewages(emp_hours, emp_rate)
fedtax = calculateFederaltax(emp_ms, salary)
statetax = calculateStateTax(salary, emp_residence)
calculateNet(salary, fedtax, statetax)
print("**********")
