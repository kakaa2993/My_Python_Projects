#!/usr/bin/env python3

#This programe is a blackjack game or 21 game,

import re
import random


list_of_all_cards = {" 1":1," 2":2," 3":3," 4":4," 5":5," 6":6," 7":7," 8":8," 9":9,"10":10," K":10," Q":10," J":10," A":random.choice([1,10])}
print("""Blackjack, by BELAMIRI Zakarya kakaa2993@gmail.com

   Rules:
	Try to get as close to 21 without going over.
	King, Queens, and Jacks are worth 10 points.
	Ace are worth 1 or 11 points.
	card 2 through 10 are worty their face value.
	(H)it to take another cards.
	(S)tand to stop taking cards.
	On your first play, you can (D)ouble down to increase your bet
	but must hit exactly one more time before standing..
	In case of a tie, the bet is returned to the player.
	The dealer stope hitting at 17.""")



def cards_generator(card):

	#card number 01:
	char = ["♥","♦","♠"]
	list_1 = []

	for i in range(5):
		# The head and the bottom of the card.
		if i == 0 :
			list_1.append(" "+"-" * 7)

		# The middle of the card.
		elif i == 1:
			list_1.append(f"|{card}    |")
		elif i == 3:
			list_1.append(f"|    {card}|")
			list_1.append(" "+"-" * 7)

		#The center of the card.
		elif re.search(rf"{i}","[2]") != None :
			list_1.append(f"|  {random.choice(char)}   |")
		#print(list_1)
	return list_1


Money = 5000

