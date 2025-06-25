print("I like volleyball")
print("it's cold outside")

# Variables - A container for a value (string, integer, floater, boolean), a variable behave as if it was the value it contains 

# Always remeber that the variables must have unique names

first_name = "talena"
print(first_name) # When printing a variable don't put it in double or single quotes, this will print the literal name of the variable and not the value

# f-strings - A feature that improves printing and readability. For example:

second_name = "barbosa"
hobbie = "draw"
print(f"my second name is {second_name} and i like to {hobbie}") # By using an f-string we can add multiple variables, making it easier to put values.

nationality = "brazilian"
holiday = "são joão"
print(f"i am {nationality} and my favorite brazilian holiday is {holiday}")

# Integer - Is a whole number, a great example of integers could be someone's age. Integers should not be between quotes because that would make it a string.

age = 18
print(f"I am {age} years old")

# Another example of integers can be quantities.

quantity = 5
print(f"I bought {quantity}kg of potatoes")

num_of_students = 35
print(f"there are {num_of_students} students in my classroom")

# Float - A float is a number, but it contains decimal portions. For example:

price = 27.55
print(f"the price for the shoe is ${price}")

gpa = 4.7
print(f"my gpa is {gpa}")

distance = 10.5
print(f"the distance until the beach is {distance}km")

# Boolean - booleans are either true or false. For example: 

is_raining = True # The true or false must be in capital
print(f"is it raining right now? {is_raining}")

# With boolean values, we really don't output them directly. It's more likely to see them being used internally within a program, such as when working with if statements. For example:

if is_raining:
    print("It's not raining")
else:
    print("It's raining right now")

for_sale = False

if for_sale:
    print("that item is not available")
else:
    print("that item is for sale")