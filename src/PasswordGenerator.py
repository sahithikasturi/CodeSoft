import secrets
import string

def main():
    print("=== Password Generator ===")
    
    # Get password length with validation
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length >= 8:
                break
            print("Password must be at least 8 characters long.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get character set preferences
    char_set = ''
    while not char_set:
        if input("Include lowercase letters? (y/n): ").lower() == 'y':
            char_set += string.ascii_lowercase
        if input("Include uppercase letters? (y/n): ").lower() == 'y':
            char_set += string.ascii_uppercase
        if input("Include digits? (y/n): ").lower() == 'y':
            char_set += string.digits
        if input("Include symbols? (y/n): ").lower() == 'y':
            char_set += string.punctuation
        
        if not char_set:
            print("You must enable at least one character type.")
    
    # Generate password securely
    password = ''.join(secrets.choice(char_set) for _ in range(length))
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()