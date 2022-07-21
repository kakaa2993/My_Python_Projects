#!/usr/bin/python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']#, #" "]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
len_alpha = len(alphabet)
def encrypt(plain_text, shift_amount):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = (position + shift) - len_alpha
        if position + shift_amount > len_alpha-1:
            cipher_text += alphabet[new_position]

        else:
            cipher_text += alphabet[position + shift]
    print(f"The encode text is :'{cipher_text}'")

def decrypt(cipher_text,shift_amount):
    decrypt_text = ""

    for letter in cipher_text:
        position = alphabet.index(letter) 
        new_position = position- shift_amount
        decrypt_text += alphabet[new_position]

    print(f"The decode text is :'{decrypt_text}'")
    ##���Bug alert: What happens if you try to encode the word 'civilization'?���

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction =="decode":
    decrypt(cipher_text=text,shift_amount=shift)
else:
    print("You can only type (encode) for encrypting text and (decode) for decoding text")