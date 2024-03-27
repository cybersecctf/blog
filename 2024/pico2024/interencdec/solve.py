1:x: import string
from time import sleep

alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

def decrypt(word,key):
    
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = word
    print()
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("\nDecrypting your message...\n")
    sleep(2) # give an appearance of doing something complicated
    print("Stand by, almost finished...\n")
    sleep(2) # more of the same
    print("Your decrypted message is:\n")
    print(decrypted_message)
word=""
key=""
decrypt(word,key)