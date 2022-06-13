#!/usr/bin/env python3

import random
import datetime
import logging
import timeit


''' Initialise the programe by the first discription and take the input of the number of birthdays that we would generate'''



birthday = datetime.datetime(2022, 1, 1)

print(''' Birthday paradox, by BELAMIRI Zakarya kakaa2993@gmail.com 
--snip--
'How many birthdays shall I generate? (Max 100)''')

num_of_birthdays = int(input('> '))
print("")


# start the generate birdays function
def generate_birthdays(): #Main function

	if num_of_birthdays <=100 and num_of_birthdays >= 1:
		birthdays = [ ]
		for i in range(num_of_birthdays):
			random_day_in_a_year = random.randint(1, 365)

			# timedelta let us to subttac or add days in a date
			random_days = datetime.timedelta(random_day_in_a_year)
			totall = (birthday + random_days).strftime("%b %d")
			birthdays.append(totall)
			
		print(f"Here are {num_of_birthdays} birthdays:")
		print(", ".join(birthdays))
		
		
		# sort the birthdays in a dictionary by the number of repetation for each date
		birthdays_dict = {}
		for i in birthdays:
			if i in birthdays_dict:
				birthdays_dict[i] += 1
			else:
				birthdays_dict[i] = 1
		birthdays_dict = sorted(birthdays_dict.items(), key=lambda repetition: repetition[1],reverse=True)
		if birthdays_dict[0][1] > 1:
			print(f"In this simulation, multiple people have a birthday on {birthdays_dict[0][0]} \n")
		else:
			print("All the birthdays are unique.\n")
		if input(f"Generating {num_of_birthdays} random birthdays 100,000 times ...\nPress Enter to begin...") == "":
			print("100000 simulation run...")
			
			
			#generate a random birthdays {num_of_birthdays}  100000 time:
			birthdays_list_of_100000 = [ ]	
			for i in range(100000):
				if i == 0:
					print("Let's run another 100,000 simulation.\n0 simulation run...")
				if i == 10000:
					print("10000 simulation run...\n---snip---")
				if i == 90000:
					print("90000 simulation run...")
				if i == 99999:
					print("100000 simulation run")

				
				birthdays_ = [ ]
				for g in range(num_of_birthdays):
					random_day_in_a_year = random.randint(1, 365)
					random_days = datetime.timedelta(random_day_in_a_year)
					totall = (birthday + random_days).strftime("%b %d")
					birthdays_.append(totall)

				birthdays_dict = {}
				for k in birthdays_:
					if k in birthdays_dict:
						birthdays_dict[k] += 1
					else:
						birthdays_dict[k] = 1
				birthdays_dict = sorted(birthdays_dict.items(), key = lambda repetition: repetition[1],reverse=True)
				birthdays_list_of_100000.append(birthdays_dict)

			count =0
			for list_ in birthdays_list_of_100000:
				if list_[0][1] >1:
					count +=1
			print(f"""Out of 100,000 simulations of {num_of_birthdays} people, there was a matching birthay in that group {count} times. This means that {num_of_birthdays}  people have {round(count/100000 *100)} % chance of having a matchimg birthday in their group.\nThat's more than you would expect!""")
	else:
		print("you are wrong, choose a number positive below 100")



if __name__ == "__main__":		
	generate_birthdays()
	
