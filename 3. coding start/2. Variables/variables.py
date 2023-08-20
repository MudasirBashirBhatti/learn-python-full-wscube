# wrong ways to declare variable

# 1. "2add" //dont start with number
# 2. "my first" // use space in variable declaration 
# 3. "my-first" //dont use 

# Correct ways to declare variables
# 1. "add1"
# 2. "myFirst"
# 3. "my_first"
# 4. "_myfirst"
# 5. "MyFirstVar" //SnakeCase
# 6. "myFirstVar" //camelCase
# ................................... 
# we can check "memory allocation" of variable in python using "id()"
# if values of two different variables are same there memory allocation will also be same.
a = 10
b = 10
print(a , b)
print(id(a),id(b))
# there memory allocation is same as in python memory allocation of variable is on the basis of values not by variable name