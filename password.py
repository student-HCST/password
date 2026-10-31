import random
import string

print("===== PASSWORD GENERATOR =====")

# Take password length from user
length = int(input("Enter password length: "))

# Character collections
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = string.punctuation

# Combine all characters
all_characters = lowercase + uppercase + digits + special

# Generate password
password = ""

# Ensure all character types are included
password += random.choice(lowercase)
password += random.choice(uppercase)
password += random.choice(digits)
password += random.choice(special)

# Generate remaining characters
for i in range(length - 4):
    password += random.choice(all_characters)

# Shuffle password characters
password = ''.join(random.sample(password, len(password)))

print("Your Generated Password is:", password)