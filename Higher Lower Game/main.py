#!/usr/bin/env python3

import random
import art
import game_data
import replit

def generate_random_no():
    maximum = len(game_data.data)
    return random.randint(0, maximum-1)

def print_logo():
    replit.clear()
    print(art.logo)


def play_game(bio1, bio2):
    print(f"Compare A : {bio1['name']}, a {bio1['description']}, from {bio1['country']}")
    print(art.vs)
    print(f"Against B : {bio2['name']}, a {bio2['description']}, from {bio2['country']}")
    option = input("Who has more followers ? Type 'A' or 'B' : ")
    option = option.strip().upper()
    return option



def correct_option(bio1, bio2):
    if bio1['follower_count'] > bio2['follower_count']:
        print("A is the correct answer")
        return 'A'
    print("B is the correct answer") 
    return 'B'

def main():
    replit.clear()
    is_game_play = True
    score_card = 0
    bio1 = game_data.data[generate_random_no()]
    bio2 = game_data.data[generate_random_no()]
    print(art.logo)
    choosen_option = play_game(bio1, bio2)
    correct_answer = correct_option(bio1, bio2)
    while(is_game_play):
        if choosen_option == correct_answer:
            score_card += 1
            print_logo()
            print(f'You are right. Current Score {score_card}')
            bio1 = bio2
            bio2 = game_data.data[generate_random_no()]
            choosen_option = play_game(bio1, bio2)
            correct_answer = correct_option(bio1, bio2)
        else:
            print_logo()
            print(f'Sorry, that\'s wrong, Final Score : {score_card}')
            is_game_play = False

    # Ask the player if he want to play again
    replay = input("Do you want to play again? [yes('y') or no('n')]: ")
    if replay.lower() == "yes" or replay.lower() == "y":
        main()
    else:
        print()
        print(" Thank you for playing ".center(80, "."))
if __name__ == '__main__':
    main()
