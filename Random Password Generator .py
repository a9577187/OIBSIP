import random
import string

def get_user_input():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer.")
    
    print("Include the following in your password:")
    include_letters = input("Letters? (y/n): ").lower() == 'y'
    include_numbers = input("Numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Symbols? (y/n): ").lower() == 'y'

    if not any([include_letters, include_numbers, include_symbols]):
        print("You must include at least one character type.")
        return get_user_input()
    
    return length, include_letters, include_numbers, include_symbols

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_pool = ''
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

length, use_letters, use_numbers, use_symbols = get_user_input()
password = generate_password(length, use_letters, use_numbers, use_symbols)
print(f"Generated password: {password}")