import random
import string


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials):
    characters = ''

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected."

    return ''.join(random.choice(characters) for _ in range(length))


def get_user_input():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_specials = input("Include special characters? (y/n): ").lower() == 'y'

    return length, use_uppercase, use_lowercase, use_numbers, use_specials


def main():
    print("Welcome to the Password Generator!")

    while True:
        user_input = get_user_input()
        if user_input is None:
            continue

        length, use_uppercase, use_lowercase, use_numbers, use_specials = user_input

        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials)
        print("\nGenerated Password:", password)

        another = input("\nGenerate another password? (y/n): ").lower()
        if another != 'y':
            print("Thank you for using the Password Generator!")
            break


if __name__ == "__main__":
    main()
