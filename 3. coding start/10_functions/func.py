# Functions are reusable blocks of code that perform a specific task. They help to break down complex problems into smaller, manageable pieces, making code more organized and easier to read.

# 1.Simple function that prints a message
def print_message():
    return "This is a simple function that prints a message."

# 2. Function with parameters
def greet(name:str):
   return f"Hello, {name}!"

# 3. Function that performs a calculation
def add(a:int, b:int):
    return a + b

# 4. Function with *args (star arguments)
def sum_all(*args):  #instead of *args we can use any name but * is important to indicate that it can take multiple arguments.
    total = 0
    for num in args:
        total += num
    return total

# 5. Function with **kwargs (double star keyword arguments)
def print_info(**kwargs):  #instead of **kwargs we can use any name but ** is important to indicate that it can take multiple keyword arguments
    return kwargs


print(greet("Mudasir"))
print(add(5, 10))
print(sum_all(1,2,3,4,5,50))
print(print_info(name= "Mudasir", age= 30, city= "New York"))