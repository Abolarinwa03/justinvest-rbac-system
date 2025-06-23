from problem2 import authenticate_user
PASSWD_FILE = "passwd.txt"
from problem1c import RoleBasedAccessControl
from main import Main

"""
This is the login file it logs a user into the system
"""

def login():
    """Login user interface."""
    print("=== User Login ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if authenticate_user(username, password):
        print("Login successful!")
        display_user_info(username)  # Display user details and permissions
    else:
        print("Login failed! Invalid username or password.")



def display_user_info(username: str):
    """Display user info and permissions."""
    # Open and read the passwd.txt file to get user details
    with open(PASSWD_FILE, "r") as file:
        user_info = {}
        for line in file:
            user_data = line.strip().split(":")
            file_username, _, _, role = user_data
            if file_username == username:
                user_info['username'] = file_username
                user_info['role'] = role
                break
        
    if 'username' not in user_info:
        print("User not found.")
        return
    
    # Display username and role
    print(f"Username: {user_info['username']}")
    print(f"Role: {user_info['role']}")
    
    # Now, use the role to fetch permissions from Main class
    main = Main()  # Create an instance of Main
    role = user_info['role']
    
    # Check if the user is a Teller and outside of working hours
    if role == "Tellers":
        rbac = main.rbac  # Access the RoleBasedAccessControl from Main
        if not rbac._is_within_work_hours():  # Check if it's outside working hours
            print("You are outside working hours. Access to permissions is restricted.")
            return  # Exit the function early if outside working hours    

    # Display permissions for the role
    print("Permissions:")
    main.rbac.display_permissions(role)
    




if __name__ == "__main__":
    login()