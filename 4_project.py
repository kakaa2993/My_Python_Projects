#!/usr/bin/env python3
import random


	

def game_brain_logic():
	#creat the matching between the numbers wtiten and the key numbers
	
	number_1 = str(random.randint(0,9))
	number_2 = str(random.randint(0,9))
	number_3 = str(random.randint(0,9))
	solution = number_1 + number_2 + number_3
	#print(solution)
	
	print("""Bagels, a deductive logic game.
		By ZAKARYA belamiri kakaa2993@gamil.com
	
	
		I am thinkin of a 3-digit number. Try to guess what is it.
		Here are some clues:
		when i say :      That means :
		  Pico             One digit is correct but in the wrong position.
		  Fermi            One digit is correct and in the right position.
		  Bagels           No digit is correct.
	
		I have throught up a number.
		  You have 10 guesses to get it.
		 """)
	#print(solution)
	
	player_solution=[]
	z=1
	while z <11:
		player_solution=[]
		print(f"Guess #{z}:")
		guess=input("> ") 
		
	
		if guess.isnumeric()==True and len(guess)==3:
			#guess=int(guess)
			guess_1,guess_2,guess_3 = guess
			if number_1 not in guess and number_2 not in guess and number_3 not in guess:
				print("Bagels")
				pass
					
			elif solution == guess:
				print("You got it!")
				replay= input("Do you want to play again? (yes or no): ")
				if replay=="yes"or replay=="y":
					z=1
					return game_brain_logic()
				elif replay=="no"or "n":
					print("Thank you for playing!")
					break	
	
					
			for t in range(1):
				if guess_1==number_1 and guess_2==number_2 or guess_1==number_1 and guess_3==number_3 or guess_2==number_2 and guess_3==number_3:
					print("Fermi Fermi \n--snip--")
					break
					
				elif guess_1==number_2 and guess_2==number_1 or guess_1==number_3 and guess_3==number_1 or guess_2==number_3 and guess_3==number_2:
					print("Pico Pico")
					break
				
				if guess_1==number_1:
					player_solution.append("Fermi")
				if guess_1 != number_1 and guess_1==number_3 or guess_1==number_2:
					player_solution.append("Pico")
				if guess_2==number_2:
					player_solution.append("Fermi")
				if guess_2 != number_2 and guess_2==number_3 or guess_2==number_1:
					player_solution.append("Pico")
				if guess_3==number_3:
					player_solution.append("Fermi")
				if guess_3 != number_3 and guess_3==number_1 or guess_3==number_2:
					player_solution.append("Pico")

			#print(player_solution)
			z+=1
			#print(z)
			print(" ".join(player_solution))
			#print(guess)
		
	
		else:
			print("You are wrong, you should write only 3 digit !")	
			pass
		
		
if __name__=="__main__":	
	print(game_brain_logic())
