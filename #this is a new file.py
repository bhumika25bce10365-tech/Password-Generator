import random
import string
# Simple Password Generator
print("=" * 50)
print("       Welcome to the Password Generator!")
print("=" * 50)
print()

# Ask user's name just to make it a little personal
name = input("Enter your name: ")
print(f"\nHello {name}! Let's whip up a strong password for you.\n")

# Ask for the desired password length
while True:
    try:
        length = int(input("How long should your password be? (minimum 6): "))
        
        # Basic validation
        if length < 6:
            print("Too short! Try a number 6 or above.\n")
        else:
            break
    except ValueError:
        # If user types something that’s not a number
        print("Please enter a valid number!\n")

# Options for what to include in the password
print("What should your password include?")
use_upper = input("Uppercase letters (A-Z)? (yes/no): ").strip().lower()
use_numbers = input("Numbers (0-9)? (yes/no): ").strip().lower()
use_special = input("Special characters (@#$%&*)? (yes/no): ").strip().lower()

# Start building the pool of characters
# Lowercase letters are always included
char_pool = string.ascii_lowercase

# Add to the pool based on user's choices
if use_upper in ["yes", "y"]:
    char_pool += string.ascii_uppercase

if use_numbers in ["yes", "y"]:
    char_pool += string.digits

if use_special in ["yes", "y"]:
    char_pool += "@#$%&*"

# Generate the actual password
password = ""
for _ in range(length):
    password += random.choice(char_pool)

# Show the result
print("\n" + "=" * 50)
print("Your new password is:")
print(password)
print("=" * 50)
print("\nMake sure to save it somewhere safe!")
print(f"Thanks for using the generator, {name}!")