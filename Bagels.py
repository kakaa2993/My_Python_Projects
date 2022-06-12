#!/usr/bin/env python3
import random

#This project is a gussing game called 'Poco-fermi-Bagelts'
#you can play this game by gussing and see if you are close to the solution or not.

def game_brain_logic():

	#creat the matching between the numbers wtiten and the key numbers
	number_1 = str(random.randint(0,9))
	number_2 = str(random.randint(0,9))
	number_3 = str(random.randint(0,9))
	solution = number_1 + number_2 + number_3

	print("""Bagels, a deductive logic game.
		By ZAKARYA belamiri kakaa2993@gamil.com


		I am thinkin of a 3-digit number. Try to guess what is it.
		A version of this game is featured in the book "The Big Book of Small Python Projects"
                I am thinking of a {}-digit number with no repeated digits.
		Try to guess what it is. Here are some clues:
		when I say :      That means :
		  Pico             One digit is correct but in the wrong position.
		  Fermi            One digit is correct and in the right position.
		  Bagels           No digit is correct.
		  
		  I have thought up a number.
		  You have 10 guesses to get it.
		 """)

	#The player has 10 guesses
	num_of_tries = 0
	while num_of_tries < 11: 
		player_solution=[]
		print(f"Guess #{num_of_tries}:")
		guess = input("> ")

		#Check the match between the player guess and the solution and print the message for each guess
		if guess.isnumeric() == True and len(guess) == 3:
			guess_1,guess_2,guess_3 = guess
			if number_1 not in guess and number_2 not in guess and number_3 not in guess:
				print("Bagels")
				pass

			elif solution == guess:
				print("You got it!")
				replay = input("Do you want to play again? (yes or no): ")
				if replay == "yes" or replay == "y":
					num_of_tries = 1
					game_brain_logic()
				elif replay == "no" or "n":
					print("Thank you for playing!")
					break

			for _ in range(1):
				if guess_1 == number_1 and guess_2 == number_2 or guess_1 == number_1 and guess_3 == number_3 or guess_2 == number_2 and guess_3 == number_3:
					print("Fermi Fermi")
					break

				elif guess_1 == number_2 and guess_2 == number_1 or guess_1 == number_3 and guess_3 == number_1 or guess_2 == number_3 and guess_3 == number_2:
					print("Pico Pico")
					break

				if guess_1 == number_1:
					player_solution.append("Fermi")
				if guess_1 != number_1 and guess_1 == number_3 or guess_1 == number_2:
					player_solution.append("Pico")
				if guess_2 == number_2:
					player_solution.append("Fermi")
				if guess_2 != number_2 and guess_2 == number_3 or guess_2 == number_1:
					player_solution.append("Pico")
				if guess_3 == number_3:
					player_solution.append("Fermi")
				if guess_3 != number_3 and guess_3 == number_1 or guess_3 == number_2:
					player_solution.append("Pico")

			num_of_tries += 1
			print(" ".join(player_solution))

			#check if the player wants to play again
			if num_of_tries == 11:
				player_answer = input("Do you want to play again? (yes or no): ")
				if player_answer.lower() =="yes" or player_answer.lower() == "y":
					game_brain_logic()
				else:
					print("Have a good day")
		else:
			print("You are wrong, you should write only 3 digit !")	
			pass


if __name__=="__main__":
	game_brain_logic()
