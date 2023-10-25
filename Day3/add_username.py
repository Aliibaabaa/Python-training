# Create a python  program, with a predefined data, that accepts a username. 
# # If username is already added, display "Welcome (username)."
# If user name is already an admin, " You are an admin"
    #then ask if you want to register a new user, 
    # if yes, enter username and age
    # if no,display the list of users
# else, display " welcome (username) you are not an admin"

# if username is wrong, display "invalid username"
    # then ask if they want to register, 
    # if yes, enter username and age

# if youre an admin, you can set this new accts admin or not
# if no, list all the users
#if you are not an admin, list all the users included

user_data = [
    {   "username": "John", 
        "age": 28, 
        "is_admin": True
    },
    {   "username": "Jane", 
        "age": 25, 
        "is_admin": False
    }
]

username = input("Enter your username: ")
found_user = None

for user in user_data:
    if user["username"] == username:
        found_user = user
        break

if found_user:
    if found_user["is_admin"]:
        print(f"Welcome, {username}! You have admin privileges. \nYou are eligible to access this content")
    else:
        print(f"Welcome, {username}! You do not have admin privileges. \nYou are not eligible to access this content")
    
    new_user = input("\nDo you want to register a new user? (yes/no): ")
    if new_user == "yes":
        new_username = input("Enter the new username: ")
        new_age = input("Enter the age for the new user: ")
        if found_user["is_admin"]:
            set_as_admin = input("Do you want to set the new user as an admin? (yes/no): ")
            is_admin = (set_as_admin == "yes")
        else:
            is_admin = False
        user_data.append({"username": new_username, "age": new_age, "is_admin": is_admin})
        print("\nUser is registered successfully!")
    else:
        print("List of all users:")
        for user in user_data:
            print(f"Username: {user['username']}, Age: {user['age']}, Admin: {user['is_admin']}")
            
else:
    print("Invalid username.")
    register = input("\nDo you want to register as a new user? (yes/no): ")
    if register == "yes":
        new_username = input("Enter the new username: ")
        new_age = input("Enter the age for the new user: ")
        is_admin = input("Are you an admin? (yes/no): ")
        user_data.append({"username": new_username, "age": new_age, "is_admin": is_admin == "yes"})
        print("\nUser is registered successfully!")

print("=====")
print("List of all users:")
for user in user_data:
    print(f"Username: {user['username']}, Age: {user['age']}, Admin: {user['is_admin']}")

