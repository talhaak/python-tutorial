
#Trying some functions in python 
minimum = min( 3 , 5 , 7 , 8)
print(minimum)
maximum = max( 11, 13 , 15 , 17 , 19 )
print(maximum)
absolute = abs(-2451)
print(absolute)

#The aim to calculate total costs using three functions for the vacation.

#Hotel costs.
def hotel_cost(nights):
    return nights * 140

#Transportation costs for each city.
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183 
    elif city == "Tampa":
        return 220 
    elif city == "Pittsburgh": 
        return 222
    elif city == "Los Angeles":
        return 475

# Renting cars cost whose money depends on the days.
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost = cost - 50
    elif days >= 3:
        cost = cost - 20
    return cost 

# Sum of all the costs and also the money for the extra requirements
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

# You were planning on taking a trip to LA
# for five days with $600 of spending money.
# Printing our cost.
print(trip_cost("Los Angeles", 5, 600))

