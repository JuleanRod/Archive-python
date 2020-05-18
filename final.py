names_array = []
ids_array = []
score1_array = []
score2_array = []
score3_array = []
def populateSinfo():
    for count in range (1, 5):
        name = input("Please enter a student's name : ")
        student_id = int( input("Please enter the studnt's ID: "))
        score1 = int( input("Please enter first score: "))
        score2 = int( input("Please enter second score: "))
        score3 = int( input("Please enter third score: "))
        names_array.append(name)
        ids_array.append(student_id)
        score1_array.append(score1)
        score2_array.append(score2)
        score3_array.append(score3)
def displaySinfo():
    search_id = int( input("Please enter the ID of the student: "))
    for position in range(4):
        if search_id == ids_array[position]:
            print("The student name is: " + str(names_array[position]))
            print("ID is: " + str(ids_array[position]))
            print("First score is: " + str(score1_array[position]))
            print("Second score is: " + str(score2_array[position]))
            print("Third score is: " + str(score3_array[position]))
    if search_id not in ids_array:
        print("The ID is not found!")
def calculategradebyid():
    search_id = int( input("Please enter the ID of the student: "))
    for place in range(4):
        if search_id == ids_array[place]:
            average = round((score1_array[place] + score2_array[place] + score3_array[place]) / 3)
            if 100 >= average >= 90:
                grade = "A"
            elif 89 >= average >= 80:
                grade = "B"
            elif 79 >= average >= 70:
                grade = "C"
            elif 69 >= average >= 60:
                grade = "D"
            elif average < 60:
                grade = "F"
            print("The average is: " + str(average))
            print("The grade is: " + str(grade))
    if search_id not in ids_array:
        print("The ID is not found!")
def updateSinfo():
    search_id = int( input("Please enter the ID of the student: "))
    for position in range(4):
        if search_id == ids_array[position]:
            print("The student name is: " + str(names_array[position]))
            print("ID is: " + str(ids_array[position]))
            print("First score is: " + str(score1_array[position]))
            print("Second score is: " + str(score2_array[position]))
            print("Third score is: " + str(score3_array[position]))
            update_Score1 = int( input("Please enter first score: "))
            update_Score2 = int( input("Please enter second score: "))
            update_Score3 = int( input("Please enter third score: "))
            score1_array[position] = update_Score1
            score2_array[position] = update_Score2
            score3_array[position] = update_Score3
    if search_id not in ids_array:
        print("The ID is not found!")
choice = ""
while choice != "E":
    print("**** MENU OPTIONS ****")
    print("Type P to populate the student information.")
    print("Type U to update student Information")
    print("Type D to display student information.")
    print("Type C to calculate the Grade.")
    print("Type E to exit")
    choice = input("Please enter your choice: ")
    if choice == "P":
        populateSinfo()
    elif choice == "D":
        displaySinfo()
    elif choice == "U":
        updateSinfo()
    elif choice == "C":
        calculategradebyid()
    elif choice == "E":
        print("Thank you for using the program.")
        print("Bye")
    else:
        print("Invalid choice. Try again")e
