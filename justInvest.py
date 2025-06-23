
from problem3 import signup_interface
from problem4 import login

"""
This file is used as a user interface for the user to select
either login or signup
"""


def user_interface():
    """
    Unified interface for logging in or signing up.
    Users can choose whether they want to log in or sign up.
    """
    print("=== Welcome to justInvest ===")
    print("1. Login")
    print("2. Signup")
    
    choice = input("Enter your choice (1 for Login, 2 for Signup): ").strip()
    
    if choice == '1':
        login()  # Call login function
    elif choice == '2':
        signup_interface()  # Call signup function
    else:
        print("Invalid choice. Please enter 1 for Login or 2 for Signup.")
    
        




if __name__ == "__main__":
    user_interface()

