
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
    if password != "1234":
        raise Exception("Wrong password") # This will raise an exception if the password is incorrect
    return username