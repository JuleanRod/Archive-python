names = []  
accountnumbers = []
balances = []
def populateaccounts():
    count = 0
    for count in range (1,6):
        name = input("Please enter a name: ")
        names.append(name)
        accountnumber = int( input("Please enter an account nmber: "))
        accountnumbers.append(accountnumber)
        balance = int( input("Please enter a balance: "))
        balances.append(balance)
def findposition():
    search = int( input("Please enter the account number to search: "))
    for position in range (5):
        if search == accountnumbers[position]:
            print("Name is: " + str(names[position]))
            print(str(names[position]) + " account has the balance of : $" + str(balances[position]))
    if search not in accountnumbers:
        print("The account number not found!")
#Main starts here
choice = ""
while choice != "E":
    print("**** MENU OPTIONS ****")
    print("Type P to populate accounts")
    print("Type S to search for account")
    print("Type E to exit")
    choice = input("Please enter your choice: ")
    if choice == "P":
        populateaccounts()
    elif choice == "S":
        findposition()
    elif choice == "E":
        print("Thank you for using the program.")
        print("Bye")
    else:
        print("Invalid choice. Please try again!")u
