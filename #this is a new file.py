import random
import string

# Simple password generator program
print("=" * 50)
print("Welcome to Password Generator!")
print("=" * 50)
print()

# Get user name for personalization
name = input("Enter your name: ")
print(f"\nHello {name}! Let's create a strong password for you.")
print()

# Ask user for password length
while True:
    try:
        length = int(input("How long should your password be? (minimum 6): "))
        if length < 6:
            print("Password is too short! Please enter at least 6.")
        else:
            break
    except:
        print("Please enter a valid number!")

# Ask what to include in password
print("\nWhat do you want in your password?")
use_upper = input("Include uppercase letters (A-Z)? (yes/no): ").lower()
use_numbers = input("Include numbers (0-9)? (yes/no): ").lower()
use_special = input("Include special characters (@#$%&*)? (yes/no): ").lower()

# Build character set based on choices
chars = string.ascii_lowercase  # always include lowercase

if use_upper == "yes" or use_upper == "y":
    chars = chars + string.ascii_uppercase

if use_numbers == "yes" or use_numbers == "y":
    chars = chars + string.digits

if use_special == "yes" or use_special == "y":
    chars = chars + "@#$%&*"

# Generate password
password = ""
for i in range(length):
    password = password + random.choice(chars)

# Display result
print("\n" + "=" * 50)
print("Your new password is:")
print(password)
print("=" * 50)
print("\nMake sure to save it somewhere safe!")
print("Thanks for using Password Generator, " + name + "!")