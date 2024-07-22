
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
def solve(ciphertext, shift,type="qwertyus"):
    keyboard = "1234567890-=~!@#$%^&*()_+qwertyuiop[]\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?"
    keyboard += keyboard.upper()  # Add uppercase letters
    keyboard += ' '  # Add space
    decrypted_text = ''

    for char in ciphertext:
        if char in keyboard:
            # Get the index of the new character
            new_index = (keyboard.index(char) - shift) % len(keyboard)
            decrypted_text += keyboard[new_index]
        else:
            decrypted_text += char  # If character is not in the keyboard, just append it

    return decrypted_text

# Usage
if __name__ == "__main__" :
 ciphertext = blog.set("BUH'tdy,|Bim5y~Bdt76yQ",1)
 shift=blog.set(2,2)
 typekey=blog.set("qwertyus",3)
 plaintext = solve(ciphertext, shift,typekey)
 print(plaintext)

