#!/usr/bin/python3
import random

'''a password generator '''

print('''

     .--------.
    / .------. \\
   / /        \\ \\
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  |      |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'
  

'''.center(20,'-'))
letters = []
for num in range(ord("A"),ord("z")):
	if chr(num) not in ['[', '\\', ']', '^', '_', '`',]:
		letters.append(chr(num))
numbers = [num for num in range(10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
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

# change the indexes of the characters in the password list
generated_password = []
max = len(password)
for chr in password:
	random_index = random.randint(0, max)
	generated_password.insert(random_index, str(chr))
print(generated_password)

#display the password

finall_password = ''.join(generated_password)
print()
print(f"Your password is: {finall_password}")
