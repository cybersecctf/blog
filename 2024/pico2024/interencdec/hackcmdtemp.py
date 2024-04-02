#python
import sys
values=sys.argv
 
def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext
ciphertext="wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}"
searchtext="pico"
shift=-1
print(sys.argv)
if len (sys.argv)>1:
 ciphertext =sys.argv[1]#for decrypt another caesar text
 if len (sys.argv)>2:
       if sys.argv.isnumeric():
            shift=sys.argv[2]
       else:
             searchtext=sys.argv[2] 
# Try all shifts from 1 to 32
if shift ==-1:
 for shift in range(1, 33):
    plaintext = caesar_decrypt(ciphertext, shift)
    if plaintext.startswith("pico"):
        print("Shift:", shift)
        print("Decrypted plaintext:", plaintext)
        break
else:
    plaintext = caesar_decrypt(ciphertext, shift)
    print("Decrypted [plaintext] in [shift]: ", plaintext,shift)
   