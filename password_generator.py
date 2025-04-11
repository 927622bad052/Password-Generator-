import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# User input
length = int(input("Enter password length: "))
digits = input("Include digits? (y/n): ").lower() == 'y'
symbols = input("Include symbols? (y/n): ").lower() == 'y'

# Generate and show
print("Generated Password:", generate_password(length, digits, symbols))
