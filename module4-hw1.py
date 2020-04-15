west_states = "California", "Nevada", "Arizona", "Washington"
south_states = "Texas", "NewMexico", "Alabama"
east_states = "NewYork", "Illinois", "Wisconsin", "Delaware"
for count in range(5):
      employee_name = input("Please enter employee Name:")
      employee_salary = int( input("Please enter employee salary: "))
      employee_state = input( "Please enter employee state: ")
      if employee_salary > 100000 :
            federal_tax = (employee_salary * 20) / 100
      else:
            if employee_salary < 100000 :
                  federal_tax = (employee_salary * 15) / 100
      if employee_state in west_states:
            state_tax = (employee_salary * 10) / 100
      elif employee_state in south_states:
            state_tax = (employee_salary * 9) / 100
      elif employee_state in east_states:
            state_tax = (employee_salary * 8) / 100
      else:
            state_tax = (employee_salary * 12) / 100
      net_salary = employee_salary - state_tax - federal_tax
      print(employee_name + " federal tax is: " + str(federal_tax))
      print(employee_name + " state tax is: " + str(state_tax))
      print(employee_name + " net salary is: " + str(net_salary))
      print("*****")
 
