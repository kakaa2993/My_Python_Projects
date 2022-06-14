#!/usr/bin/env python3

import random
import datetime
import time


''' Explore the probability of the "Birthday Paradox" by this simulation.
You can get more info about the birthday paradox here at : https://en.wikipedia.org/wiki/Birthday_problem
This prject inspired from the book Big Small Python Programming'''



birthday = datetime.datetime(2022, 1, 1)

print(''' Birthday paradox, by BELAMIRI Zakarya kakaa2993@gmail.com 
The birthday problem asks for an approximate probability that in a group of n people at least two have the same birthday.

How many birthdays shall I generate? (Max 100)''')

num_of_birthdays = int(input('> '))
print("")


# start the generate birdays function
def generate_birthdays(): # Main function

	if num_of_birthdays <= 100 and num_of_birthdays >= 1:
		birthdays = [ ]
		for i in range(num_of_birthdays):
			random_day_in_a_year = random.randint(1, 365)

			# timedelta let us to subttac or add days in a date
			random_days = datetime.timedelta(random_day_in_a_year)
			totall = (birthday + random_days).strftime("%b %d")
			birthdays.append(totall)

		print(f"Here are {num_of_birthdays} birthdays: ")
		print(", ".join(birthdays))


		# Sorte the birthdays in a dictionary by the number of repetation for each date
		birthdays_dict = {}
		for _birthday in birthdays:
			if _birthday in birthdays_dict:
				birthdays_dict[_birthday] += 1
			else:
				birthdays_dict[_birthday] = 1

		#Sorte the birthdays and choice the most repeated birthday if it's exist.
		birthdays_dict = sorted(birthdays_dict.items(), key=lambda repetition: repetition[1],reverse=True)
		if birthdays_dict[0][1] > 1:
			print(f"In this simulation, multiple people have a birthday on {birthdays_dict[0][0]} \n")
		else:
			print("All the birthdays are unique.\n") # All birthdays are unique.
		print()

		#Generate a random birthdays {num_of_birthdays}  100000 time:
		if input(f"Generating {num_of_birthdays} random birthdays 100,000 times ...\nPress Enter to begin...") == "":
			print("100000 simulation run...")
			print("Let's run another 100,000 simulation.\n")

			birthdays_list_of_100000 = [ ]
			for count_ in range(100000):
				if count_ % 10000 == 0:
					print(count_," simulation run...")
				if count_ == 99999:
					print("100000 simulation run")

				birthdays_ = [ ]
				for _ in range(num_of_birthdays):
					random_day_in_a_year = random.randint(1, 365)
					random_days = datetime.timedelta(random_day_in_a_year)
					totall = (birthday + random_days).strftime("%b %d")
					birthdays_.append(totall)

				birthdays_dict = {}
				for i in birthdays_:
					if i in birthdays_dict:
						birthdays_dict[i] += 1
					else:
						birthdays_dict[i] = 1
				birthdays_dict = sorted(birthdays_dict.items(), key = lambda repetition: repetition[1],reverse=True)
				birthdays_list_of_100000.append(birthdays_dict)

			count = 0
			for list_ in birthdays_list_of_100000:
				if list_[0][1] > 1:
					count += 1
			print()
			print(f"""Out of 100,000 simulations of {num_of_birthdays} people, there was a matching birthay in that group {count} times. This means that {num_of_birthdays} people have {round(count/100000 *100),2} % chance of having a matchimg birthday in their group.\nThat's more than you would expect!""")
	else:
		print("you are wrong, choose a number positive below 100")



if __name__ == "__main__":
	generate_birthdays()