def main(Money=5000):

	print(f"Money : {Money}")
	Bet = input("""How much do you want to bet? (1-5000, or QUIT)\n> """)

	# Check if the player input is match with the conditions
	if Bet.isnumeric() == True and 0 < int(Bet) <= 5000:
			print(f"Bet : {Bet}")
	else:
			print(" The Bet must be a number and must be bigger than Zero and smaller than 5000 !!!\n")
			main()


	Bet = int(Bet)
	DEALER = 0
	PLAYER = 0

	while True: # Main loop
		keys =  [i for i in list_of_all_cards.keys()]

		#DEALER.................................................
		print("")
		print("DEALER : ???")
		print("")

		DEALER_card_1 = random.choice(keys)
		DEALER_card_2 = random.choice(keys)
		DEALER = list_of_all_cards[DEALER_card_1] + list_of_all_cards[DEALER_card_2]

		#print the cards of the dealer
		D_card1, D_card2 = cards_generator("##"), cards_generator(DEALER_card_2)

		for row in zip(D_card1, D_card2):
			line_in_card_1, line_in_card_2 = row
			print(str(line_in_card_1)," ",str(line_in_card_2))


		#PLAYER...............................................
		keys =  [i for i in list_of_all_cards.keys()]
		PLAYER_card_1 = random.choice(keys)
		PLAYER_card_2 = random.choice(keys)
		PLAYER = list_of_all_cards[PLAYER_card_1] + list_of_all_cards[PLAYER_card_2]

		print("")
		print("PLAYER: {}".format(PLAYER))
		print("")



		# Print the cards of the player
		P_card1, P_card2 = cards_generator(PLAYER_card_1), cards_generator(PLAYER_card_2)

		for row in zip(P_card1, P_card2):
			line_in_card_1, line_in_card_2 = row
			print(str(line_in_card_1)," ",str(line_in_card_2))

		# The player choice and check if the player got 21 point
		print(" ")
		if PLAYER == 21:
			print("You win $ {} !!!".format(Bet*2))
			Money = Money + (Bet*2)
			print("Your Money = {}".format(Money))
			main(Money)


		print("(H)it, (S)tand, (D)ouble, down")

		PLAYER_answer = input("> ").strip().lower()





		# Add the stand function
		if PLAYER_answer == "s" or PLAYER_answer == "stand":
			#DEALER.................................................
			print("")
			print(f"DEALER : {DEALER}")
			print("")

			#print the cards of the dealer
			D_card1, D_card2 = cards_generator([DEALER_card_1), cards_generator(DEALER_card_2)

			for row in zip(D_card1, D_card2):
				line_in_card_1, line_in_card_2 = row
				print(str(line_in_card_1)," ",str(line_in_card_2))

			print("")
			print("PLAYER: {}".format(PLAYER))
			print("")



			# Print the cards of the player

			for row in zip(P_card1, P_card2):
				line_in_card_1, line_in_card_2 = row
				print(str(line_in_card_1)," ",str(line_in_card_2))


			# Do the comparision between the DEALER and the PLAYER
			










		#card 3

		if PLAYER_answer == "h" or PLAYER_answer == "hit":
			print("")

			#DEALER.................................................
			print("DEALER : ???")
			print("")
			for row in zip(D_card1, D_card2):
				line_in_card_1, line_in_card_2 = row
				print(str(line_in_card_1)," ",str(line_in_card_2))


			#PLAYER...............................................
			PLAYER_card_3 = random.choice(keys)
			PLAYER = PLAYER + list_of_all_cards[PLAYER_card_3] 

			P_card1, P_card2, P_card3= cards_generator(PLAYER_card_1), cards_generator(PLAYER_card_2), cards_generator(PLAYER_card_3)
			print("")
			print("PLAYER: {}".format(PLAYER))
			print("")

			for row in zip(P_card1, P_card2, P_card3):
				line_in_card_1, line_in_card_2, line_in_card_3 = row
				print(str(line_in_card_1)," ",str(line_in_card_2)," ",str(line_in_card_3))

			print(PLAYER)
			if PLAYER == 21:
				print("You win $ {} !!!".format(Bet*2))
				Money = Money + (Bet*2)
				print("Your Money = {}".format(Money))
				main(Money)
			elif PLAYER > 21:
				print("Bust")
				Money = Money -  (Bet*2)
				print(" Money : {} ".format(Money))
				main(Money)

		#card 4
		print("(H)it, (S)tand, (D)ouble, down")


		PLAYER_answer = input("> ").strip().lower()
		if PLAYER_answer == "h" or PLAYER_answer == "hit":
			print("")

			#DEALER.................................................
			print("DEALER : ???")
			print("")
			for row in zip(D_card1, D_card2):
				line_in_card_1, line_in_card_2 = row
				print(str(line_in_card_1)," ",str(line_in_card_2))


			#PLAYER...............................................
			PLAYER_card_4 = random.choice(keys)
			PLAYER = PLAYER + list_of_all_cards[PLAYER_card_4] 

			P_card1, P_card2, P_card3, P_card4= cards_generator(PLAYER_card_1),cards_generator(PLAYER_card_2),cards_generator(PLAYER_card_3),cards_generator(PLAYER_card_4)
			print("")
			print("PLAYER: {}".format(PLAYER))
			print("")

			for row in zip(P_card1,P_card2, P_card3, P_card4):
				line_in_card_1, line_in_card_2, line_in_card_3, line_in_card_4= row
				print(str(line_in_card_1)," ",str(line_in_card_2)," ",str(line_in_card_3)," ",str(line_in_card_4))

			print(PLAYER)
			if PLAYER == 21:
				print("You win $ {} !!!".format(Bet*2))
				Money = Money + (Bet*2)
				print("Your Money = {}".format(Money))
				main(Money)
			elif PLAYER > 21:
				print("Bust")
				Money = Money -  (Bet*2)
				print(" Money : {} ".format(Money))
				main(Money)

		# card 5
		print("(H)it, (S)tand, (D)ouble, down")


		PLAYER_answer = input("> ").strip().lower()
		if PLAYER_answer == "h" or PLAYER_answer=="hit":
			print("")

			#DEALER.................................................
			print("DEALER : ???")
			print("")
			for row in zip(D_card1,D_card2):
				line_in_card_1, line_in_card_2= row
				print(str(line_in_card_1)," ",str(line_in_card_2))


			#PLAYER...............................................
			PLAYER_card_5 = random.choice(keys)
			PLAYER =PLAYER + list_of_all_cards[PLAYER_card_5] 

			P_card1, P_card2, P_card3, P_card4, P_card5 = cards_generator(PLAYER_card_1),cards_generator(PLAYER_card_2),cards_generator(PLAYER_card_3),cards_generator(PLAYER_card_4),cards_generator(PLAYER_card_5)
			print("")
			print("PLAYER: {}".format(PLAYER))
			print("")

			for row in zip(P_card1,P_card2, P_card3, P_card4, P_card5):
				line_in_card_1, line_in_card_2, line_in_card_3, line_in_card_4, line_in_card_5 = row
				print(str(line_in_card_1)," ",str(line_in_card_2)," ",str(line_in_card_3)," ",str(line_in_card_4)," ",str( line_in_card_5))

			print(PLAYER)
			if PLAYER == 21:
				print("You win $ {} !!!".format(Bet*2))
				Money = Money + (Bet*2)
				print("Your Money = {}".format(Money))
				main(Money)
			elif PLAYER > 21:
				print("Bust")
				Money = Money -  (Bet*2)
				print(" Money : {} ".format(Money))
				main(Money)

		# card 6
		print("(H)it, (S)tand, (D)ouble, down")


		PLAYER_answer = input("> ").strip().lower()
		if PLAYER_answer == "h" or PLAYER_answer=="hit":
			print("")

			#DEALER.................................................
			print("DEALER : ???")
			print("")
			for row in zip(D_card1,D_card2):
				line_in_card_1, line_in_card_2= row
				print(str(line_in_card_1)," ",str(line_in_card_2))


			#PLAYER...............................................
			PLAYER_card_6 = random.choice(keys)
			PLAYER =PLAYER + list_of_all_cards[PLAYER_card_6] 

			P_card1, P_card2, P_card3, P_card4, P_card5, P_card6= cards_generator(PLAYER_card_1),cards_generator(PLAYER_card_2),cards_generator(PLAYER_card_3),cards_generator(PLAYER_card_4),cards_generator(PLAYER_card_5),cards_generator(PLAYER_card_6)
			print("")
			print("PLAYER: {}".format(PLAYER))
			print("")

			for row in zip(P_card1,P_card2, P_card3, P_card4, P_card5, P_card6):
				line_in_card_1, line_in_card_2, line_in_card_3, line_in_card_4, line_in_card_5, line_in_card_6 = row
				print(str(line_in_card_1)," ",str(line_in_card_2)," ",str(line_in_card_3)," ",str(line_in_card_4)," ",str( line_in_card_5)," ",str( line_in_card_6))

			print(PLAYER)
			if PLAYER == 21:
				print("You win $ {} !!!".format(Bet*2))
				Money = Money + (Bet*2)
				print("Your Money = {}".format(Money))
				main(Money)
			elif PLAYER > 21:
				print("Bust")
				Money = Money -  (Bet*2)
				print(" Money : {} ".format(Money))
				main(Money)

		break


if __name__=="__main__":
	main()
