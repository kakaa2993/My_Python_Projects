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
#symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
symbols = [ _ for _ in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']

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
	index = str(random.choice(numbers))
	password.append(index)
# change the indexes of the characters in the password list
random.shuffle(password)

#display the password

finall_password = ''.join(password)
print('''
            .-""-.
           / .--. \\
          / /    \\ \\
          | |    | |
          | |.-""-.|
         ///`.::::.`\\
        ||| ::/  \:: ;
        ||; ::\__/:: ;
         \\\\ '::::' /
          `=':-..-'`



''')
print(f"Your password is: \"{finall_password}\"")
