#!/usr/bin/python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']#, #" "]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

len_alpha = len(alphabet)
def caesar(plain_text, shift_amount, direction):
    result_text = ""
    # if (direction != "encode") or (direction != "decode"):
    #     print("You can only type (encode) for encrypting text and (decode) for decoding text")
    for letter in plain_text:
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
