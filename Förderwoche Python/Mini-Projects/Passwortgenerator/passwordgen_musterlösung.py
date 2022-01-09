import random
import string

#append strings
letters_lower = string.ascii_lowercase
letters_upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation

options = letters_lower + letters_upper + digits + special

lenght = int(input("How long should your password be? : "))
password = ""

for i in range(lenght):
    rand = random.choice(options)           #rand = options[random.rangrange(0, len(options))]
    password = password + rand

print(password)


