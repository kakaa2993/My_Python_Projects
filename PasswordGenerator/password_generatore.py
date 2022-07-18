#!/usr/bin/python3
import random

letters = []
for num in range(ord("A"),ord("z")):
	if chr(num) not in ['[', '\\', ']', '^', '_', '`',]:
		letters.append(chr(num))
numbers = [num for num in range(10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+',"\\"]
#symobls = [ _ for _ in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']

# Display the welcome message

print("Welcome to the Password Generator!")

num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_numbers = int(input('How many numbers would you like?\n'))

password = []
index = 0
for _ in range(num_of_letters):
	index = random.choice(letters)
	password.append(index)
for _ in range(num_of_symbols):
	index = random.choice(symbols)
	password.append(index)
for _ in range(num_of_numbers):
	index = random.choice(numbers)
	password.append(index)

print(password)
