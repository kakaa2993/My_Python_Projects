#!/usr/bin/env python3


# message about the programe
print("/" *80)
print("  Hello and welcome to the days and weeks and months calculator  ".center(80,"/"))
print("  This program convert your age(by years) to days or weeks or month as you want  ".center(80,"/"))
print("/" *80)


#collect data and print the result of calculation
answer = ""
while answer != "no" or answer != "n":
	age = input("What is your age?(by years): ").strip()
	if age.isnumeric() == False:
                print('Age must be a number!!!')
                continue

	age = int(age)
	user = input("What do you want to convert to: months ,weeks , days ? ").lower().strip()
	days = age * 365
	month = (age*365)/30
	week = month *4
	if user == "month" or user == "m":
	    print(f"you lived {month:,} month")
	elif user == "days" or user == "d":
	    print(f'you lived {days:,} day')
	elif user == "weeks" or user == "w":
	    print(f'you lived {week:,} week')
	answer = input("do you want to convert again (yes/no)?").lower()
	if answer == "no" or answer == "n":
		break
print("")
print("  I wish for you a beautiful life filed with amazing moments  ".center(80,"/"))


