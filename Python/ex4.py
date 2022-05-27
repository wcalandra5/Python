# Define number of cars
# = sign is the assignment operator for Python
cars = 100

# Define space in a car
space_in_a_car = 4.0

# Define drivers
drivers = 30

# Define passengers
passengers = 90

# Define cars not driven - to be cars - drivers
cars_not_driven = cars - drivers

# One driver per car
cars_driven = drivers

# Capacity is cars driven times space in a car
carpool_capacity = cars_driven * space_in_a_car

# Average passengers per car is passengers divided by cars driven - though be careful, you'd want floating point for this (number with decimals. Down the line we'll get to single and double precision for these.)
average_passengers_per_car = passengers / cars_driven

# Print out information - the , is used like the << in C++ cout statements
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Calculations
x = 5
y = 2

print "This should be 2 -", x / y # 5 / 2 = 2.5 -- 2 becuase integer
print "This should be 10 -", x * y # 5 * 2 = 10

