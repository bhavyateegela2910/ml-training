import random
import string

# Function to generate password
def generate_password():
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)


# Function to check password strength
def check_strength():
    password = input("Enter password to check strength: ")

    length = len(password)
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    score = sum([has_digit, has_upper, has_lower, has_symbol])

    if length >= 8 and score >= 3:
        print("Strong Password")
    elif length >= 6 and score >= 2:
        print("Medium Password")
    else:
        print("Weak Password")


# Main menu
def main():
    while True:
        print("\nPassword Generator Menu")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_password()

        elif choice == "2":
            check_strength()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


# Run program
if __name__ == "__main__":
    main()