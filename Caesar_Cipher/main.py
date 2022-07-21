#!/usr/bin/python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']#, #" "]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
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

    #if direction.lower().strip() == "encode":
    for letter in plain_text:
        if alphabet.index(letter)+ shift_amount > len_alpha-1:
            cipher_text += alphabet[(alphabet.index(letter) + shift) - len_alpha]

        else:
            cipher_text += alphabet[alphabet.index(letter) + shift]
    # else:
    #     print("Go away")

    print(f"The encode text is :'{cipher_text}'")
    ##���Bug alert: What happens if you try to encode the word 'civilization'?���

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(plain_text=text, shift_amount=shift)
