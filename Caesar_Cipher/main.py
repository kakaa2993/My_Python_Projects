#!/usr/bin/python3

from art import logo
import os


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#clear the screen
os.system("clear")
print(logo)
end_of_game = False

#the main loop
while not end_of_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    len_alpha = len(alphabet)
    def caesar(plain_text, shift_amount, direction):
        result_text = ""
        # if (direction != "encode") or (direction != "decode"):
        #     print("You can only type (encode) for encrypting text and (decode) for decoding text")

        shift_amount = shift_amount % 26
        for letter in plain_text:
            if letter not in alphabet:
                result_text += letter
            else:
                position = alphabet.index(letter)
                if direction == "decode":
                    new_position = position- shift_amount
                    result_text += alphabet[new_position]
                if direction == "encode":
                    new_position = (position + shift_amount) - len_alpha
                    if position + shift_amount > len_alpha-1:
                        result_text += alphabet[new_position]
                    else:
                        result_text += alphabet[position + shift_amount]

        print(f"The {direction}d text is :'{result_text}'")

    caesar(plain_text=text, shift_amount=shift, direction=direction)
    replay = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if replay == 'no':
        end_of_game = True
