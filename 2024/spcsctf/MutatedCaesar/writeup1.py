
from hashlib import md5

cipher = "/:7,67Ct01;'1;'8:7*)*4A'.->-:'.:75'<0-'=88-:'n14-E"
hash_val = "14927c0edb1bfaf21c81d6b88ca9472a"

def caesar_decrypt(input_string, shift):
    output_string = ""
    for char in input_string:
        ascii_val = ord(char)
        new_ascii_val = ((ascii_val - 32 - shift) % 94) + 32
        output_string += chr(new_ascii_val)
    return output_string

for shift in range(3000):
    potential_plaintext = caesar_decrypt(cipher, shift)
    if md5(potential_plaintext.encode()).hexdigest() == hash_val:
        print(f"Found potential flag: {potential_plaintext} with shift {shift}")
        break

