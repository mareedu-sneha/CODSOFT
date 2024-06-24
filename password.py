import random
import string

def password(length, uppercase, lowercase, digits, special_chars):
    string_set= ""
    if uppercase:
        string_set += string.ascii_uppercase
    if lowercase:
        string_set+= string.ascii_lowercase
    if digits:
        string_set += string.digits
    if special_chars:
        string_set += string.punctuation
    
    if string_set=="":
        print("select at least one character type.")
        return None
    
    password =""
    for i in range(length):
        password = password+random.choice(string_set)
    return password

def gen_pass():
    
    length = int(input("Enter the length of the password: "))
        
        # Prompt the user to select character types
    uppercase = input("1. uppercase letters? (yes/no): ").lower() == 'yes'
    lowercase = input("2. lowercase letters? (yes/no): ").lower() == 'yes'
    digits = input("3. digits? (yes/no): ").lower() == 'yes'
    special_chars = input("4. special characters? (yes/no): ").lower() == 'yes'
        
    res = password(length, uppercase, lowercase, digits, special_chars)
    print("Generated Password:", res)
    


gen_pass()