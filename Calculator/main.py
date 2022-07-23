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
answer = round(calculation_function(num1, num2),2)


print(f" {num1} {operation_symbol} {num2} = {answer}")


def replay(result):
    player_want_to_continue = True
    replay = input("do you want to continue? type 'y' to continue and type 'n' to exit: ").lower()

    if replay == 'n':
        player_want_to_continue = False
        return 
    while player_want_to_continue:
        

        operation_symbol = input("Pick an operation symbol ('+'','-','*','/') : ")
        num3 = int(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        result = calculation_function(result, num3)

        print(f" {result} {operation_symbol} {num3} = {result}")
        replay = input("do you want to continue? type 'y' to continue and type 'n' to exit: ").lower()

        if replay == 'n':
            player_want_to_continue = False
    #replay(final_result)

replay(answer)
