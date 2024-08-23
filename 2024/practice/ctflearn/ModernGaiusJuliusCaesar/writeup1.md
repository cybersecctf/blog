<title>Modern Gaius Julius Caesar- ctflearn</title>

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
with _ and }
<pre>
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

