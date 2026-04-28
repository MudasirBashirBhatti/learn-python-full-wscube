def login_required(func):
    def wrapper(*args, **kwargs):
        user_logged_in = args[0] 

        if not user_logged_in:
            print("Login required")
            return

        return func(*args, **kwargs)
    return wrapper

@login_required
def dashboard(isLoggedIn):
    print("Dashboard open")

dashboard(False)