# Note: Requires veterinarian.txt, zookeeper.txt, and admin.txt

# MD5 Conversion Code

# Imports
import sys
import hashlib


# Function for converting user password into MD5 Hash
# This function uses the hashlib library to convert the user password (string) into hash

def MD5_conversion(user_password, user_type):
    original = user_password
    user_type = user_type

    hashed = hashlib.md5(original.encode())  # uses hashlib to encode hashed password
    hashed2 = hashed.hexdigest()  # returns the digest for the hashed pass; returns as string containing only -
    # hexadecimals
    password_check(hashed2, user_type)

    return hashed2  # Returns hashed password for unit testing

# Function for checking the inputted password against the passwords stored in the lists
# The passwords are pre-determined in the lists


def password_check(password, zoo_type):
    user_password = password
    user_type = zoo_type

    # Lists to store pre-determined passwords

    keeper_pass = ["85ee6ee9541c8f294772e182147a5f42", "09a2ccf1476407f61867d4de719b0b97"]
    admin_pass = ["92446c031dbe789c917c6da0d7ab44b9", "1a6f3e7c72ef9fe22e0e9c21843e91d1"]
    vet_pass = ["cb8df1b3cb170724ad07ad5f64c099fe", "23245ffe3d90c2c9a7a702ab34df44bd"]

    # Check if user password is within one of the lists; also checks user user_type to ensure correct file is viewed
    # Once verification is performed, file_open is called to open the correct file

    if user_password in keeper_pass and user_type == "zookeeper":
        file_open(user_type)

    elif user_password in admin_pass and user_type == "admin":
        file_open(user_type)

    elif user_password in vet_pass and user_type == "veterinarian":
        file_open(user_type)

    else:
        print("\nInvalid Password!\n")  # If password is invalid ; returns to login loop


# File for opening and reading .txt files. Each file is related to one of the three user types


def file_open(file_select):
    if file_select == "zookeeper":  # Reads the zookeeper file and prints
        file1 = open("zooKeeper.txt", "r")
        print(file1.read())
        print("\n")
        log_out()

    if file_select == "admin":  # Reads the admin file and prints
        file2 = open("admin.txt", "r")
        print(file2.read())
        print("\n")
        log_out()

    if file_select == "veterinarian":  # Reads the veterinarian file and prints
        file3 = open("veterinarian.txt", "r")
        print(file3.read())
        print("\n")
        log_out()

# Logout function - Simple menu interface to see if user wants to log out of the system or not


def log_out():

    logout_loop = True

    print("Logout/return to menu or exit?")
    print("1 - Logout and return to menu")
    print("2 - Exit")

    while logout_loop:  # Logout loop is used to ensure user is kept in logout menu until they select 1 or 2

        logout_selection = input()
        if logout_selection == '1':
            logout_loop = False
            main()  # Returns user to main function
        elif logout_selection == '2':
            print("Goodbye!")
            sys.exit()  # Exits / terminates the program
        else:
            print("Error, please user_type 1 or 2\n")
            continue


# Main function; contains most the primary menu login system and asks for user password and username

def main():
    menu = True
    attempts = 3
    print("Welcome to the authentication system.")
    while menu:  # Menu loop for login attempts

        print("Please enter a number to continue: \n1-Login \n2-Exit")
        menuSelection = input()

        if menuSelection == '1':  # Menu selection 1
            while attempts != 0:  # Attempts counter; user only has 3 attempts
                print("Enter Username: ")
                user_name = input()  # Collect username

                print("Enter Password: ")
                user_password = input()  # Collect user password

                if user_name in ["griffin.keys", "donald.monkey"]:
                    user_type = "zookeeper"  # Assigns user user_type zookeeper
                    MD5_conversion(user_password, user_type)  # Calls md5 password conversion
                    attempts -= 1  # Subtracts 1 attempt from counter

                elif user_name in ["rosario.dawson", "bruce.grizzlybear"]:
                    user_type = "admin"
                    MD5_conversion(user_password, user_type)
                    attempts -= 1

                elif user_name in ["bernie.gorilla", "jerome.grizzlybear"]:
                    user_type = "veterinarian"
                    MD5_conversion(user_password, user_type)
                    attempts -= 1

                else:
                    print("Invalid user name!\n")
                    attempts -= 1  # Subtracts 1 attempt from counter
                    print(attempts, "Attempt(s) left\n")

                    if attempts == 0:
                        print("\nOut of login attempts. Goodbye!")
                        sys.exit()  # Exits if logout attempts are reached
                    continue  # Loop
            break  # Loop

        if menuSelection == '2':  # Menu selection 2

            yes_no_loop = True  # Variable for loop
            while yes_no_loop:  # Loop for yes or no choice

                print("Are you sure you want to exit? (y/n)")
                user_close = input()

                if user_close in ['y', 'Y']:
                    print("Goodbye!")
                    sys.exit()  # Exits if user input is Y or y

                elif user_close in ['n', 'N']:
                    yes_no_loop = False  # Ends loop and returns to main if user input is n or N
                    main()

                else:
                    print("Error, please user_type y or n")  # Error message ( not y/Y or n/N)
                    continue # Loop
        else:
            print("\nError, please enter 1 or 2\n\n")  # Menu options, if user does not input 1 or  2
            continue  # Loop


if __name__ == "__main__":
    main()
