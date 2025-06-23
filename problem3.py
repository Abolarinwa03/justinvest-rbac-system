from problem2 import is_password_valid
from problem2 import add_user

"""
This is the enrol system file, it has a signup function
"""

valid_roles = ["Clients", "Premium Clients", "Financial Advisors", "Financial Planners", "Tellers"]

def signup_interface():
    """
    Signup user interface for enrolling new users.
    """
    print("=== Signup Interface ===")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()
    
    while True:
        role = input("Enter your role (e.g., Clients, Premium Clients, Financial Advisors, Financial Planners, Tellers): ").strip()
        if role in valid_roles:
            break
        else:
            print("Invalid role entered. Please choose one of the following:")
            for valid_role in valid_roles:
                print(f"- {valid_role}")
                
    if not is_password_valid(username, password):
        print("Failed to sign up: Invalid password.")
        return

    if add_user(username, password, role):
        print("Signup successful! Welcome to the system.")
    else:
        print("Signup failed: Username already exists.")




if __name__ == "__main__":
    signup_interface()