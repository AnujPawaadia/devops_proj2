import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_symbols):
    characters = ''
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the length of the password: "))
    
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special_symbols = input("Include special symbols? (yes/no): ").lower() == 'yes'
    
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_symbols)
    
    if password:
        print("Generated Password: " + password)

if __name__ == "__main__":
    main()