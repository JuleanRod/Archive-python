married = "Married", "married", "MARRIED"
single = "Single", "single", "SINGLE"
divorced = "Divorced", "divorced", "DIVORCED"
separated = "Separated", "separated", "SEPARATED"

western_region_cases = "CA", "ca", "AR", "ar", "NV", "nv", "WA", "wa"
western_region_count = 0
western_married_count = 0
western_single_count = 0
western_divorced_count = 0
western_separated_count = 0

eastern_region_cases = "NY", "ny", "MA", "ma", "FL", "fl"
eastern_region_count = 0
eastern_married_count = 0
eastern_single_count = 0
eastern_divorced_count = 0
eastern_separated_count = 0

southern_region_cases = "TX", "tx", "AL", "al", "GA", "ga"
southern_region_count = 0
southern_married_count = 0
southern_single_count = 0
southern_divorced_count = 0
southern_separated_count = 0

allcases = western_region_cases + eastern_region_cases + southern_region_cases
marital_status = married + single + divorced + separated
######
first_resides = input("please enter the state where the first person resides :")
first_ms = input("Please enter your marital status of first person :")
if first_resides not in allcases:
   print("The person is not counted towards Any of the following states. TX, AI, GA, NY, MA, FL, CA, NV, AR, or WA")
elif first_ms not in marital_status:
   print("The person is not counted towards any marital group")
second_resides = input("please enter the state where the second person resides :")
second_ms = input("Please enter your marital status of second person :")
if second_resides not in allcases:
   print("The person is not counted towards Any of the following states. TX, AI, GA, NY, MA, FL, CA, NV, AR, or WA")
elif second_ms not in marital_status:
   print("The person is not counted towards any marital group")
third_resides = input("please enter the state where the third person resides :")
third_ms = input("Please enter your marital status of third person :")
if third_resides not in allcases:
   print("The person is not counted towards Any of the following states. TX, AI, GA, NY, MA, FL, CA, NV, AR, or WA")
elif third_ms not in marital_status:
   print("The person is not counted towards any marital group")
fourth_resides = input("please enter the state where the fourth person resides :")
fourth_ms = input("Please enter your marital status of fourth person :")
if fourth_resides not in allcases:
   print("The person is not counted towards Any of the following states. TX, AI, GA, NY, MA, FL, CA, NV, AR, or WA")
elif fourth_ms not in marital_status:
   print("The person is not counted towards any marital group")
fifth_resides = input("please enter the state where the fifth person resides :")
fifth_ms = input("Please enter your marital status of fifth person :")
if fifth_resides not in allcases:
   print("The person is not counted towards Any of the following states. TX, AI, GA, NY, MA, FL, CA, NV, AR, or WA")
elif fifth_ms not in marital_status:
   print("The person is not counted towards any marital group")

#1
if first_resides in western_region_cases:
   western_region_count += 1
if first_ms in  married and first_resides in western_region_cases: 
   western_married_count += 1
if first_ms in single and first_resides in western_region_cases:
   western_single_count += 1
if first_ms in divorced and first_resides in western_region_cases:
   western_divorced_count += 1
if first_ms in separated and first_resides in western_region_cases:
   western_separated_count += 1

if first_resides in eastern_region_cases:
   eastern_region_count += 1
if first_ms in married and first_resides in eastern_region_cases:
   eastern_married_count += 1
if first_ms in single and first_resides in eastern_region_cases:
   eastern_single_count += 1
if first_ms in divorced and first_resides in eastern_region_cases:
   eastern_divorced_count += 1
if first_ms in separated and first_resides in eastern_region_cases:
   eastern_separated_count += 1
   
if first_resides in southern_region_cases:
   southern_region_count += 1
if first_ms in married and first_resides in southern_region_cases:
   southern_married_count += 1
if first_ms in single and first_resides in southrn_region_cases:
   southern_single_count += 1
if first_ms in divorced and first_resides in southern_region_cases:
   southern_divorced_count += 1
if first_ms in separated and first_resides in southern_region_cases:
   southern_separated_count += 1
#2
if second_resides in western_region_cases:
   western_region_count += 1
if second_ms in  married and second_resides in western_region_cases: 
   western_married_count += 1
if second_ms in single and second_resides in western_region_cases:
   western_single_count += 1
if second_ms in divorced and second_resides in western_region_cases:
   western_divorced_count += 1
if second_ms in separated and second_resides in western_region_cases:
   western_separated_count += 1

if second_resides in eastern_region_cases:
   eastern_region_count += 1
if second_ms in married and second_resides in eastern_region_cases:
   eastern_married_count += 1
if second_ms in single and second_resides in eastern_region_cases:
   eastern_single_count += 1
if second_ms in divorced and second_resides in eastern_region_cases:
   eastern_divorced_count += 1
if second_ms in separated and second_resides in eastern_region_cases:
   eastern_separated_count += 1
   
if second_resides in southern_region_cases:
   southern_region_count += 1
if second_ms in married and second_resides in southern_region_cases:
   southern_married_count += 1
if second_ms in single and second_resides in southern_region_cases:
   southern_single_count += 1
if second_ms in divorced and second_resides in southern_region_cases:
   southern_divorced_count += 1
if second_ms in separated and second_resides in southern_region_cases:
   southern_separated_count += 1

