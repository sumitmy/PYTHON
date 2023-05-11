# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

print("Welcome to the PyPassword Generator!")
# take input as number
nr_number = int(input("How many 'number' would you like in your password\n"))
# take input as letter
nr_letters = int(input("How many 'letters' would you like in your password\n"))
# take input as symbol
nr_symbol = int(input("How many 'symbol' would you like in your password\n"))

password_list = []
# for random number using in password
for char in range(0, nr_number):
    password_list += random.choice(numbers)
# for random letter using in password
for char in range(0, nr_letters):
    password_list += random.choice(letters)
# for random symbol using in password
for char in range(0, nr_symbol):
    password_list += random.choice(symbols)
# shuffle is a keyword that print lists elements randomly
random.shuffle(password_list)

password = ""
# here password adding symbol,letters and number as a str without any space
# that is look like a normal password
for char in password_list:
    password += char
print(f"your password is {password}")
