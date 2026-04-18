
def divide():
    divident = input("Enter a Divident: ")
    diviser = input("Enter a Divisor: ")

    try:
        result = int(divident) / int(diviser)
        remainder = int(divident) % int(diviser)
        return result, remainder
    
    except ValueError:
        print("That's not a valid number. Please enter an integer.")

    except ZeroDivisionError:
        print("You cannot divide by zero.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        print("Thanks for using the program!")

# ***************Program 2*****************
def login():
    username = input("Enter your username:")
    password = input("Enter your password:")
    if username != "admin":
        raise Exception("User not found") # This will raise an exception if the username is incorrect
    if password != "1234":
        raise Exception("Wrong password") 
    return f"Welcome {username}!"

# Common errors in Python:

# ValueError → wrong value type
# TypeError → wrong data type
# KeyError → key not found in a dictionary
# IndexError → index out of range
# ZeroDivisionError → division by zero
# FileNotFoundError → file not found
# AttributeError → attribute not found on an object
# ImportError → module not found or cannot be imported
# NameError → variable not defined
# SyntaxError → invalid syntax

try:
    login()
except Exception as e:
    print(e)