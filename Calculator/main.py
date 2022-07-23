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

def calculation():
    num1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    player_want_to_continue = True
    while player_want_to_continue:

        operation_symbol = input("Pick a symbol from the above : ")
        num2 = int(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)

        print(f" {num1} {operation_symbol} {num2} = {result}")
        replay = input(f"Do you want to continue with '{result}'? type 'y' to continue and type 'n' to restart the calculation.\n ").lower()

        if replay == 'n':
            calculation()
        elif replay == 'y':
            num1 = result
calculation()