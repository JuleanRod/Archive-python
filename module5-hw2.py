def passengersTotal(pl):
    totalp = 0
    totalp = pl[0] + pl[1] + pl[2]
    return totalp
def passengersFare(tp):
    chargedTotal = tp*2.50
    return chargedTotal
def passengersDeduction(tf):
    o_cost = tf*0.50
    return o_cost
    
passenge_list = []
for bus_count in range (1,4):
    passengers = int( input("Please enter the number of passengers for bus" + str(bus_count) + " :"))
    passenger_list.append(passengers)

#main starts here
total_passengers = passengersTotal(passenger_list)
total_fare = passengersFare(total_passengers)
total_deduction = passengersDeduction(total_fare)
total_net = total_deduction
print("***********")
print("There are total " + str(total_passengers) + " passengers from three buses.")
print("The total fare earned is: $" + str(total_fare))
print("The net profit is: $" + str(total_net))
print("***********") r
