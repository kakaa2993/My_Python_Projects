#!/usr/bin/python3


#Calculator

#print(operations)
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
	'+':add,
	'-':subtract,
	'*':multiply,
	'/':divide,
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input('Pick an operation symbol from the line above: ')

function = operations[operation_symbol]
answer = function(num1, num2)


print(f" {num1} {operation_symbol} {num2} = {answer}")
