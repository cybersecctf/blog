#python
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog
def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                plaintext += chr((ord(char) - int(shift) - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - int(shift) - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext
def solve(ciphertext,searchtext,shift=-1):
 if searchtext.isnumeric():
            shift=int(searchtext)
 # Try all shifts from 1 to 32
 if shift ==-1:
  for shift in range(1, 33):
    plaintext = caesar_decrypt(ciphertext, shift)
    if searchtext in plaintext :
        print("Shift:", shift)
        print("Decrypted result plaintext:", plaintext)
     
 else:
    plaintext = caesar_decrypt(ciphertext, shift)
    print("Decrypted [plaintext] in [shift]: ", plaintext,shift)
if __name__ == "__main__" :
    ciphertext=blog.set("wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}",1)
    searchtext=blog.set("",2)
    shift=blog.set(-1,3)
    solve(ciphertext,searchtext,shift)