exam1_score = int( input("Please enter your first exams score :"))
exam2_score = int( input("Please enter your second exams score :"))
exam3_score = int( input("Please enter your third exams score :"))

a_student = "A"
b_student = "B"
c_student = "C"
f_student = "F"

average_score = (exam1_score + exam2_score + exam3_score)/3

print("Your average score is :" + str(average_score))
if(average_score >= 90):
    print("Your grade :" + a_student)
if(average_score >= 80) and (average_score < 90):
    print("Your grade :" + b_student)
if(average_score >= 70) and (average_score < 80):
    print("Your grade :" + c_student)
if(average_score < 70):
    print("Your grade is :" + f_student)
