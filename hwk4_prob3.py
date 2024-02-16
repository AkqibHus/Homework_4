import random
import string

def generate_password(length=8):
    """Generates a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def is_acceptable(password, dictionary):
    """Checks if the password is acceptable."""
    if not any(char in string.punctuation for char in password):
        return False
    if password.lower() in dictionary:
        return False
    return True

def main():
    # Dictionary of common English words
    common_words = ["password", "123456", "qwerty", "letmein", "welcome", "monkey", "football", "abc123", "dragon", "superman"]
    
    # Keep track of accepted passwords
    accepted_passwords = []
    iterations = 0
    
    while len(accepted_passwords) < 40:
        iterations += 1
        password = generate_password()
        
        # Check if the password is acceptable
        if is_acceptable(password, common_words):
            accepted_passwords.append(password)
        else:
            continue
    
    # Print the accepted passwords
    for i, password in enumerate(accepted_passwords, 1):
        print(f"Accepted Password {i}: {password}")
    
    print(f"Total Iterations: {iterations}")

main()
