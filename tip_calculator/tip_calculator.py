#!/usr/bin/python3

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 3.

#---------------------------Solution--------------------------


#displaty the intro message
print("Welcome to the tip calculator!")

the_bill = int(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12 , 15? "))
people = int(input("How many people to split the bill? "))
tip = (the_bill + (the_bill * (tip_percent / 100))) / people
print(f"Eash person should pay: ${tip}")
