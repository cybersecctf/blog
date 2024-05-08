
<!DOCTYPE html>
<html>

<body>
    <h1>Modern Gaius Julius Caesar- ctflearn</h1>

    <h2>Challenge Description</h2>
    <p> One of the easiest and earliest known ciphers but with XXI century twist! Nobody uses Alphabet nowadays right? Why should you when you have your keyboard?

BUH'tdy,|Bim5y~Bdt76yQ
 
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
Modern Gaius Julius Caesar  and alphabet maybe means keyboard shift chipher that is use keyboard alphabet for shift number 
like caesar so use this code and get flag  CTFlearn{Cyb3r-Cae54r]
that should changed to have correct version of flag.
       <pre>
import sys
def keyboard_shift_decrypt(ciphertext, shift,type="qwertyus"):
    keyboard = "1234567890-=~!@#$%^&*()_+qwertyuiop[]\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<>?"
    if type == "azerty":
     keyboard = "&é\"'(-è_çàAZERTYUIOPQSDFGHJKLM<WXCVBN,;:!"


    if type=="dvorak":
         keyboard="`1234567890[]',.PYFGCRL/=AOEUIDHTNS-;QJKXBMWVZ" 
    if type=="colemak":
         keyboard="`1234567890-QWFPGJLUY;[]ARSTDHNEIO'ZXCVBKM,./"
    if type == "workman":
     keyboard = "`1234567890-=qdrwbjfup;[]ashtgyneoi'zxmcvkl,./"
    if type == "qwertz":
     keyboard = "`1234567890ß´qwertzuiopü+asdfghjklöä#<yxcvbnm,.-"
    if type == "jcukenn":
     keyboard = "йцукенгшщзхъфывапролджэячсмитьбю."
      
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
typekey="qwertyus"
ciphertext = "BUH'tdy,|Bim5y~Bdt76yQ"
if len(sys.argv)>1:
 ciphertext=sys.argv[1]
shift = 2  # Replace with the actual shift used
if len(sys.argv)>2:
 shift=sys.argv[2]
if len(sys.argv)>3:
 typekey=sys.argv[3] 
plaintext = keyboard_shift_decrypt(ciphertext, shift,typekey)
print(plaintext)

</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">CTFlearn{Cyb3r_Cae54r}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for keyboard shift cipher and crypto</p>
</body>
</html>

