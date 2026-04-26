# It is a concise, readable way to create a new list by applying an expression to each item in an existing iterable (like a list, range, or string), optionally filtering items.

# using loop
squares = []
for x in range(5):
    squares.append(x*x)
print(squares)

# using list comprehension
squares2 = [x * x for x in range(5)]
print(squares2)

# find even
even = [x for x in range(20) if x%2==0]
print(even)

words = ['hello', 'world']
upper = [w.upper() for w in words]
print(upper)

# how to remember it 
# [O(output) -> L(loop) -> C(condition)] 
