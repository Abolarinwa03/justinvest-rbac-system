import hashlib
import os
import re

# Constants
SPECIAL_CHARACTERS = {"!", "@", "#", "$", "%", "?", "*", "."}
EXCLUSION_FILE = "passwd_exclusions.txt"
PASSWD_FILE = "passwd.txt"


def generate_salt(length: int = 16) -> str:
    """Generate a random salt for hashing."""
    return os.urandom(length).hex()


def hash_password(password: str, salt: str) -> str:
    """Hash the password using SHA-512 with a salt."""
    return hashlib.sha512((salt + password).encode()).hexdigest()


def is_password_valid(username: str, password: str) -> bool:
    """Check if a password meets all required criteria."""
    if len(password) < 8 or len(password) > 12:
        print("Password must be between 8 and 12 characters.")
        return False
    
    if contains_exclusion(password):
        print("Password is too weak or common.")
        return False    

    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False

    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return False

    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False

    if not any(char in SPECIAL_CHARACTERS for char in password):
        print(f"Password must contain at least one special character: {SPECIAL_CHARACTERS}")
        return False

    if username.lower() in password.lower():
        print("Password cannot include the username.")
        return False

    return True


def contains_exclusion(password: str) -> bool:
    """Check if the password matches common formats or weak patterns."""
    with open(EXCLUSION_FILE, "r") as file:
        exclusions = file.read().splitlines()
        return any(exclusion.lower() in password.lower() for exclusion in exclusions)


def write_exclusion(exclusion: str) -> None:
    """Add a new exclusion to the exclusion file."""
    with open(EXCLUSION_FILE, "a") as file:
        file.write(f"{exclusion}\n")


def add_user(username: str, password: str, role: str) -> bool:
    """Add a new user to the password file, ensuring unique usernames."""
    if os.path.exists(PASSWD_FILE):
        with open(PASSWD_FILE, "r") as file:
            if any(line.split(":")[0] == username for line in file):
                print(f"Username '{username}' already exists.")
                return False  # Username already exists

    # Generate salt and hash the password
    salt = generate_salt()
    hashed_pass = hash_password(password, salt)

    # Append the new user record to the file
    with open(PASSWD_FILE, "a") as file:
        file.write(f"{username}:{salt}:{hashed_pass}:{role}\n")

    print(f"User '{username}' added successfully.")
    return True  # User added successfully



def authenticate_user(username: str, password: str) -> bool:
    """Verify a user's credentials."""
    if not os.path.exists(PASSWD_FILE):
        print("Password file not found.")
        return False

    with open(PASSWD_FILE, "r") as file:
        for line in file:
            stored_username, salt, stored_hash, _ = line.strip().split(":")
            if stored_username == username:
                return hash_password(password, salt) == stored_hash

    print("Invalid username or password.")
    return False


# Example Usage
if __name__ == "__main__":
    # Some exclusions
    write_exclusion("password")
    write_exclusion("123456")
    write_exclusion("qwerty123")
    write_exclusion("password123")
    write_exclusion("password1")
    write_exclusion("111111")

    # Adding users to test password checker
    users = [
        {"username": "bola", "password": "Abdul@123", "role": "Clients"},
        {"username": "alex123", "password": "Alex@456", "role": "Premium Clients"},
        {"username": "jeremiah", "password": "password", "role": "Tellers"}, #invalid password case (common passwords in exclusionfile)
        {"username": "lebron23", "password": "lebronjames", "role": "Financial Advisors"}, #testing invalid password (no uppercase)
        {"username": "razak", "password": "ARSENALFC", "role": "Clients"}, #testing invlaid password (no lowercase)
        {"username": "Bukayosaka", "password": "Bukayosaka7.", "role": "Clients"},  #testing invalid password (username cannot be in password)
        {"username": "martin", "password": "Captain@", "role": "Clients"}, #invalid password (one digit at least)
        {"username": "eberechi", "password": "Lovefooty1", "role": "Clients"}, #no special character in password
        {"username": "mofewood", "password": "w00d!", "role": "Tellers"}, #less than 8 characters
        {"username": "mofarah", "password": "Myn@meisMof3rah", "role": "Clients"} #more than 12 characters
        
    ]

    for user in users:
        username = user["username"]
        password = user["password"]
        role = user["role"]

        if is_password_valid(username, password):
            if add_user(username, password, role):
                print(f"User '{username}' added successfully!")
            else:
                print(f"Failed to add user '{username}'. Username already exists.")                
        else:
            print(f"Failed to add user '{username}'. Invalid password.")

    # Authenticating users
    login_tests = [
        {"username": "bola", "password": "Abdul@123"},
        {"username": "alex123", "password": "WrongPass"},
        {"username": "bossman123", "password": "SomePass"} #nonexistent user
    ]

    for test in login_tests:
        login_username = test["username"]
        login_password = test["password"]

        if authenticate_user(login_username, login_password):
            print(f"Login successful for '{login_username}'!")
        else:
            print(f"Login failed for '{login_username}'.")
