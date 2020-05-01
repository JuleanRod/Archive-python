response = ""
total_balance = 0

while (response != "E"):
     print("Type D to deposit money")
     print("Type W to withdraw money")
     print("Type B to display Balance")
     print("Type E to exit")
     response = input("Enter your response now: ")
     if(response == "D"):
          new_deposit = int(input("Please enter your amount to deposit: "))
          total_balance += new_deposit
          print("*****")
     elif(response == "W"):
        with_balance = int( input("Please enter the amount you want to withdraw: "))
        if total_balance < with_balance:
            print("Not enough balance")
            print("*****")
        if total_balance > with_balance:
            total_balance -= with_balance
            print("*****")
     elif(response == "B"):
          print("Your balance is: " + str(total_balance))
          print("*****")
     elif(response == "E"):
          print("")
     else:
          print("Invalid response. Try again")
          print("*****")
