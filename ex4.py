cars = 100 #100 cars
space_in_a_car = 4 #4 seats
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
#10 cars 30 drivers = 0
cars_driven = drivers 
#one for each car
carpool_capacity = cars_driven * space_in_a_car
#how many people you can take
average_passengers_per_car = passengers / cars_driven
#amount of people over cars, simple

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