#3
if third_resides in western_region_cases:
   western_region_count += 1
if third_ms in  married and third_resides in western_region_cases: 
   western_married_count += 1
if third_ms in single and third_resides in western_region_cases:
   western_single_count += 1
if third_ms in divorced and third_resides in western_region_cases:
   western_divorced_count += 1
if third_ms in separated and third_resides in western_region_cases:
   western_separated_count += 1

if third_resides in eastern_region_cases:
   eastern_region_count += 1
if third_ms in married and third_resides in eastern_region_cases:
   eastern_married_count += 1
if third_ms in single and third_resides in eastern_region_cases:
   eastern_single_count += 1
if third_ms in divorced and third_resides in eastern_region_cases:
   eastern_divorced_count += 1
if third_ms in separated and third_resides in eastern_region_cases:
   eastern_separated_count += 1
   
if third_resides in southern_region_cases:
   southern_region_count += 1
if third_ms in married and third_resides in southern_region_cases:
   southern_married_count += 1
if third_ms in single and third_resides in southern_region_cases:
   southern_single_count += 1
if third_ms in divorced and third_resides in southern_region_cases:
   southern_divorced_count += 1
if third_ms in separated and third_resides in southern_region_cases:
   southern_separated_count += 1
   
#4
if fourth_resides in western_region_cases:
   western_region_count += 1
if fourth_ms in  married and fourth_resides in western_region_cases: 
   western_married_count += 1
if fourth_ms in single and fourth_resides in western_region_cases:
   western_single_count += 1
if fourth_ms in divorced and fourth_resides in western_region_cases:
   western_divorced_count += 1
if fourth_ms in separated and fourth_resides in western_region_cases:
   western_separated_count += 1

if fourth_resides in eastern_region_cases:
   eastern_region_count += 1
if fourth_ms in married and fourth_resides in eastern_region_cases:
   eastern_married_count += 1
if fourth_ms in single and fourth_resides in eastern_region_cases:
   eastern_single_count += 1
if fourth_ms in divorced and fourth_resides in eastern_region_cases:
   eastern_divorced_count += 1
if fourth_ms in separated and fourth_resides in eastern_region_cases:
   eastern_separated_count += 1
   
if fourth_resides in southern_region_cases:
   southern_region_count += 1
if fourth_ms in married and fourth_resides in southern_region_cases:
   southern_married_count += 1
if fourth_ms in single and fourth_resides in southern_region_cases:
   southern_single_count += 1
if fourth_ms in divorced and fourth_resides in southern_region_cases:
   southern_divorced_count += 1
if fourth_ms in separated and fourth_resides in southern_region_cases:
   southern_separated_count += 1
   
#5
if fifth_resides in western_region_cases:
   western_region_count += 1
if fifth_ms in  married and fifth_resides in western_region_cases: 
   western_married_count += 1
if fifth_ms in single and fifth_resides in western_region_cases:
   western_single_count += 1
if fifth_ms in divorced and fifth_resides in western_region_cases:
   western_divorced_count += 1
if fifth_ms in separated and fifth_resides in western_region_cases:
   western_separated_count += 1

if fifth_resides in eastern_region_cases:
   eastern_region_count += 1
if fifth_ms in married and fifth_resides in eastern_region_cases:
   eastern_married_count += 1
if fifth_ms in single and fifth_resides in eastern_region_cases:
   eastern_single_count += 1
if fifth_ms in divorced and fifth_resides in eastern_region_cases:
   eastern_divorced_count += 1
if fifth_ms in separated and fifth_resides in eastern_region_cases:
   eastern_separated_count += 1
   
if fifth_resides in southern_region_cases:
   southern_region_count += 1
if fifth_ms in married and fifth_resides in southern_region_cases:
   southern_married_count += 1
if fifth_ms in single and fifth_resides in southern_region_cases:
   southern_single_count += 1
if fifth_ms in divorced and fifth_resides in southern_region_cases:
   southern_divorced_count += 1
if fifth_ms in separated and fifth_resides in southern_region_cases:
   southern_separated_count += 1
   
print("*****")
print("The number of people who belong to Western region is :" + str(western_region_count))
print("The number of people who are married in Western region is :" + str(western_married_count))
print("The number of people who are single in Western region is :" + str(western_single_count))
print("The number of people who are divorced in Western region is :" + str(western_divorced_count))
print("The number of people who are separated in Western region is :" + str(western_separated_count))
print("*****")
print("The number of people who belong to Estern region is :" + str(eastern_region_count))
print("The number of people who are married in Estern region is :" + str(eastern_married_count))
print("The number of people who are single in Estern region is :" + str(eastern_single_count))
print("The number of people who are divorced in Estern region is :" + str(eastern_divorced_count))
print("The number of people who are separated in Estern region is :" + str(eastern_separated_count))
print("*****")
print("The number of people who belong to Soutern region is :" + str(southern_region_count))
print("The number of people who are married in Soutern region is :" + str(southern_married_count))
print("The number of people who are single in Soutern region is :" + str(southern_single_count))
print("The number of people who are divorced in Soutern region is :" + str(southern_divorced_count))
print("The number of people who are separated in Soutern region is :" + str(southern_separated_count))
print("*****")e
