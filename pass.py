import random
import string


def generate_password(length):
    # Define characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired password length: "))

        if length <= 0:
            print("Password length must be greater than zero.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print("Generated password: " + password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")


if __name__ == "__main__":
    main()
