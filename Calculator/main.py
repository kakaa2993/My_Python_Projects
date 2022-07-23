#!/usr/bin/python3


#Calculator

# addition

def add(num1, num2):
    return num1 + num2

# Subtract
def subtract(num1, num2):
    return num1 - num2

# Multiply
def multiply(num1, num2):
    return num1 * num2

# Divide
def divide(num1, num2):
    return num1 / num2

operations = {
	'+': add,
	'-': subtract,
	'*': multiply,
	'/': divide,
}

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input('Pick an operation symbol from the line above: ')

num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)


print(f" {num1} {operation_symbol} {num2} = {answer}")
