#!/usr/bin/python3
import random

letters = []
for num in range(ord("A"),ord("z")):
	if chr(num) not in ['[', '\\', ']', '^', '_', '`',]:
		letters.append(chr(num))
numbers = [num for num in range(10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+',"\\"]
#symobls = [ _ for _ in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']
#print(symbols)


