for employee_count in range(1, 7):
    salary_list = []
    for year_count in range(1, 6):
        salary = int(input("Please enter employee " + str(employee_count) + " salary for year " + str(year_count) + ": "))
        salary_list.append(salary)
       average = sum(salary_list)/len(salary_list)

    print("Employee " + str(employee_count) + " smallest salary is: $" + str(min(salary_list)))
    print("Employee " + str(employee_count) + " highest salary is: $" + str(max(salary_list)))
    print("Employee " + str(employee_count) + " average salary is: $" + str(average))
    print("**********") 
