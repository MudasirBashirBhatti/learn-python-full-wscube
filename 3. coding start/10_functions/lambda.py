# lambda functions are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions that are not reused elsewhere in the code.

# 1. Basic lambda function that adds two numbers
add = lambda num1,num2: num1 + num2
print(add(5, 10))

# 2. Lambda function used with the map() function to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Use lambda when logic is short, obvious, and used once. For more complex logic or when the function is reused, it's better to define a regular function using def.