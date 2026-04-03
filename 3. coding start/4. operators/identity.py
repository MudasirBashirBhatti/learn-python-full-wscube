# Identity operators: is, is not

# IMPORTANT:
# is      → checks if two variables point to the SAME object in memory
# is not  → checks if two variables point to DIFFERENT objects

# NOTE:
# is is NOT the same as "=="
# == compares values, while is compares memory (identity)

x = 5
y = 3

print(x is y)       # False → x and y are different objects
print(x is not y)   # True  → x and y are not the same object


# More clear explanation:
# is returns True only if both variables refer to the EXACT same object
# is not returns True if both variables refer to DIFFERENT objects

a = 1000
b = 1000

print(a == b)  # True  → values are equal
print(a is b)  # May be True or False → depends on memory